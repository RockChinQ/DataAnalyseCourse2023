import os

import pandas as pd

from .. import model as exporter_model


class ExcelExporter(exporter_model.AbsDataExporter):

    def export(self, data: list[exporter_model.news.News], target_file: str, **kwargs) -> None:
        
        if os.path.exists(target_file):
            os.remove(target_file)
        
        df = pd.DataFrame(columns=["新闻标题", "发布日期"])
        
        for d in data:
            dic = {
                "新闻标题": [d.title],
                "发布日期": [d.published_at.strftime("%Y-%m-%d")],
            }


            for i in range(len(d.images)):
                dic[f"图片链接{i+1}"] = [d.images[i]]
            
            df = pd.concat([df, pd.DataFrame(dic)])
        
        df.to_excel(target_file, index=False)

