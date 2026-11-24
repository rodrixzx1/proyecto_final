Especificación de Clase: PolinomioNumerico

Identificación
- **Nombre:** `PolinomioNumerico`
- **Archivo:** `clases/polinomio_numerico.py`
- **Objetivo:** Representar, validar y evaluar un polinomio f(x) y su derivada f'(x)
- **Responsabilidad:** Almacenar los coeficientes del polinomio (de mayor a menor grado), validar que sea válido y calcular f(x) y f'(x)

Atributos
`coeficientes` (`list[float]`): Coeficientes de mayor a menor grado (ej. `[1.0, 0.0, -4.0]`).

Constructor `__init__`
-Recibe `(self, coeficientes: list[float])`.
-Convierte cada elemento a `float`, llama a `validar_polinomio()` y guarda `self.coeficientes`

Metodos
- `validar_polinomio(self) -> None`: Verifica que `self.coeficientes` no esté vacío y que `self.coeficientes[0] != 0.0`; si no cumple, lanza `ValueError`
- `evaluar(self, x: float) -> float`: Evalua el f(x) usando potencia y retorna el resultado como `float`
- `evaluar_derivada(self, x: float) -> float`: Evalúa f'(x) a partir de los coeficientes y retorna el resultado como `float`
- `formato_funcion(self) -> str`: Devuelve una representación legible de f(x)

Reglas que Copilot NO puede alterar
-El coeficiente principal (`coeficientes[0]`) no puede ser `0.0`
-La derivada debe calcularse de forma consistente con el grado del polinomio