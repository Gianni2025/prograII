"""
Testing correspondiente al módulo que implementa el patrón Simple Factory.
"""

import os
import sys

# Configurar paths para que los imports funcionen correctamente
factory_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
simple_factory_path = os.path.join(factory_dir, "simple_factory")
sys.path.insert(0, simple_factory_path)

from simple_factory import SimplePizzaFactory
from store import PizzaStore
from pizza import CheesePizza, VeggiePizza, ClamPizza, PepperoniPizza
import pytest


# ========== TESTS BÁSICOS DE SIMPLE FACTORY ==========


class TestSimplePizzaFactory:
    """Tests para verificar la creación de pizzas mediante Simple Factory"""

    @pytest.mark.parametrize(
        "pizza_type, expected_class, expected_name",
        [
            ("cheese", CheesePizza, "Cheese Pizza"),
            ("veggie", VeggiePizza, "Veggie Pizza"),
            ("clam", ClamPizza, "Clam Pizza"),
            ("pepperoni", PepperoniPizza, "Pepperoni Pizza"),
        ],
    )
    def test_factory_should_create_correct_pizza_type(
        self, pizza_type, expected_class, expected_name
    ):
        """Test que verifica que la factory cree el tipo correcto de pizza"""
        factory = SimplePizzaFactory()
        pizza = factory.create_pizza(pizza_type)

        assert isinstance(pizza, expected_class)
        assert pizza.name == expected_name

    @pytest.mark.parametrize("pizza_type", ["cheese", "CHEESE", "Cheese"])
    def test_factory_should_handle_case_insensitive_input(self, pizza_type):
        """Test que verifica que la factory maneje entradas insensibles a mayúsculas"""
        factory = SimplePizzaFactory()
        pizza = factory.create_pizza(pizza_type)

        assert isinstance(pizza, CheesePizza)

    def test_factory_should_raise_error_for_invalid_type(self):
        """Test que verifica que la factory lance error para tipos inválidos"""
        factory = SimplePizzaFactory()

        with pytest.raises(ValueError, match="Tipo inválido"):
            factory.create_pizza("invalid")


# ========== TESTS DE PIZZA STORE ==========


class TestPizzaStore:
    """Tests para verificar el funcionamiento de PizzaStore con Simple Factory"""

    def test_store_should_process_pizza_order_correctly(self):
        """Test que verifica que la tienda procese correctamente un pedido"""
        factory = SimplePizzaFactory()
        store = PizzaStore(factory)

        pizza = store.order_pizza("cheese")

        assert isinstance(pizza, CheesePizza)
        assert pizza.name == "Cheese Pizza"

    @pytest.mark.parametrize(
        "pizza_type, expected_toppings",
        [
            ("cheese", ["Reggiano cheese"]),
            ("veggie", ["Mushroom", "Onion", "Red Pepper"]),
            ("pepperoni", ["Sliced Pepperoni", "Onion", "Cheese"]),
        ],
    )
    def test_store_should_return_pizza_with_correct_toppings(
        self, pizza_type, expected_toppings
    ):
        """Test que verifica que las pizzas tengan los toppings correctos"""
        factory = SimplePizzaFactory()
        store = PizzaStore(factory)
        pizza = store.order_pizza(pizza_type)
        assert pizza.toppings == expected_toppings

def test_import_simple_factory():
    import main as s  
 #   from simple_factory import SimplePizzaFactory 
 #   from store import PizzaStore
 #   from pizza import CheesePizza, VeggiePizza, ClamPizza, PepperoniPizza
    assert callable(s.main)