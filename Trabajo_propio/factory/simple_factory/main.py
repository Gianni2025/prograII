"""
Punto de entrada para la aplicación de la pizzería.
"""
import os
import sys

# Configurar paths para que los imports funcionen correctamente
simple_factory_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
simple_factory_path = os.path.join(simple_factory_dir, "simple_factory")
sys.path.insert(0, simple_factory_path)
from store import  PizzaStore
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
