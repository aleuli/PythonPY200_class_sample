class Iphone:
    def __init__(self, name_model: int, quantity_of_cameras: int, approval_of_steve_jobs: bool):
        """
        Cоздание и подготовка к работе обьекта "iphone"

        :param name_model: модель iphone
        :param quantity_of_cameras: количество камер
        :param approval_of_steve_jobs: Одобрил ли Стив Джобс данную модель (iphone 5)
        """
        self.name_model = name_model
        self.quantity_of_cameras = quantity_of_cameras
        self.approval_of_steve_jobs = approval_of_steve_jobs

    def is_iphone(self) -> bool:
        """
        Функция проверяющая является ли обьект айфоном

        :return: Является аппарат айфоном или нет
        """
        ...

    def is_name(self, new_name_model: str) -> bool:
        """
        Функция проверяющая возможно ли на индийском рынке поменять цифру на модели айфона (можно с 1-8 модель)

        :param new_name_model: Цифра модели айфона
        :return: Измененная цифра
        """
        ...

    def upp_quantity_of_cameras(self, new_quantity_of_cameras: int) -> int:
        """
        Функция которая увеличивает количество камер, путем сборки на индийском рынке (можно до 5 камер,
        если модель айфона >= X(10))

        :param new_quantity_of_cameras: количество камер которое хотим добавить
        :return: Увеличенное количество камер у данного айфона
        """
        ...

    def death_approval_of_steve_jobs(self, new_approval_of_steve_jobs: bool) -> bool:
        """
        Функция показывающая , одобрил ли все эти изменения на индийском рынке Стив Джобс,
        p.s. если изменялись любые параметры то НЕТ.

        :param new_approval_of_steve_jobs: Спиритический сеанс со Стивом для выяснения его мнения
        :return: Мнение Стива Джобса
        """
        ...
