"""
Script principal para probar el patrón Decorator.
"""

from pretty_print import pretty_print
from builder import build_beverage
from tests import tests

def main():
    """
    Función principal que simula la preparación de cafés en Starbuzz.
    """
    print("Bienvenido a Starbuzz Coffee!")
    print("--- Preparando pedidos ---")

    # Pedido 1: Un Espresso simple, sin condimentos.
    espresso_simple = build_beverage("Espresso")
    print(
        f"Pedido 1: {espresso_simple.get_description()} ${espresso_simple.cost():.2f}"
    )

    # Pedido 2: Un DarkRoast con doble Mocha y Crema.
    darkroast_doble_mocha_crema = build_beverage(
        "DarkRoast", condiments=["Mocha", "Mocha", "Whip"]
    )
    print(
        f"Pedido 2: {darkroast_doble_mocha_crema.get_description()} ${darkroast_doble_mocha_crema.cost():.2f}"
    )

    # Pedido 3: Un HouseBlend con Soja, Mocha y Crema.
    houseblend_soja_mocha_crema = build_beverage(
        "HouseBlend", size="Grande", condiments=["Soy", "Mocha", "Whip"]
    )
    print(
        f"Pedido 3: {houseblend_soja_mocha_crema.get_description()} ${houseblend_soja_mocha_crema.cost():.2f}"
    )

    # Pedido 4: Un Decaf con Soja y Mocha.
    decaf_soja_mocha = build_beverage("Decaf", "Grande", ["Soy", "Mocha"])
    print(
        f"Pedido 4: {decaf_soja_mocha.get_description()}    ${decaf_soja_mocha.cost():.2f}"
    )
    print("-----------------")

    # Imprimir la descripción de cada bebida de manera legible
    print(pretty_print(espresso_simple.get_description()))
    print(pretty_print(darkroast_doble_mocha_crema.get_description()))
    print(pretty_print(houseblend_soja_mocha_crema.get_description()))
    print(pretty_print(decaf_soja_mocha.get_description()))


if __name__ == "__main__":
    main()
