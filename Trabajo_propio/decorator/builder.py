"""
Módulo hecho para la fácil construcción de bebidas
"""

from typing import List, Optional
from beverages import Beverage
from condiments import CondimentDecorator


class BeverageBuilder:
    """
    Clase para construir bebidas de manera flexible.
    """

    # Diccionario de bebidas disponibles
    bebidas = Beverage.__subclasses__()
    BEVERAGES = dict(zip([cls.__name__ for cls in bebidas], bebidas))

    # Diccionario de condimentos disponibles
    condimentos = CondimentDecorator.__subclasses__()
    CONDIMENTS = dict(zip([cls.__name__ for cls in condimentos], condimentos))

    SIZES = {"Tall", "Grande", "Venti"}

    def __init__(self, beverage: str, size: Optional[str]) -> None:
        if beverage not in self.BEVERAGES:
            raise ValueError(f"Esa bebida: {beverage} no existe.")
        self.beverage = self.BEVERAGES[beverage](size)
        if size:
            if size not in self.SIZES:
                raise ValueError(f"Ese tamaño: {size} no existe.")
            self.beverage.set_size(size)

    def add_condiment(self, condiment: str) -> "BeverageBuilder":
        """
        Añade un condimento a la bebida.
        """
        if condiment not in self.CONDIMENTS:
            raise ValueError(f"Condimento no reconocido: {condiment}")
        condiment_class = self.CONDIMENTS[condiment]
        self.beverage = condiment_class(self.beverage)
        return self

    def add_condiments(self, condiments: List[str]) -> None:
        """
        Añade una lista de condimentos a la bebida.
        """
        for c in condiments:
            self.add_condiment(c)

    def build(self) -> Beverage:
        """
        Devuelve la bebida construida.
        """
        return self.beverage


def build_beverage(
    base: str, size: Optional[str] = "Tall", condiments: Optional[List[str]] = []
) -> Beverage:
    """
    Construye una bebida con los parámetros dados.
    """
    builder = BeverageBuilder(base, size)
    if condiments:
        builder.add_condiments(condiments)
    return builder.build()
