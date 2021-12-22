class RussianDemocracy:
    def __init__(self, police_officers: int, official: int, rocket: int, income_of_citizens: int):
        """
        Создание и подготовка к работе объекта "Русская демократия"

        :param police_officers: количество полицейских
        :param official: количество чиновников
        :param rocket: ракеты
        :param income_of_citizens: доходы граждан
        """
        self.police_officers = police_officers
        self.official = official
        self.rocket = rocket
        self.income_of_citizens = income_of_citizens

    def is_RussianDemocracy(self) -> bool:
        """
        Функция проверяющая действительно мы работаем с русской демократией

        :return: Является это обьектом русской демократии или нет
        """
        ...

    def add_police_officers(self, new_police_officers: int) -> int:
        """
        Функция позволяющая увеличить количество штатных полицейских (не ограничено)

        :param new_police_officers: Количество полицейских
        :return: Новое(увеличенное) количество полицейских
        """
        ...

    def add_official(self, new_official: int) -> int:
        """
        Функция позволяющая увеличить количество чиновников (не ограничено)

        :param new_official: количество чиновников
        :return: Новое(увеличенное) количество чиновников
        """
        ...

    def add_rocket(self, new_rocket: int) -> int:
        """
        Функция увеличивающая количество ракет

        :param new_rocket: количество ракет
        :return: Новое(увеличенное) количество ракет
        """
        ...

    def minus_income_of_citizens(self, new_income_of_citizens: int) -> int:
        """
        Функция проверяющая: если количество полицейских , чиновников и ракет увеличилось то доходы падают на 20%,
        если количество уменьшилось , то увеличить доходы на 0.5 %.

        :param new_income_of_citizens:
        :return:
        """
        ...
