from . import news


def json_encoder(obj) -> dict:
    if isinstance(obj, news.News):
        return {
            "title": obj.title,
            "published_at": obj.published_at.strftime("%Y-%m-%d"),
            "images": obj.images
        }
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
