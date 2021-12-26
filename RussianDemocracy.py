from typing import Union


class RussianDemocracy:
    def __init__(self, police_officers: int, official: int, rocket: int):
        """
        Создание и подготовка к работе объекта "Русская демократия"

        :param police_officers: количество полицейских
        :param official: количество чиновников
        :param rocket: ракеты
        """
        self.police_officers = police_officers
        self.official = official
        self.rocket = rocket

    def is_russianemocracy(self) -> bool:
        """
        Функция проверяющая действительно мы работаем с русской демократией

        :return: Является это обьектом русской демократии или нет
        """
        ...

    def add_police_officers(self, new_police_officers: Union[int, float]) -> None:
        """
        Функция позволяющая увеличить количество штатных полицейских (не ограничено)

        :param new_police_officers: Количество полицейских
        :return: Новое(увеличенное) количество полицейских
        """
        if not isinstance(new_police_officers, (int, float)):
            raise TypeError
        if new_police_officers < 0:
            raise ValueError
        self.police_officers += new_police_officers

    def add_official(self, new_official: Union[int, float]) -> None:
        """
        Функция позволяющая увеличить количество чиновников (не ограничено)

        :param new_official: количество чиновников
        :return: Новое(увеличенное) количество чиновников
        """
        if not isinstance(new_official, (int, float)):
            raise TypeError
        if new_official < 0:
            raise ValueError
        self.official += new_official

    def add_rocket(self, new_rocket: Union[int, float]) -> None:
        """
        Функция увеличивающая количество ракет

        :param new_rocket: количество ракет
        :return: Новое(увеличенное) количество ракет
        """
        if not isinstance(new_rocket, (int, float)):
            raise TypeError
        if new_rocket < 0:
            raise ValueError
        self.rocket += new_rocket

    def __str__(self) -> str:
        return f"В России число полицейских составляет {self.police_officers}, чиновников {self.official}, " \
               f"ракет {self.rocket}"


if __name__ == '__main__':

    rd = RussianDemocracy(100, 20, 10)
    print(rd)

    rd.add_rocket(100)
    print(rd)

    rd.add_police_officers(50)
    rd.add_official(500)
    print(rd)
