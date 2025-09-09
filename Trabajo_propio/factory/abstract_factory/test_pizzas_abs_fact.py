
from .store import NYPizzaStore, ChicagoPizzaStore
from .ingredients import *#PizzaIngredientFactory
import pytest
from .pizza import *

# ========== TESTS BÁSICOS DE STORE Y USO DIFERENCIAL INGREDIENTES ==========

class TestStoresAbstractFactory:
    """Tests para verificar la creacion de los dos stores NY y Chicago
        y el uso diferencial de masa y clams
    """ 
    @pytest.mark.parametrize(
    "store,  texto, dough, clams", 
    [(NYPizzaStore,"NY Style", "Thin Crust Dough", "Fresh Clams"), 
     (ChicagoPizzaStore,  "Chicago Style","Thick Crust Dough", "Frozen Clams")]
     )
    def test_clams_pizza_has_correct_clams_dough_and_store(self, store, texto, dough, clams):
        pizza = store().order_pizza("clam"); 
        assert (texto  in str(pizza))
        assert (dough in str(pizza.dough))
        assert (clams in str(pizza.clam))
        
    @pytest.mark.parametrize(
    "store, texto, cheeses", 
    [(NYPizzaStore, "NY Style", "Reggiano Cheese" ), 
     (ChicagoPizzaStore,  "Chicago Style", "Mozzarella Cheese")]
     )
    def test_cheese_pizza_has_correct_cheese_and_store(self, store, texto, cheeses):
        pizza = store().order_pizza("cheese"); 
        assert (texto  in str(pizza.store))
        assert (cheeses in str(pizza.cheese))
    
    @pytest.mark.parametrize(
    "store, tipo, clase", 
    [(NYPizzaStore,"pepperoni",PepperoniPizza ), 
     (NYPizzaStore,"cheese",  CheesePizza),
     (ChicagoPizzaStore,"mushroom", MushroomPizza)]
     )
    def test_pizza_has_correct_instance(self, store,tipo, clase):
        pizza = store().order_pizza(tipo); 
        assert isinstance(pizza, clase)