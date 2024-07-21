from abc import ABC

from src.parser import HeadHunterAPI
from src.AbstractGetApiHH import AbstractGetApiHh


def test_issubclass():
    assert issubclass(AbstractGetApiHh, ABC)
    assert issubclass(HeadHunterAPI, AbstractGetApiHh)


def test_get_vacancies():
    assert HeadHunterAPI().get_vacancies('python')


def test_all_vacancy():
    get_api = HeadHunterAPI()
    get_api.get_vacancies('python')

    assert len(get_api.vacancies) > 0










