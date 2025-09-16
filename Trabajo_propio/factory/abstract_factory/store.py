"""
Código que representa tiendas de pizzas.
"""

from abc import ABC, abstractmethod

from ingredients import (
    NYPizzaIngredientFactory,
    ChicagoPizzaIngredientFactory,
    PizzaIngredientFactory,
)
from pizza import (
    Pizza,
    CheesePizza,
    ClamPizza,
    MushroomPizza,
    VeggiesPizza,
    PepperoniPizza,
)


class PizzaStore(ABC):
    """
    Clase que representa una tienda de pizzas.
    """

    def order_pizza(self, kind: str) -> Pizza:
        """
        Procesa un pedido de pizza.
        """
        pizza = self.create_pizza(kind)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, kind: str) -> Pizza:
        """
        Crea una pizza del tipo especificado.
        """


class NYPizzaStore(PizzaStore):
    """
    Clase que representa una tienda de pizzas estilo NY.
    """

    def __init__(self):
        self.factory: PizzaIngredientFactory = NYPizzaIngredientFactory()

    def create_pizza(self, kind: str) -> Pizza:
        k = kind.lower()
        if k == "cheese":
            return CheesePizza("NY Style Cheese Pizza", self.factory)
        if k == "clam":
            return ClamPizza("NY Style Clam Pizza", self.factory)
        if k == "veggies":
            return VeggiesPizza("NY Style Veggie Pizza", self.factory)
        if k == "pepperoni":
            return PepperoniPizza("NY Style Pepperoni Pizza", self.factory)
        if k == "mushroom":
            return MushroomPizza("NY Style Mushroom Pizza", self.factory)
        raise ValueError(f"No NY pizza for kind: {kind}")


class ChicagoPizzaStore(PizzaStore):
    """
    Clase que representa una tienda de pizzas estilo Chicago.
    """

    def __init__(self):
        self.factory: PizzaIngredientFactory = ChicagoPizzaIngredientFactory()

    def create_pizza(self, kind: str) -> Pizza:
        k = kind.lower()
        if k == "cheese":
            return CheesePizza("Chicago Style Cheese Pizza", self.factory)
        if k == "clam":
            return ClamPizza("Chicago Style Clam Pizza", self.factory)
        if k == "veggies":
            return CheesePizza("Chicago Style Veggies Pizza", self.factory)
        if k == "pepperoni":
            return PepperoniPizza("Chicago Style Pepperoni Pizza", self.factory)
        if k == "mushroom":
            return MushroomPizza("Chicago Style Mushroom Pizza", self.factory)
        raise ValueError(f"No Chicago pizza for kind: {kind}")
