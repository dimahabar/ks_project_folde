from src.vacansy import Vacansy

def test___str__():
    vacancy = Vacansy("Python Developer", "open", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...", "104131675", "1")
    assert vacancy.__str__() == ('Название вакансии: Python Developer \n'
                                 'Заработная плата: 100 000-150 000 руб. \n'
                                 'Описание: Требования: опыт работы от 3 лет... \n'
                                 'Ссылка: open \n'
                                 'ID: 1 \n')

def test_validate__str():
    vacancy = Vacansy("Python Developer", "open", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...", "104131675", "1")
    assert vacancy.validate__str(value=0) == 'Информация не была найдена'

