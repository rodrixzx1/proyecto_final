# 01. Análisis del Problema

## 1. Nombre del problema y asignatura donde se estudió
- **Nombre del problema:** Aproximación de raíces reales de funciones polinomiales mediante el método de Newton-Raphson.
- **Asignatura original:** Análisis Numérico.

## 2. Descripción, justificación y planteamiento original
En Análisis Numérico se busca aproximar la raíz real x* de una ecuación f(x) = 0 cuando resolverla de forma algebraica directa es laborioso o requiere un método iterativo. El método de Newton-Raphson parte de una aproximación inicial x0 y actualiza mediante:
x_{k+1} = x_k - f(x_k) / f'(x_k)
hasta que el error aproximado |x_{k+1} - x_k| sea menor o igual a una tolerancia dada, o hasta alcanzar el máximo de iteraciones permitidas.

## 3. Entradas
| Nombre | Tipo de dato | Restricciones | Significado |
| :--- | :--- | :--- | :--- |
| `coeficientes` | `list[float]` | Lista no vacía; el coeficiente de mayor grado no debe ser `0` | Coeficientes de f(x) de mayor a menor grado (ej. `[1, 0, -4]` para x^2 - 4) |
| `x0` | `float` | Número real finito | Valor inicial de partida para la iteración |
| `tolerancia` | `float` | `> 0` | Criterio de paro para el error absoluto |
| `max_iter` | `int` | `>= 1` | Número máximo de iteraciones permitidas |

## 4. Procesos
- Construir f(x) y su derivada f'(x) a partir de los coeficientes del polinomio.
- Para cada iteración k desde 1 hasta `max_iter`:
  - Evaluar `fx = f(x_actual)` y `dfx = f'(x_actual)`.
  - Si `abs(dfx) < 1e-12`: detener por derivada cercana a cero (posible división entre cero o tangente horizontal).
  - Calcular `x_siguiente = x_actual - (fx / dfx)`.
  - Calcular `error = abs(x_siguiente - x_actual)`.
  - Registrar la iteración y actualizar `x_actual = x_siguiente`.
  - Si `error <= tolerancia`: marcar convergencia y detener el ciclo.

## 5. Salidas esperadas
- Raíz aproximada `raiz`, error final `error`, número de iteraciones realizadas `iteraciones` y estado (`convergio` o `no_convergio`).
- Tabla/detalle de iteraciones realizadas.
- Historial de resoluciones ejecutadas y conteo de casos convergentes.

## 6. Ejemplo original resuelto
- **Datos:** f(x) = x^2 - 4 -> `coeficientes = [1.0, 0.0, -4.0]`, `x0 = 3.0`, `tolerancia = 0.0001`, `max_iter = 20`.
  Derivada: f'(x) = 2x.
- **Procedimiento:**
  - Iteración 1: x0 = 3.0 -> f(3) = 5.0, f'(3) = 6.0 -> x1 = 3.0 - (5.0 / 6.0) = 2.166667, error = 0.833333.
  - Iteración 2: x1 = 2.166667 -> f(2.166667) = 0.694444, f'(2.166667) = 4.333333 -> x2 = 2.006410, error = 0.160256.
  - Iteración 3: x2 = 2.006410 -> f(2.006410) = 0.025682, f'(2.006410) = 4.012821 -> x3 = 2.000010, error = 0.006400.
  - Iteración 4: x3 = 2.000010 -> f(2.000010) = 0.000041, f'(2.000010) = 4.000021 -> x4 = 2.000000, error = 0.000010 <= 0.0001.
- **Resultado:** Raíz aproximada `x ≈ 2.0` en `4` iteraciones (error `0.000010`).

## 7. Alcance
- Validar coeficientes polinomiales, tolerancia y máximo de iteraciones.
- Resolver ecuaciones polinomiales f(x) = 0 con Newton-Raphson y mostrar cada iteración.
- Consultar historial de resoluciones y cantidad de aproximaciones convergentes.

## 8. Comprobación de requisitos técnicos
- Problema previo de otra asignatura (Análisis Numérico) con ejemplo resuelto: Sí.
- Entradas, procesos, salidas y reglas/validaciones: Sí.
- Al menos 2 clases (`PolinomioNumerico` y `ResolutorNewtonRaphson`): Sí.
- Menú en `main.py`, lista de registros, al menos 5 pruebas y uso de Copilot documentado: Sí.