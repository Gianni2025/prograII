# Informe de Implementación - Patrón Decorator

**Realizado por:**

* Gianni Bevilacqua
* Javier Spina
* Fabiana Fulgenzi
* Gerardo Toboso

## Decisiones de Diseño

### 1. Propagación de Tamaños

La implementación del sistema de tamaños siguió el principio de **no duplicar estado**, asegurando que la información del tamaño se mantenga centralizada en la bebida base:

- **En la clase `Beverage`**: Se agregaron los métodos `set_size()`, `get_size()` y `get_available_sizes()` con validación de tamaños válidos (`["Tall", "Grande", "Venti"]`).

- **En `CondimentDecorator`**: Los decoradores obtienen el tamaño de la bebida envuelta mediante `self.size = beverage.get_size()` en el constructor, manteniendo una referencia al tamaño actual sin duplicar la lógica de validación.

- **Propagación de cambios**: Cuando se modifica el tamaño de una bebida decorada, el cambio se propaga automáticamente a través de la cadena de decoradores, ya que todos consultan la misma fuente (la bebida base).

### 2. Precios Dependientes del Tamaño

Se implementó un sistema de precios variables para el condimento **Soy**, donde el costo depende del tamaño de la bebida:

```python
# En la clase Soy
def cost(self) -> float:
    costo = [0.10, 0.15, 0.20]  # Tall, Grande, Venti
    if self.size == "Tall":
        return self._beverage.cost() + costo[0]
    elif self.size == "Grande":
        return self._beverage.cost() + costo[1]
    else:
        return self._beverage.cost() + costo[2]
```

Esta implementación:

- Consulta el tamaño de la bebida envuelta
- Aplica el precio correspondiente sin modificar la lógica de otras clases
- Respeta el principio Open-Closed (OCP)

### 3. Sistema Builder para Usabilidad

Se implementó un patrón Builder (`BeverageBuilder`) para simplificar la construcción de bebidas complejas:

- **Uso de reflexión**: Se utilizan `__subclasses__()` para obtener dinámicamente las clases disponibles de bebidas y condimentos
- **Interfaz fluida**: Método `add_condiment()` que retorna `self` para permitir encadenamiento
- **Función de conveniencia**: `build_beverage(base, size, condiments)` que encapsula la lógica de construcción

### 4. Pretty Print para Presentación

Se desarrolló una función `pretty_print()` que mejora la legibilidad de las descripciones:

- **Detección de repeticiones**: Identifica condimentos duplicados en la descripción
- **Formateo inteligente**: Convierte "Mocha, Mocha" en "Double Mocha" y "Mocha, Mocha, Mocha" en "Triple Mocha"
- **Escalabilidad**: Para más de 3 repeticiones utiliza formato "nx Condimento"
- **No invasiva**: Opera solo a nivel de presentación sin afectar la lógica de cálculo de costos

## Estrategia de Testing

### Organización de Tests

Los tests se organizaron en 3 archivos especializados:

1. **`test_beverages.py`**: Tests para funcionalidad básica de bebidas y tamaños
2. **`test_condiments.py`**: Tests para decoradores y combinaciones complejas
3. **`test_pretty_print.py`**: Tests para funcionalidad de formateo

### Cobertura de Casos

- **Tests parametrizados**: Se utilizó `@pytest.mark.parametrize` para probar múltiples combinaciones eficientemente
- **Casos edge**: Tests para decoradores anidados profundamente y propagación de propiedades
- **Integridad del patrón**: Verificación de que las bebidas decoradas mantienen la interfaz `Beverage`
- **Validación de costos**: Tests específicos para asegurar que los cálculos de precios son correctos

### Validación de Totales

Los tests incluyen verificaciones exhaustivas de cálculos:

```python
def test_complex_combination_should_calculate_correctly_when_multiple_condiments_applied(self):
    house_blend = HouseBlend(size="Tall")
    complex_drink = Whip(Mocha(Soy(house_blend)))
    
    expected_cost = 0.89 + 0.10 + 0.20 + 0.10  # 1.29
    assert complex_drink.cost() == expected_cost
```

## Cumplimiento de Principios

### Open-Closed Principle (OCP)

- **Extensión sin modificación**: Se agregó el condimento `Caramel` sin modificar clases existentes
- **Nuevas funcionalidades**: Builder y Pretty Print se implementaron como módulos separados
- **Precios por tamaño**: Solo se modificó la clase `Soy` para implementar precios variables

### Composición sobre Herencia

- **Delegación efectiva**: Cada decorador delega el trabajo principal a la bebida envuelta
- **Flexibilidad en runtime**: Las combinaciones se construyen dinámicamente sin explosión de clases
- **Mantenimiento del tipo**: Los decoradores mantienen la interfaz `Beverage` por herencia

## Conclusiones

La implementación logró cumplir con todos los requisitos del patrón Decorator manteniendo:

- **Flexibilidad**: Fácil adición de nuevos condimentos y bebidas
- **Usabilidad**: Builder pattern simplifica la construcción de bebidas complejas
- **Presentación**: Pretty print mejora la experiencia del usuario
- **Robustez**: Suite de tests comprehensiva asegura correctitud funcional
- **Escalabilidad**: Arquitectura preparada para futuras extensiones sin romper código existente

La solución demuestra un diseño sólido que balancea correctamente los principios SOLID con la practicidad de uso.