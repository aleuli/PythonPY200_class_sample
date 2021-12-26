from typing import Union, Any


class Iphone:

    def __init__(self, name_model: Union[int, float], quantity_of_cameras: Union[int, float]):
        """
        Cоздание и подготовка к работе обьекта "iphone"

        :param name_model: модель iphone
        :param quantity_of_cameras: количество камер
        """
        self.name_model = name_model
        self.quantity_of_cameras = quantity_of_cameras

    def is_iphone(self) -> Any:
        """
        Функция проверяющая является ли обьект айфоном

        :return: Является аппарат айфоном или нет
        """
        if not isinstance(Iphone, classmethod):
            raise TypeError("аппарат не является айфоном , это машалах 3000")
        else:
            ...

    def is_name(self, new_name_model: Union[int, float]) -> Any:
        """
        Функция проверяющая возможно ли на индийском рынке поменять цифру на модели айфона (можно с 1-8 модель)

        :param new_name_model: Цифра модели айфона
        :return: Измененная цифра
        """
        if not isinstance(new_name_model, (int, float)):
            raise TypeError("Такой модели не существует")
        if new_name_model in range(9, 14) and new_name_model in [0]:
            raise ValueError("Увы , но нет, можно менять только на старых аппаратах")
        if new_name_model < 0:
            raise ValueError("отрицательной модели не существует")
        self.name_model = new_name_model

    def upp_quantity_of_cameras(self, new_quantity_of_cameras: Union[int, float]) -> Any:
        """
        Функция которая увеличивает количество камер, путем сборки на индийском рынке (можно до 5 камер,
        если модель айфона >= X(10))

        :param new_quantity_of_cameras: количество камер которое хотим добавить
        :return: Увеличенное количество камер у данного айфона
        """
        if not isinstance(new_quantity_of_cameras, (int, float)):
            raise TypeError("ВВедено некоректное число камер")
        if new_quantity_of_cameras < 0:
            raise ValueError("нельзя убрать камеры, можно только добавить")
        if self.quantity_of_cameras + new_quantity_of_cameras > 5:
            raise ValueError("Можно добавить до 5 камер , не больше")
        self.quantity_of_cameras += new_quantity_of_cameras

    def __str__(self):
        return f"Модель айфона {self.name_model}, количество камер {self.quantity_of_cameras}"


if __name__ == '__main__':

    iphone_6 = Iphone(6, 1)
    print(iphone_6)

    iphone_6.is_name(29)
    iphone_6.upp_quantity_of_cameras(4)
    print(iphone_6)



