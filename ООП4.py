
class Coniferous_trees:
    """ Базовый класс Хвойные деревья. """
    def __init__(self, name: str, height: float):
        """
            Создание и подготовка к работе объекта "Хвойное дерево"
            :param name: Название хвойного дерева
            :param height: Высота хвойного дерева в метрах
            Примеры:
            >>> coniferous_trees = Coniferous_trees("oak", 30)  # инициализация экземпляра класса
            >>> Хвойное дерево: oak. Высота: 30
            """
        if not isinstance(name, (str)):
            raise TypeError("Название хвойного дерева должно быть типа str ")
        self.name = name

        if not isinstance(height, (int, float)):
            raise TypeError("Высота хвойного дерева должна быть int или float")
        if height <= 0:
            raise ValueError("Высота хвойного дерева не может быть отрицательным числом или равной нулю")
        self.height = height

    def is_tree(self) -> bool:
        """
        Функция, которая проверяет есть ли хвойное дерево с таким названием
        :return: Присутствует ли хвойное дерево с таким названием
        Примеры:
        >>> coniferous_trees = Coniferous_trees("trees", 20)
        >>> coniferous_trees.is_tree()
        """
        ...

    def add_height(self, name: str, height: float) -> float:
        """
     Функция, которая увеличивает высоту в 1,5 раза
        :return: Увеличивает высоту хвойного дерева в 1,5 раза
        """
        new_tree= self.height * 1,5
        return  new_tree


    def __str__(self):
        """
        Реализация метода str - возвращаем строковое представление данных
        """
        return f"Хвойное дерево: {self.name}. Высота: {self.height}"

    def __repr__(self):
        """
        Реализация метода repr - возвращаем строковое представление данных
        """
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height})"

class Fir(Coniferous_trees):
    def __init__(self, name: str, height: float):
        super().__init__(name, height)

    def __str__(self):
        """
        Реализация метода str - возвращаем строковое представление данных
        """
        #return f"Хвойное дерево: {self.name}. Высота этого дерева: {self.height}"
        return f"{super().__str__()}"

    def __repr__(self):
        """
        Реализация метода repr - возвращаем строковое представление данных
        """
        return f"Name:{self.__class__.__name__}. Height={self.height}"

    def is_tree(self) -> bool:
        """
        Функция, которая проверяет есть ли хвойное дерево с таким названием
        :return: Присутствует ли хвойное дерево с таким названием
        Примеры:
        >>> fir = Coniferous_trees("brch", 20)
        >>> fir.is_tree()
        """
        ...

    def add_height(self) -> float:
        """
     Функция, которая добавляет хвойному дереву высоту
        :return: Увеличивает высоту хвойного дерева
        """

        new_tree= self.height + 500
        return  new_tree

if __name__ == '__main__':

    first = Coniferous_trees("Дерево", 700)
    second = Fir("Ель", 900)
    print(first)
    print(second)
    print(first.is_tree())

    print(second.is_tree())
    print(second.add_height())
