import datetime

class News:

    title: str

    published_at: datetime

    images: list[str]

    def __init__(self, title: str, published_at: datetime, images: list[str]) -> None:
        self.title = title
        self.published_at = published_at
        self.images = images

    def __repr__(self) -> str:
        return f"News(title={self.title}, published_at={self.published_at}, images={self.images})"
