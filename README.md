#Proyecto Final

Nombre y descripcion
Aplicación de consola en Python para aproximar raíces reales de funciones polinomiales f(x) = 0 mediante el método de Newton-Raphson, consultar el historial y ver resoluciones convergentes

Asignatura original
Análisis Numérico.

Objetivo
Aplicar programación orientada a objetos, estructuras de datos, validaciones y control de versiones en Git/GitHub a partir de un problema de Análisis Numerico

Funcionalidades
- Validación de coeficientes polinomiales, tolerancia y número máximo de iteraciones
- Evaluación de f(x) y f'(x) y ejecución del método de Newton-Raphson
- Consulta de historial de resoluciones y conteo de casos convergentes

Clases y estructura
- `clases/polinomio_numerico.py` (`PolinomioNumerico`): modela, valida y evalúa f(x) y f'(x)
- `clases/resolutor_newton_raphson.py` (`ResolutorNewtonRaphson`): ejecuta Newton-Raphson y mantiene `historial`
- `main.py`: menú de consola, instanciación de objetos y coordinación del flujo