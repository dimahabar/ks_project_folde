import requests
import json
from config import DATA
from src.AbstractGetApiHH import AbstractGetApiHh
from src.mixinlog import MixinLog


class HeadHunterAPI(AbstractGetApiHh, MixinLog):

    def __init__(self, name):
        super().__init__()
        self.name_vacancy: str = name
        self.url = 'https://api.hh.ru/vacancies'
        self.all_vacancy: list = []


    def get_vacancies(self):  # json словарь
        """
        Получаем информацию по вакансиям с сайта НН.ру
        :return:
        """
        param_response = {'text': f'NAME:{self.name_vacancy}',
                          "only_with_salary": "true", 'per_page': 100}
        response = requests.get(f"{self.url}", param_response)
        try:
            response.status_code == 200
        except ConnectionError:
            print("Вакансии не найдены\nПопробуйте выбрать другою специальность")
            return "Vacancy found"
        else:
            self.all_vacancy = json.loads(response.text)['items']
        if len(self.all_vacancy) == 0:
            print("Вакансии не найдены\nПопробуйте выбрать другою специальность")
            return "Vacancy not found"
        else:
            with open(DATA, 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.all_vacancy, ensure_ascii=False))
                print(f"Найдено вакансий: {len(self.all_vacancy)} ")


        return self.all_vacancy

