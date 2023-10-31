import abc

from ..entities import news


class AbsDataExporter(metaclass=abc.ABCMeta):

    def export(self, data: list[news.News], **kwargs) -> None:
        pass
