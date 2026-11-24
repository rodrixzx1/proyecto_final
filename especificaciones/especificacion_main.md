Especificación del Programa Principal: main.py

Menú de opciones
1. Resolver ecuación polinomial f(x) = 0 con Newton-Raphson
2. Ver historial de resoluciones
3. Ver cantidad de resoluciones convergentes
4. Salir

Objetos a crear y métodos a llamar
- Crear `ResolutorNewtonRaphson(tolerancia=1e-4, max_iter=25)` al iniciarr
- En la opción 1: solicitar coeficientes separados por coma y valor inicial `x0` instanciar `PolinomioNumerico(coeficientes)` y llamar a `resolutor.resolver(polinomio, x0)`
- En la opción 2: recorrer `resolutor.historial` e imprimir los resutados
- En la opción 3: llamar a `resolutor.contar_convergentes()` y mostrar el total

Secuencia de operaciones y condiciones de salida
- Ciclo `while` hasta elegir la opción `4`
- Capturar `ValueError` ante datos inválidos sin interrumpir el menú