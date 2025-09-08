# Trabajo Práctico: Patrones de Diseño Factory
## 🚀 Consigna del Trabajo Práctico

**Ejecución Código**

```bash
# Ejecuta la versión con Simple Factory
python -m factory.simple_factory.main

# Ejecuta la versión con Factory Method
python -m factory.factory_method.main

# Ejecuta la versión con Abstract Factory
python -m factory.abstract_factory.main
```

**Analiza la salida de cada comando.** Nota las diferencias en la preparación y los ingredientes entre las pizzas de Nueva York y Chicago en la versión final (`abstract_factory`).

python -m factory.abstract_factory.main
    Preparing NY Style Cheese Pizza
    -> Thin Crust Dough / Marinara Sauce / Reggiano Cheese
    Bake 25 min at 350
    Cutting pizza into diagonal slices
    Place pizza in official box
    Preparing Chicago Style Clam Pizza
    -> Thick Crust Dough / Plum Tomato Sauce / Mozzarella Cheese / Frozen Clams
    Bake 25 min at 350
    Cutting pizza into diagonal slices
    Place pizza in official box

### Paso 1: Extender el Patrón Factory Method

La pizzería quiere ampliar su menú. Tu primera tarea es agregar las variedades `VeggiePizza` y `PepperoniPizza` al sistema que usa **Factory Method**.

1.  **Crea las clases de producto concretas:**

    **Hecho!!!**

      * En `factory/factory_method/pizzas.py`, crea las clases `NYStyleVeggiePizza`, `NYStylePepperoniPizza`, `ChicagoStyleVeggiePizza` y `ChicagoStylePepperoniPizza`.
      * Inspírate en las clases `...CheesePizza` existentes para definir sus ingredientes (masa, salsa, toppings).

2.  **Actualiza los Concrete Creators:**

    **Hecho!!!**

      * En `factory/factory_method/stores.py`, modifica los métodos `create_pizza` de `NYPizzaStore` y `ChicagoPizzaStore` para que puedan instanciar las nuevas variedades de pizza cuando se les pasa el `kind` "veggie" o "pepperoni".

3.  **Verifica tu implementación:**
    
    **Hecho!!!**
    
      * Modifica `factory/factory_method/main.py` para ordenar las nuevas pizzas y comprueba que se crean correctamente.

### Paso 2: Extender el Patrón Abstract Factory

Ahora, harás lo mismo pero en la versión más compleja, que utiliza **Abstract Factory** para gestionar los ingredientes. El objetivo es asegurar que las nuevas pizzas también usen ingredientes consistentes con su región.

1.  **Define los nuevos productos de ingredientes:**
    
    **Hecho!!!**
      * En `factory/abstract_factory/ingredients.py`, crea las clases para los nuevos ingredientes que necesitarás, como `Veggies` y `Pepperoni` (puedes crear clases abstractas y luego concretas como `Onion`, `Mushroom`, `SlicedPepperoni`, etc.).

2.  **Actualiza la interfaz de la fábrica abstracta:**

      * En el mismo archivo, agrega nuevos métodos abstractos a `PizzaIngredientFactory` para crear los nuevos tipos de ingredientes (ej: `create_veggies()` y `create_pepperoni()`).

3.  **Actualiza las fábricas concretas:**

      * Implementa los nuevos métodos en `NYPizzaIngredientFactory` y `ChicagoPizzaIngredientFactory`, devolviendo las familias de ingredientes correctas para cada región.

**Nuevas pizzas de factory_method**
      PS C:\Users\Toshiba\Documents\prograII\Trabajo_propio> python -m factory.factory_method.main
      Preparing NY Style Veggie Cheese
      Adding toppings: Shredded Veggie Cheese, Onion, Mushroom
      Bake 25 min at 350
      Cutting pizza into diagonal slices
      Place pizza in official box
      Ana ordered: NY Style Veggie Cheese
      -----------
      Preparing Chicago Style Veggie Cheese
      Adding toppings: Shredded Veggie Cheese, Onion, Mushroom
      Bake 25 min at 350
      Cutting the pizza into square slices
      Place pizza in official box
      Juliet ordered: Chicago Style Veggie Cheese
      -----------
      Preparing Chicago Style Veggie Cheese
      Adding toppings: Shredded Veggie Cheese, Onion, Mushroom
      Bake 25 min at 350
      Cutting the pizza into square slices
      Place pizza in official box
      Caroline ordered: Chicago Style Veggie Cheese
      -----------
      Preparing Chicago Style Veggie Cheese
      Adding toppings: Shredded Veggie Cheese, Onion, Mushroom
      Bake 25 min at 350
      Cutting the pizza into square slices
      Place pizza in official box
      Michael ordered: Chicago Style Veggie Cheese
      -----------

4.  **Crea las nuevas clases de Pizza:**

      * En `factory/abstract_factory/pizzas.py`, crea las clases `VeggiePizza` y `PepperoniPizza`.
      * **Punto clave:** Su método `prepare()` debe usar la `ingredient_factory` que reciben en el constructor para obtener los ingredientes, de la misma forma que lo hacen `CheesePizza` y `ClamPizza`.

5.  **Actualiza los `PizzaStore`:**

      * Finalmente, en `factory/abstract_factory/store.py`, modifica `NYPizzaStore` y `ChicagoPizzaStore` para que puedan crear instancias de `VeggiePizza` y `PepperoniPizza`.

**Nuevas pizzas de abstract_factory**

      PS C:\Users\Toshiba\Documents\prograII\Trabajo_propio> python -m factory.abstract_factory.main
      Preparing NY Style Veggie Pizza
      -> Thin Crust Dough / Marinara Sauce / Veggie Cheese / Caramelized Sliced Onion / Sliced mushroom
      Bake 25 min at 350
      Cutting pizza into diagonal slices
      Place pizza in official box
      --------
      Preparing Chicago Style Veggies Pizza
      -> Thick Crust Dough / Plum Tomato Sauce / Mozzarella Cheese
      Bake 25 min at 350
      Cutting pizza into diagonal slices
      Place pizza in official box
      --------
      Preparing NY Style Pepperoni Pizza
      -> Thin Crust Dough / Marinara Sauce / Reggiano Cheese / Sliced Pepperoni
      Bake 25 min at 350
      Cutting pizza into diagonal slices
      Place pizza in official box
      --------
      Preparing Chicago Style Pepperoni Pizza
      -> Thick Crust Dough / Plum Tomato Sauce / Mozzarella Cheese / Sliced Pepperoni
      Bake 25 min at 350
      Cutting pizza into diagonal slices
      Place pizza in official box
      --------

### Paso 3: Pruebas Unitarias

La calidad es clave en Objectville. Debes escribir pruebas para asegurar que el sistema funciona como se espera.

1.  **Crea un archivo de pruebas:** Por ejemplo, `factory/abstract_factory/test_pizzas.py`.

2.  **Escribe entre 3 y 5 pruebas** que verifiquen los siguientes escenarios en la implementación de **Abstract Factory**:

      * Que `NYPizzaStore` efectivamente crea una pizza de tipo `NYStyle...`.
      * Que `ChicagoPizzaStore` crea una pizza de tipo `ChicagoStyle...`.
      * Que una pizza de queso de NY (`CheesePizza` creada por `NYPizzaStore`) contiene los ingredientes correctos de NY (ej: `Thin Crust Dough`).
      * Que una pizza de almejas de Chicago (`ClamPizza` creada por `ChicagoPizzaStore`) contiene los ingredientes correctos de Chicago (ej: `Frozen Clams`).

    **Pista para las pruebas:** Puedes instanciar una tienda, ordenar una pizza y luego usar `isinstance` para verificar el tipo de los ingredientes.

    ```python
    # Ejemplo de esqueleto de prueba con pytest
    from .store import NYPizzaStore
    from .ingredients import ThinCrustDough

    def test_ny_cheese_pizza_has_correct_dough():
        # Arrange
        store = NYPizzaStore()
        # Act
        pizza = store.order_pizza("cheese")
        # Assert
        assert isinstance(pizza.dough, ThinCrustDough)
    ```

-----

## 📦 Formato de Entrega

1.  Realiza un **fork** de este repositorio.
2.  Trabaja en tu fork, haciendo commits a medida que completas cada paso.
3.  En tu propio `README.md`, escribe una breve sección (`## Decisiones de Diseño`) explicando las decisiones que tomaste y cualquier desafío que encontraste.
4.  La entrega final será el enlace a tu repositorio de GitHub.

**¡Mucha suerte y a codificar\!**
