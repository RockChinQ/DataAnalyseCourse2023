import re
import datetime

from bs4 import BeautifulSoup
import requests

from .. import model as crawler_model


@crawler_model.crawler("newstjuteducn", ["https://news.tjut.edu.cn/.+"])
class NewsTJUTEduCNCrawler(crawler_model.AbsSiteCrawler):

    root_url = "https://news.tjut.edu.cn/"
    
    def do(self, url: str, **kwargs) -> list[crawler_model.news.News]:
        timeout = kwargs['timeout'] if 'timeout' in kwargs else 10

        resp = requests.get(
            url=url,
            headers=self.make_headers(),
            timeout=timeout
        )
        
        if resp.status_code != 200:
            raise Exception("HTTP status code is not 200")
        
        resp.encoding = "utf-8"

        soup = BeautifulSoup(resp.text, "html.parser")

        table_element = soup.select("#main > div.page2.box > div.w720.fl > table > tr")

        # print(table_element)

        # print(len(table_element))

        news: list[crawler_model.news.News] = []

        for ele in table_element:

            id = ele.get("id")

            if id is None:
                continue

            if not id.startswith("line"):
                continue

            # print("ele: ", ele)

            # print(ele.find_all("td")[1].find("a"))

            href = ele.find_all("td")[1].find("a").get("href")

            new = self.detail(url=self.root_url+href)

            # print(new)

            news.append(new)

        return news

    def detail(self, url: str, **kwargs) -> crawler_model.news.News:
        resp = requests.get(
            url=url,
            headers=self.make_headers(),
            timeout=10
        )

        if resp.status_code != 200:
            raise Exception("HTTP status code is not 200")
        
        resp.encoding = "utf-8"

        soup = BeautifulSoup(resp.text, "html.parser")

        # print(soup)

        # print(soup.select("#main > div.page2.box > div.w720.fl > table > tbody > tr > td > form"))

        content = soup.find("div", class_="main_content")

        title = content.select_one("div > div > h1").text.strip()

        sub_title = content.select_one("div > div > div").text.strip()

        # print(sub_title)
        # 发布时间：2023-10-31 作者：张耀文 来源：

        date_str = re.search(r"发布时间：(.+)作者", sub_title).group(1)

        # print(date_str)

        date_obj = datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d")

        imgs = content.select("img")

        # print(imgs)

        images = [self.root_url+img.get("src") for img in imgs]

        return crawler_model.news.News(
            title=title,
            published_at=date_obj,
            images=images
        )

        


