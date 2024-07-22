from src.utils import read_json, vacancies_file_path, save_to_json

def test_read_json():
    assert read_json(file_path=vacancies_file_path)

def test_save_to_json():
    assert save_to_json(filtred_vacancies='pyton', file_path=vacancies_file_path) == None