import json

import pytest
from src.AbstractGetApiHH import AbstractGetApiHh
from config import DATA_TEST
from src.parser import HeadHunterAPI
from src.get_json import JSONSaver


@pytest.fixture
def fixture_class_get_hh_valid():
    return HeadHunterAPI('python').get_vacancies()


@pytest.fixture
def fixture_class_get_hh_negative():
    return HeadHunterAPI("1").get_vacancies()


@pytest.fixture
def fixture_class_json_saver():
    return JSONSaver()

@pytest.fixture
def fixture_class_list():
    json_saver = JSONSaver()
    json_saver.save_file([{'name': 'Kris'}])
    return json_saver


@pytest.fixture
def new_file():
    with open(DATA_TEST, encoding='utf-8') as file:
        return json.load(file)