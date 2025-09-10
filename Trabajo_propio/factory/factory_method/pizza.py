"""
Módulo que contiene las clases de pizza.
"""

from abc import ABC


class Pizza(ABC):
    """
    Clase base para todas las pizzas.
    """
    name: str = "Generic Pizza"
    toppings: list[str] = []

    def prepare(self):
        """
        Prepara la pizza.
        """
        print(f"Preparing {self.name}")
        print("Adding toppings:", ", ".join(self.toppings))

    def bake(self):
        """
        Hornea la pizza.
        """
        print("Bake 25 min at 350")

    def cut(self):
        """
        Corta la pizza.
        """
        print("Cutting pizza into diagonal slices")

    def box(self):
        """
        Empaqueta la pizza.
        """
        print("Place pizza in official box")

    def __str__(self):
        return self.name


class NYStyleCheesePizza(Pizza):
    """
    Clase concreta para pizza de queso estilo NY.
    """
    def __init__(self):
        self.name = "NY Style Sauce & Cheese"
        self.toppings = ["Reggiano cheese"]


class ChicagoStyleCheesePizza(Pizza):
    """
    Clase concreta para pizza de queso estilo Chicago.
    """
    def __init__(self):
        self.name = "Chicago Style Deep Dish Cheese"
        self.toppings = ["Shredded Mozzarella"]

    def cut(self):
        print("Cutting the pizza into square slices")


class NYStyleVeggiePizza(Pizza):
    """
    Clase concreta para pizza vegetariana estilo NY.
    """
    def __init__(self):
        self.name = "NY Style Veggie Cheese"
        self.toppings = ["Shredded Veggie Cheese", "Onion", "Mushroom"]


class ChicagoStyleVeggiePizza(Pizza):
    """
    Clase concreta para pizza vegetariana estilo Chicago.
    """
    def __init__(self):
        self.name = "Chicago Style Veggie Cheese"
        self.toppings = ["Shredded Veggie Cheese", "Onion", "Mushroom"]

    def cut(self):
        print("Cutting the pizza into square slices")


class NYStylePepperoniPizza(Pizza):
    """
    Clase concreta para pizza de pepperoni estilo NY.
    """
    def __init__(self):
        self.name = "NY Style Deep Dish Cheese and Pepperonni"
        self.toppings = ["Shredded Mozzarella", "SlicedPepperoni"]


class ChicagoStylePepperoniPizza(Pizza):
    """
    Clase concreta para pizza de pepperoni estilo Chicago.
    """
    def __init__(self):
        self.name = "Chicago Style Deep Dish Cheese and Pepperoni"
        self.toppings = ["Shredded Mozzarella", "SlicedPepperoni"]

    def cut(self):
        print("Cutting the pizza into square slices")
