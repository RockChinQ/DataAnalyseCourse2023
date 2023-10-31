import abc

from fake_useragent import UserAgent

from ..entities import news


class AbsSiteCrawler(metaclass=abc.ABCMeta):

    def do(self, url: str, **kwargs) -> list[news.News]:
        pass

    def make_headers(self, **kwargs) -> dict:
        ua = UserAgent()
        return {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": ua.random,
        }


crawler_impls = {}
"""
网页爬虫适配器列表

{
    "crawler1": {
        "regexp": [
            "https://www\\.example\\.com/.*"  
        ],
        "cls": <class 'exp2.crawler.example.ExampleSiteCrawler'>
    }
}
"""

# 爬虫实现装饰器
def crawler(name: str, regexp: list[str]):
    def decorator(cls):
        crawler_impls[name] = {
            "regexp": regexp,
            "cls": cls
        }
        return cls
    return decorator
