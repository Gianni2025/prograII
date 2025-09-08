
from .store import NYPizzaStore, ChicagoPizzaStore
import pytest
import sys
import os


""" 1.  **Crea un archivo de pruebas:** Por ejemplo, `factory/abstract_factory/test_pizzas.py`.

2.  **Escribe entre 3 y 5 pruebas** que verifiquen los siguientes escenarios en la implementación de **Abstract Factory**:

      * Que `NYPizzaStore` efectivamente crea una pizza de tipo `NYStyle...`.
      * Que `ChicagoPizzaStore` crea una pizza de tipo `ChicagoStyle...`.
      * Que una pizza de queso de NY (`CheesePizza` creada por `NYPizzaStore`) contiene los ingredientes correctos de NY (ej: `Thin Crust Dough`).
      * Que una pizza de almejas de Chicago (`ClamPizza` creada por `ChicagoPizzaStore`) contiene los ingredientes correctos de Chicago (ej: `Frozen Clams`).

    **Pista para las pruebas:** Puedes instanciar una tienda, ordenar una pizza y luego usar `isinstance` para verificar el tipo de los ingredientes.
Testing correspondiente al abstract factory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
"""


# ========== TESTS BÁSICOS DE STORE ==========



class TestStores:
    """Tests para verificar la creacion de los dos stores NY y Chicago

    def test_ny_cheese_pizza_has_correct_dough(self):
        pizza = NYPizzaStore().order_pizza("cheese")
        assert (pizza.dough == "Thin Crust Dough")
""" 
 #   @pytest.mark.parametrize(

  ##          "store,  nombre", [(NYPizzaStore, "cheese"), (ChicagoPizzaStore,  "Cheese")]
           
   # )
    def test_cheese_pizza_has_correct_dough_store(self):
        ny = NYPizzaStore()
        pizza = ny.order_pizza("clam"); 
        assert ("NY Style"  in str(pizza))

    def test_cheese_pizza_has_correct_dough_store(self):
        chi = ChicagoPizzaStore()
        pizza = chi.order_pizza("clam"); 
        assert ("Chicago"  in str(pizza))