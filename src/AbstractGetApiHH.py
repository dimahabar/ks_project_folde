from abc import ABC, abstractmethod


class AbstractGetApiHh(ABC):
    class API(ABC):
        """Абстрактный класс для получения API с сайта"""

        @abstractmethod
        def __repr__(self):
            pass

        @abstractmethod
        def get_vacancy_from_api(self):
            pass