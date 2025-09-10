"""
Código que representa tiendas de pizzas.
"""

from abc import ABC, abstractmethod
from pizza import (
    NYStyleCheesePizza,
    NYStyleVeggiePizza,
    ChicagoStyleCheesePizza,
    ChicagoStyleVeggiePizza,
    NYStylePepperoniPizza,
    ChicagoStylePepperoniPizza,
    Pizza,
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
    def create_pizza(self, kind: str) -> Pizza:
        if kind.lower() == "cheese":
            return NYStyleCheesePizza()
        if kind.lower() == "veggie":
            return NYStyleVeggiePizza()
        if kind.lower() == "pepperoni":
            return NYStylePepperoniPizza()
        raise ValueError(f"No NY pizza for kind: {kind}")


class ChicagoPizzaStore(PizzaStore):
    """
    Clase que representa una tienda de pizzas estilo Chicago.
    """
    def create_pizza(self, kind: str) -> Pizza:
        if kind.lower() == "cheese":
            return ChicagoStyleCheesePizza()
        if kind.lower() == "veggie":
            return ChicagoStyleVeggiePizza()
        if kind.lower() == "pepperoni":
            return ChicagoStylePepperoniPizza()
        raise ValueError(f"No Chicago pizza for kind: {kind}")
