from abc import ABC, abstractmethod


class AbstractGetApiHh(ABC):
    class API(ABC):
        """Абстрактный класс для получения API с сайта"""

        @abstractmethod
        def get_vacancies(self, query):

            pass