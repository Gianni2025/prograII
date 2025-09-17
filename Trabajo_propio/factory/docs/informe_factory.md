# Informe de Implementación - Patrones Factory

**Realizado por:**

* Gianni Bevilacqua
* Javier Spina
* Fabiana Fulgenzi
* Gerardo Toboso

## Decisiones de Diseño

### 1. Evolución desde Simple Factory hacia Abstract Factory

La implementación siguió una progresión natural de complejidad, abordando diferentes niveles de problemas de acoplamiento y extensibilidad:

#### **Simple Factory - Encapsulación Básica**
- **Problema resuelto**: Centralización de la lógica de creación de pizzas que estaba dispersa en condicionales `if/else`
- **Implementación**: Clase `SimplePizzaFactory` que encapsula la creación de objetos pizza
- **Ventajas**: Código cliente desacoplado de clases concretas, fácil mantenimiento de tipos de pizza
- **Limitaciones**: Violación del Open-Closed Principle al requerir modificación para nuevos tipos

#### **Factory Method - Delegación a Subclases**
- **Problema resuelto**: Extensión del sistema para múltiples regiones (NY vs Chicago) sin modificar código existente
- **Implementación**: Método abstracto `create_pizza()` en `PizzaStore`, implementado por `NYPizzaStore` y `ChicagoPizzaStore`
- **Cumplimiento de OCP**: Nuevas regiones se agregan extendiendo, no modificando clases base
- **Polimorfismo**: Diferentes tiendas crean diferentes estilos de la misma pizza

#### **Abstract Factory - Consistencia de Familias**
- **Problema resuelto**: Garantizar que los ingredientes regionales sean consistentes entre sí
- **Implementación**: Interfaz `PizzaIngredientFactory` con implementaciones `NYPizzaIngredientFactory` y `ChicagoPizzaIngredientFactory`
- **Garantía de consistencia**: Una pizza de NY siempre usa masa delgada, salsa marinara y almejas frescas

### 2. Extensiones Implementadas

#### **Nuevos Tipos de Pizza en Factory Method**
Se agregaron exitosamente `VeggiePizza` y `PepperoniPizza` siguiendo el patrón establecido:

```python
# Ejemplo: NYStyleVeggiePizza
class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name = "NY Style Veggie Cheese"
        self.toppings = ["Shredded Veggie Cheese", "Onion", "Mushroom"]
```

**Decisiones de diseño:**
- **Consistencia de nombres**: Siguió convención "RegionStyle + TipoPizza"
- **Diferenciación regional**: Chicago usa corte cuadrado vs diagonal de NY
- **Extensibilidad**: Fácil agregar nuevas regiones o tipos sin romper código existente

#### **Ingredientes Especializados en Abstract Factory**
Se expandió el sistema de ingredientes para soportar todos los tipos de pizza:

- **Nuevos ingredientes**: `Pepperoni`, `Mushroom`, `Onion`, `VeggieCheese`
- **Métodos de fábrica**: `create_pepperoni()`, `create_mushroom()`, `create_onion()`, `create_veggiecheese()`
- **Consistencia regional**: NY usa "Sliced Girgolas" vs Chicago "Sliced mushroom"

### 3. Manejo de Dependencias e Imports

#### **Desafío de Estructura Modular**
El proyecto presentó complejidades únicas de imports debido a:
- Múltiples módulos con archivos de mismo nombre (`pizza.py`, `store.py`)
- Imports relativos en archivos principales
- Necesidad de ejecutar desde diferentes contextos (main vs tests)

#### **Solución Implementada**
```python
# Configuración de paths para tests
factory_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, factory_dir)

# Imports absolutos para evitar conflictos
import simple_factory.simple_factory
SimplePizzaFactory = simple_factory.simple_factory.SimplePizzaFactory
```

**Ventajas de la solución:**
- **Isolation**: Cada test es independiente de la estructura de directorios
- **Clarity**: Imports explícitos evitan ambigüedades
- **Maintainability**: Fácil agregar nuevos módulos sin afectar existentes

### 4. Cumplimiento de Principios SOLID

#### **Single Responsibility Principle (SRP)**
- **Simple Factory**: `SimplePizzaFactory` se encarga únicamente de crear pizzas
- **Stores**: Cada store maneja solo pedidos de su región específica
- **Ingredient Factories**: Cada fábrica maneja solo ingredientes de su región

#### **Open-Closed Principle (OCP)**
- **Factory Method**: Nuevas regiones se agregan por extensión, no modificación
- **Abstract Factory**: Nuevos ingredientes se agregan implementando nuevos métodos en la interfaz
- **Extensiones**: Se agregaron VeggiePizza y PepperoniPizza sin modificar código base

#### **Dependency Inversion Principle (DIP)**
- **Store depende de abstracción**: `PizzaStore` depende de `Pizza` abstracta, no implementaciones concretas
- **Ingredient Factory**: Pizzas dependen de `PizzaIngredientFactory` interfaz, no implementaciones específicas

### 5. Estrategia de Testing

#### **Organización de Tests**
```
tests/
├── test_simple_factory.py      # Tests para Simple Factory
├── test_factory_method.py      # Tests para Factory Method  
└── test_abstract_factory.py    # Tests para Abstract Factory
```

#### **Cobertura de Escenarios**
- **Creación correcta**: Verificación de tipos e instancias creadas
- **Parámetros**: Manejo de entradas case-insensitive y validación de errores
- **Consistencia regional**: Ingredientes correctos por región
- **Integración**: Funcionamiento end-to-end de cada patrón

#### **Tests Parametrizados**
```python
@pytest.mark.parametrize(
    "store_class, pizza_type, expected_class, expected_style",
    [
        (NYPizzaStore, "cheese", NYStyleCheesePizza, "NY Style"),
        (ChicagoPizzaStore, "cheese", ChicagoStyleCheesePizza, "Chicago Style"),
    ],
)
def test_store_should_create_correct_pizza_style(self, store_class, pizza_type, expected_class, expected_style):
```

**Ventajas del approach:**
- **Eficiencia**: Un test cubre múltiples combinaciones
- **Mantenibilidad**: Fácil agregar nuevos casos
- **Legibilidad**: Clara separación entre datos y lógica de test

## Análisis Comparativo de Patrones

### **Simple Factory vs Factory Method**
| Aspecto | Simple Factory | Factory Method |
|---------|---------------|----------------|
| **Extensibilidad** | Requiere modificación | Extensión por herencia |
| **Acoplamiento** | Medio (cliente-factory) | Bajo (cliente-abstracción) |
| **Complejidad** | Baja | Media |
| **Casos de uso** | Tipos limitados y estables | Múltiples variantes |

### **Factory Method vs Abstract Factory**
| Aspecto | Factory Method | Abstract Factory |
|---------|---------------|------------------|
| **Producto** | Un objeto por vez | Familia de objetos |
| **Consistencia** | No garantizada | Garantizada por familia |
| **Complejidad** | Media | Alta |
| **Flexibilidad** | Alta para tipos | Alta para familias |

## Conclusiones

La implementación de los tres patrones Factory demostró exitosamente:

### **Cumplimiento de Objetivos**
- ✅ **Desacoplamiento**: Cliente independiente de clases concretas
- ✅ **Extensibilidad**: Nuevos tipos y regiones sin modificar código base
- ✅ **Consistencia**: Garantías de familias de ingredientes coherentes
- ✅ **Mantenibilidad**: Código organizado y principios SOLID respetados

### **Valor Práctico**
- **Escalabilidad**: Fácil agregar nuevas pizzerías regionales
- **Robustez**: Sistema de tests comprensivo asegura calidad
- **Claridad**: Separación clara de responsabilidades facilita comprensión
- **Flexibilidad**: Múltiples niveles de abstracción según necesidades específicas

La solución final demuestra cómo una progresión thoughtful de patrones puede resolver elegantemente problemas de complejidad creciente mientras mantiene la integridad arquitectural del sistema.
