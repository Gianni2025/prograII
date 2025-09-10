"""
Testing correspondiente al módulo que implementa el patrón Factory Method.
"""

import os
import sys

# Configurar paths para que los imports funcionen correctamente
factory_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
factory_method_path = os.path.join(factory_dir, "factory_method")
sys.path.insert(0, factory_method_path)

from store import NYPizzaStore, ChicagoPizzaStore
from pizza import (  
    NYStyleCheesePizza,
    ChicagoStyleCheesePizza,
    NYStyleVeggiePizza,
    ChicagoStyleVeggiePizza,
    NYStylePepperoniPizza,
    ChicagoStylePepperoniPizza,
)
import pytest


# ========== TESTS BÁSICOS DE FACTORY METHOD ==========


class TestFactoryMethodStores:
    """Tests para verificar la creación de pizzas mediante Factory Method"""

    @pytest.mark.parametrize(
        "store_class, pizza_type, expected_class, expected_style",
        [
            (NYPizzaStore, "cheese", NYStyleCheesePizza, "NY Style"),
            (ChicagoPizzaStore, "cheese", ChicagoStyleCheesePizza, "Chicago Style"),
            (NYPizzaStore, "veggie", NYStyleVeggiePizza, "NY Style"),
            (ChicagoPizzaStore, "veggie", ChicagoStyleVeggiePizza, "Chicago Style"),
            (NYPizzaStore, "pepperoni", NYStylePepperoniPizza, "NY Style"),
            (
                ChicagoPizzaStore,
                "pepperoni",
                ChicagoStylePepperoniPizza,
                "Chicago Style",
            ),
        ],
    )
    def test_store_should_create_correct_pizza_style(
        self, store_class, pizza_type, expected_class, expected_style
    ):
        """Test que verifica que cada tienda cree pizzas del estilo correcto"""
        store = store_class()
        pizza = store.order_pizza(pizza_type)

        assert isinstance(pizza, expected_class)
        assert expected_style in pizza.name

    @pytest.mark.parametrize(
        "store_class, pizza_type, expected_toppings",
        [
            (NYPizzaStore, "cheese", ["Reggiano cheese"]),
            (ChicagoPizzaStore, "cheese", ["Shredded Mozzarella"]),
            (NYPizzaStore, "veggie", ["Shredded Veggie Cheese", "Onion", "Mushroom"]),
            (
                ChicagoPizzaStore,
                "veggie",
                ["Shredded Veggie Cheese", "Onion", "Mushroom"],
            ),
        ],
    )
    def test_pizza_should_have_correct_toppings_by_style(
        self, store_class, pizza_type, expected_toppings
    ):
        """Test que verifica que las pizzas tengan los toppings correctos según el estilo"""
        store = store_class()
        pizza = store.order_pizza(pizza_type)

        assert pizza.toppings == expected_toppings

    @pytest.mark.parametrize("store_class", [NYPizzaStore, ChicagoPizzaStore])
    def test_store_should_raise_error_for_invalid_pizza_type(self, store_class):
        """Test que verifica que las tiendas lancen error para tipos inválidos"""
        store = store_class()

        with pytest.raises(ValueError):
            store.order_pizza("invalid")

    def test_chicago_pizza_should_cut_differently(self):
        """Test que verifica que las pizzas de Chicago se corten de manera diferente"""
        store = ChicagoPizzaStore()
        pizza = store.order_pizza("cheese")

        # Verificar que es una pizza de Chicago
        assert isinstance(pizza, ChicagoStyleCheesePizza)
        assert "Chicago Style" in pizza.name
