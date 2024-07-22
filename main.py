
import os
from abc import ABC

from src.parser import HeadHunterAPI
from src.get_json import JSONSaver
from src.utils import filter_vacancies, sort_vacancies, get_vacancies_by_salary_range, get_top_vacancies
from src.vacansy import Vacansy






def user_interaction():
    search_query = input("Введите поисковый запрос: ").split()
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI(search_query)
    # json_saver_inst = JSONSaver()
    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies()
    vacancies_list = Vacansy.cast_to_object_list(hh_vacancies)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filtered_vacancies = filter_vacancies(vacancies_list, search_query)

    min_sal = input('введите минимальную зарплату : ')
    max_sal = input('введите максимальную зарплату : ')
    try:
        get_by_sal_range = get_vacancies_by_salary_range(vacancies_list, int(min_sal), int(max_sal))
    except ValueError as e:
        print(f'возникла ошибка {e}')

    sorted_vacancies = sort_vacancies(get_by_sal_range)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    for vacancy in top_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()
