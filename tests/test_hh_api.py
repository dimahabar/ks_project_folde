from abc import ABC

import pytest

from config import DATA
from src.parser import HeadHunterAPI
from src.AbstractGetApiHH import AbstractGetApiHh


def test_issubclass():
    assert issubclass(AbstractGetApiHh, ABC)
    assert issubclass(HeadHunterAPI, AbstractGetApiHh)


def test_get_vacancy_from_api():
    vacancy1 = HeadHunterAPI('tttttt')

    assert vacancy1.get_vacancies() == "Vacancy not found"







