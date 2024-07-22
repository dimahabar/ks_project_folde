from abc import ABC

from src.AbstractGetApiHH import AbstractGetApiHh
from src.parser import HeadHunterAPI


def test_issubclass():
    assert issubclass(HeadHunterAPI, ABC)
    assert issubclass(HeadHunterAPI, AbstractGetApiHh)


def test_all_vacancy():
    get_api = HeadHunterAPI('python')
    get_api.get_vacancies()

    assert len(get_api.all_vacancy) > 0