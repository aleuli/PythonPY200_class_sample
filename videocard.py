class VideoCard:
    def __init__(self, name: str, video_memory_capacity: int, technical_process: int, turbo_frequency: int):
        self.name = name
        self.video_memory_capacity = video_memory_capacity
        self.technical_process = technical_process
        self.turbo_frequency = turbo_frequency

    def amount_of_video_memory(self, name: str) -> bool:
        """
        Функция проверяющая имя видеокарты

        :param name: Название видеокарты
        :return: Если обе видеокарты совпали по именам , то возвращаем True.
        """
        ...

    def increasing_the_amount_of_memory(self, volume_memory: int):
        """
        Функция которая добавляет заданное количество видеопамяти к основной видеопамяти,
        если запас видеопамяти позволяет это сделать.

        :param volume_memory: Обьем памяти
        :return: Увеличенный обьем памяти видеокарты
        """
        ...

    def improving_the_technical_process(self, nm: int):
        """
        Функция которая увеличивает технический процесс видеокарты путем увеличения производительности,
        если запас нанометров позволяет это сделать.

        :param nm: Нанометр
        :return: Увеличенная производительность видеокарты
        """
        ...

    def lowering_the_turbo_frequency(self, turbo_fr: int):
        """
        Функция которая уменьшает порог турбочастоты, но не менее нижней границы штатной работы.

        :param turbo_fr: Турбочастота
        :return: Уменьшенная турбочастота
        """
        ...
