
import os
from abc import ABC

from src.parser import HeadHunterAPI
from src.get_json import JSONSaver
from src.utils import filter_vacancies, sort_vacancies, get_vacancies_by_salary_range, \
    get_top_vacancies
from src.vacansy import Vacansy

from config import DATA

# vacancies_file_path = os.path.join(ROOT_DIR, 'data', 'vacancies.json')


def user_interaction():
    search_query = input("Введите поисковый запрос: ").split()
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    #json_saver_inst = JSONSaver()
    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacansy.cast_to_object_list(hh_vacancies)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filtered_vacancies = filter_vacancies(vacancies_list, search_query)
    # ranged_vacancies = get_vacancies_by_salary_range(filtered_vacancies, 20000, 3000000)
    #json_saver_inst.save_filtred_vacancices(vacancies_list)  # сохраняем вакансии в формате джсон
    min_sal = input('введите минимальную зарплату : ')
    max_sal = input('введите максимальную зарплату : ')
    try:
        get_by_sal_range = get_vacancies_by_salary_range(vacancies_list, int(min_sal), int(max_sal))
    except ValueError as e:
        print(f'возникла ошибка {e}')

    sorted_vacancies = sort_vacancies(get_by_sal_range)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(filtered_vacancies) вот здесь была проблема  это печать всех вакансий
    for vacancy in top_vacancies:
        print(vacancy)
    # json_saver_inst.save_filtred_vacancices(top_vacancies)


if __name__ == "__main__":
    user_interaction()



# # Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()
#
# # Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies("Python")
#
# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#
# # Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)
#
# # Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
#
#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()