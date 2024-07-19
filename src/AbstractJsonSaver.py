from abc import ABC, abstractmethod


class AbstractJsonSaver(ABC):
    """Абстрактный класс для добавления вакансий в JSON файл"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy, id: [int]):
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, criteria):
        pass
