"""
Código de la fábrica simple para crear pizzas.
"""

from pizza import Pizza, CheesePizza, VeggiePizza, ClamPizza, PepperoniPizza


class SimplePizzaFactory:
    """
    Clase de fábrica simple para crear pizzas.
    """
    def create_pizza(self, kind: str) -> Pizza:
        """
        Crea una pizza del tipo especificado.
        """
        k = kind.lower()
        if k == "cheese":
            return CheesePizza()
        if k == "veggie":
            return VeggiePizza()
        if k == "clam":
            return ClamPizza()
        if k == "pepperoni":
            return PepperoniPizza()
        raise ValueError(f"Tipo inválido: {kind}")
