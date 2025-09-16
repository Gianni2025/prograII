"""
Testing correspondiente al módulo que implementa el patrón Abstract Factory.
"""

import os
import sys

# Configurar paths para que los imports funcionen correctamente
factory_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
abstract_factory_path = os.path.join(factory_dir, "abstract_factory")
sys.path.insert(0, abstract_factory_path)

from store import NYPizzaStore, ChicagoPizzaStore
from pizza import PepperoniPizza, CheesePizza, MushroomPizza
import pytest

# ========== TESTS BÁSICOS DE STORE Y USO DIFERENCIAL INGREDIENTES ==========


class TestStoresAbstractFactory:
    """Tests para verificar la creacion de los dos stores NY y Chicago
    y el uso diferencial de masa y clams
    """

    @pytest.mark.parametrize(
        "store,  texto, dough, clams",
        [
            (NYPizzaStore, "NY Style", "Thin Crust Dough", "Fresh Clams"),
            (ChicagoPizzaStore, "Chicago Style", "Thick Crust Dough", "Frozen Clams"),
        ],
    )
    def test_clams_pizza_has_correct_clams_dough_and_store(
        self, store, texto, dough, clams
    ):
        pizza = store().order_pizza("clam")
        assert texto in str(pizza)
        assert dough in str(pizza.dough)
        assert clams in str(pizza.clam)

    @pytest.mark.parametrize(
        "store, texto, cheeses",
        [
            (NYPizzaStore, "NY Style", "Reggiano Cheese"),
            (ChicagoPizzaStore, "Chicago Style", "Mozzarella Cheese"),
        ],
    )
    def test_cheese_pizza_has_correct_cheese_and_store(self, store, texto, cheeses):
        pizza = store().order_pizza("cheese")
        assert texto in str(pizza)
        assert cheeses in str(pizza.cheese)

    @pytest.mark.parametrize(
        "store, tipo, clase",
        [
            (NYPizzaStore, "pepperoni", PepperoniPizza),
            (NYPizzaStore, "cheese", CheesePizza),
            (ChicagoPizzaStore, "mushroom", MushroomPizza),
        ],
    )
    def test_pizza_has_correct_instance(self, store, tipo, clase):
        pizza = store().order_pizza(tipo)
        assert isinstance(pizza, clase)


class TestIngredientFactories:
    """Tests para verificar que las fábricas de ingredientes funcionen correctamente"""

    @pytest.mark.parametrize(
        "store_class, expected_sauce",
        [
            (NYPizzaStore, "Marinara Sauce"),
            (ChicagoPizzaStore, "Plum Tomato Sauce"),
        ],
    )
    def test_stores_should_use_different_sauces(self, store_class, expected_sauce):
        """Test que verifica que cada tienda use diferentes salsas"""
        store = store_class()
        pizza = store.order_pizza("cheese")

        assert expected_sauce in str(pizza.sauce)

    @pytest.mark.parametrize(
        "store_class, pizza_type",
        [
            (NYPizzaStore, "cheese"),
            (ChicagoPizzaStore, "cheese"),
            (ChicagoPizzaStore, "mushroom"),
            (NYPizzaStore, "mushroom"),
        ],
    )
    def test_all_pizzas_should_have_required_ingredients(self, store_class, pizza_type):
        """Test que verifica que todas las pizzas tengan los ingredientes básicos"""
        store = store_class()
        pizza = store.order_pizza(pizza_type)

        # Todas las pizzas deben tener masa, salsa y queso
        assert hasattr(pizza, "dough") and pizza.dough is not None
        assert hasattr(pizza, "sauce") and pizza.sauce is not None
        assert hasattr(pizza, "cheese") and pizza.cheese is not None

    def test_factory_should_create_consistent_ingredients_per_store(self):
        """Test que verifica que cada tienda use consistentemente sus ingredientes"""
        ny_store = NYPizzaStore()
        chicago_store = ChicagoPizzaStore()

        ny_pizza1 = ny_store.order_pizza("cheese")
        ny_pizza2 = ny_store.order_pizza("mushroom")

        chicago_pizza1 = chicago_store.order_pizza("cheese")
        chicago_pizza2 = chicago_store.order_pizza("mushroom")

        # Las pizzas de NY deben usar los mismos tipos de ingredientes
        assert str(ny_pizza1.dough) == str(ny_pizza2.dough)
        assert str(ny_pizza1.sauce) == str(ny_pizza2.sauce)

        # Las pizzas de Chicago deben usar los mismos tipos de ingredientes
        assert str(chicago_pizza1.dough) == str(chicago_pizza2.dough)
        assert str(chicago_pizza1.sauce) == str(chicago_pizza2.sauce)

        # Pero diferentes entre tiendas
        assert str(ny_pizza1.dough) != str(chicago_pizza1.dough)
        assert str(ny_pizza1.sauce) != str(chicago_pizza1.sauce)

    def test_import_abstract_factory(self):   
        import main as af 
    #    from store import NYPizzaStore, ChicagoPizzaStore
    #    from pizza import PepperoniPizza, CheesePizza, MushroomPizza    
        import factory.abstract_factory.main as af
        assert callable(af.main)  