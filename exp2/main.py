if __name__ == "__main__":

    import os
    import sys

    from pkg import crawler
    from pkg import entities
    
    url = sys.argv[1]

    import json

    data = crawler.do(url)

    print(json.dumps(data, default=entities.json_encoder, indent=4, ensure_ascii=False))

    target = sys.argv[2]

    from pkg.exporter.impls import excel

    excel.ExcelExporter().export(data, target)


