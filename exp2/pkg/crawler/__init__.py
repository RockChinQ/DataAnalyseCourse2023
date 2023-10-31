import re

from .impls import newstjuteducn
from . import model

def do(url: str, **kwargs):

    for k, v in model.crawler_impls.items():
        for r in v["regexp"]:
            if re.match(r, url):
                return v["cls"]().do(url, **kwargs)
    
    raise Exception("No crawler found for url: " + url)
