"""
Punto de entrada para la aplicación de la pizzería.
"""
import os
import sys

# Configurar paths para que los imports funcionen correctamente
factory_method_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
factory_method_path = os.path.join(factory_method_dir, "factory_method")
sys.path.insert(0, factory_method_path)
from store import NYPizzaStore, ChicagoPizzaStore


def main():
    """
    Función principal para ejecutar la aplicación.
    """
    ny = NYPizzaStore()
    chi = ChicagoPizzaStore()
    p1 = ny.order_pizza("cheese")
    print("Ethan ordered:", p1)
    print("-----------")
    p2 = chi.order_pizza("cheese")
    print("Joel ordered:", p2)
    print("-----------")
    p3 = ny.order_pizza("veggie")
    print("Ana ordered:", p3)
    print("-----------")
    p4 = chi.order_pizza("veggie")
    print("Juliet ordered:", p4)
    print("-----------")
    p5 = ny.order_pizza("pepperoni")
    print("Caroline ordered:", p5)
    print("-----------")
    p6 = chi.order_pizza("pepperoni")
    print("Michael ordered:", p6)
    print("-----------")


if __name__ == "__main__":
    main()
