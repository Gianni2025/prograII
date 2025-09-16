"""
Punto de entrada para la aplicación de la pizzería.
"""

import os
import sys

# Configurar paths para que los imports funcionen correctamente
factory_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
abstract_factory_path = os.path.join(factory_dir, "abstract_factory")
sys.path.insert(0, abstract_factory_path)

from store import NYPizzaStore, ChicagoPizzaStore


def main():
    """
    Función principal para ejecutar la aplicación.
    """
    ny = NYPizzaStore()
    chi = ChicagoPizzaStore()

    ny.order_pizza("cheese")
    print("--------")

    chi.order_pizza("cheese")
    print("--------")

    chi.order_pizza("clam")
    print("--------")

    ny.order_pizza("veggies")
    print("--------")

    chi.order_pizza("veggies")
    print("--------")

    ny.order_pizza("pepperoni")
    print("--------")

    chi.order_pizza("pepperoni")
    print("--------")

    ny.order_pizza("mushroom")
    print("--------")

    chi.order_pizza("mushroom")
    print("--------")


if __name__ == "__main__":
    main()
