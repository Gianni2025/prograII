"""
Módulo que contiene las clases de pizza.
"""

from abc import ABC


class Pizza(ABC):
    """
    Clase base para todas las pizzas.
    """
    name: str = "Generic Pizza"
    dough: str = ""
    sauce: str = ""
    toppings: list[str] = []

    def prepare(self):
        """
        Prepara la pizza.
        """
        print(f"Preparing {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings:")
        for t in self.toppings:
            print("  ", t)

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


class CheesePizza(Pizza):
    """
    Clase concreta para pizza de queso.
    """
    def __init__(self):
        self.name = "Cheese Pizza"
        self.dough = "Regular"
        self.sauce = "Marinara"
        self.toppings = ["Reggiano cheese"]


class VeggiePizza(Pizza):
    """
    Clase concreta para pizza vegetariana.
    """
    def __init__(self):
        self.name = "Veggie Pizza"
        self.dough = "Thin"
        self.sauce = "Marinara"
        self.toppings = ["Mushroom", "Onion", "Red Pepper"]


class ClamPizza(Pizza):
    """
    Clase concreta para pizza de almejas.
    """
    def __init__(self):
        self.name = "Clam Pizza"
        self.dough = "Thin"
        self.sauce = "White"
        self.toppings = ["Fresh Clams", "Grated Cheese"]


class PepperoniPizza(Pizza):
    """
    Clase concreta para pizza de pepperoni.
    """
    def __init__(self):
        self.name = "Pepperoni Pizza"
        self.dough = "Regular"
        self.sauce = "Marinara"
        self.toppings = ["Sliced Pepperoni", "Onion", "Cheese"]
