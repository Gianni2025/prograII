"""
Punto de entrada para la aplicación de la pizzería.
"""

from store import PizzaStore
from simple_factory import SimplePizzaFactory


def main():
    """
    Función principal para ejecutar la aplicación.
    """
    store = PizzaStore(SimplePizzaFactory())
    for kind in ["cheese","veggie"]:
        p = store.order_pizza(kind)
        print(f"Ordered -> {p}")


if __name__ == "__main__":
    main()
