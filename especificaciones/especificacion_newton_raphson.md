Especificación de Clase: ResolutorNewtonRaphson

Identificación
- **Nombre:** `ResolutorNewtonRaphson`
- **Archivo:** `clases/resolutor_newton_raphson.py`
- **Objetivo:** Aplicar el método de Newton-Raphson a un `PolinomioNumerico` y guardar el historial de resultados
- **Responsabilidad:** Ejecutar las iteraciones de Newton-Raphson, aplicar criterios de paro y mantener la lista `historial`

Atributos
- `tolerancia` (`float`): Error absoluto máximo permitido (`> 0`). Por defecto: `1e-4`
- `max_iter` (`int`): Máximo de iteraciones (`>= 1`). Por defecto: `25`
- `historial` (`list[dict]`): Lista inicializada vacía `[]` con cada resolución ejecutada

Constructor `__init__`
- Recibe `(self, tolerancia: float = 1e-4, max_iter: int = 25)`
- Valida `tolerancia > 0` y `max_iter >= 1` (lanza `ValueError` si no cumple) e inicializa atributos

Métodos
- `resolver(self, polinomio: PolinomioNumerico, x0: float) -> dict`:
  - Itera hasta `self.max_iter` usando `x_{k+1} = x_k - f(x_k) / f'(x_k)`
  - Si `abs(dfx) < 1e-12`, detiene con estado `"derivada_nula"`
  - Si `abs(x_sig - x_act) <= self.tolerancia`, detiene con estado `"convergio"`
  - Si se agotan las iteraciones sin cumplir tolerancia, estado `"max_iter_alcanzado"`
  - Guarda el diccionario en `self.historial` y lo retorna.
- `contar_convergentes(self) -> int`: Cuenta cuántos registros en `self.historial` tienen `estado == "convergio"`

Reglas que Copilot NO puede alterar
- La fórmula de actualización debe ser `x_siguiente = x_actual - (fx / dfx)`
- Cada ejecución debe agregarse a `self.historial`