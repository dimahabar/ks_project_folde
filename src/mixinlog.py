class MixinLog:

    def __init__(self):
        self.code: str = ''
        self.name: str = ''

    @property
    def get_params(self):
        """
        Запрос кода города и специальности
        :return:
        """

        while True:
            self.name = input(f'''Введите название профессии. Например для поиска вакансии программиста 
            достаточно ввести название языка(python, go, Java  и т.д.) или токарь, слесарь, начальник
            финансист и т.д.\n''')
            try:
                self.name = str('name')
                break
            except ValueError:
                print("Ошибка: введите корректное число")

        return self.name