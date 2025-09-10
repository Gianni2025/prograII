"""
Módulo que contiene las clases de ingredientes para las pizzas.
"""

from abc import ABC, abstractmethod


class Dough:
    """
    Clase que representa la masa de la pizza.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Sauce:
    """
    Clase que representa la salsa de la pizza.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Cheese:
    """
    Clase que representa el queso de la pizza.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class VeggieCheese:
    """
    Clase que representa el queso vegetariano de la pizza.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Clams:
    """
    Clase que representa las almejas de la pizza.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Onion:
    """
    Clase que representa la cebolla de la pizza.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Mushroom:
    """
    Clase que representa el champiñón de la pizza.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Pepperoni:
    """
    Clase que representa el pepperoni de la pizza.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class PizzaIngredientFactory(ABC):
    """
    Interfaz para la creación de ingredientes de pizza.
    """

    @abstractmethod
    def create_dough(self) -> Dough:
        """
        Añade la masa de la pizza.
        """

    @abstractmethod
    def create_sauce(self) -> Sauce:
        """
        Añade la salsa de la pizza.
        """

    @abstractmethod
    def create_cheese(self) -> Cheese:
        """
        Añade el queso de la pizza.
        """

    @abstractmethod
    def create_veggiecheese(self) -> VeggieCheese:
        """
        Añade el queso vegetariano de la pizza.
        """

    @abstractmethod
    def create_clam(self) -> Clams:
        """
        Añade las almejas de la pizza.
        """

    @abstractmethod
    def create_onion(self) -> Onion:
        """
        Añade la cebolla de la pizza.
        """

    @abstractmethod
    def create_mushroom(self) -> Mushroom:
        """
        Añade el champiñón de la pizza.
        """

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        """
        Añade el pepperoni de la pizza.
        """


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    """
    Clase concreta para la creación de ingredientes de pizza estilo NY.
    """

    def create_dough(self) -> Dough:
        return Dough("Thin Crust Dough")

    def create_sauce(self) -> Sauce:
        return Sauce("Marinara Sauce")

    def create_cheese(self) -> Cheese:
        return Cheese("Reggiano Cheese")

    def create_onion(self) -> Onion:
        return Onion("Caramelized Sliced Onion")

    def create_veggiecheese(self) -> VeggieCheese:
        return VeggieCheese("Veggie Cheese")

    def create_clam(self) -> Clams:
        return Clams("Fresh Clams")

    def create_mushroom(self) -> Mushroom:
        return Mushroom("Sliced Girgolas")

    def create_pepperoni(self) -> Pepperoni:
        return Pepperoni("Sliced Pepperoni")


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    """
    Clase concreta para la creación de ingredientes de pizza estilo Chicago.
    """

    def create_dough(self) -> Dough:
        return Dough("Thick Crust Dough")

    def create_sauce(self) -> Sauce:
        return Sauce("Plum Tomato Sauce")

    def create_cheese(self) -> Cheese:
        return Cheese("Mozzarella Cheese")

    def create_onion(self) -> Onion:
        return Onion("Red Caramelized Sliced Onion")

    def create_veggiecheese(self) -> VeggieCheese:
        return VeggieCheese("Veggie Cheese")

    def create_clam(self) -> Clams:
        return Clams("Frozen Clams")

    def create_mushroom(self) -> Mushroom:
        return Mushroom("Sliced mushroom")

    def create_pepperoni(self) -> Pepperoni:
        return Pepperoni("Sliced Pepperoni")
