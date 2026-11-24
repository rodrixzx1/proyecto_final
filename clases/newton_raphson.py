from clases.polinomio_numerico import PolinomioNumerico


class ResolutorNewtonRaphson:
    """Ejecuta el método de Newton-Raphson y almacena el historial de resoluciones."""

    def __init__(self, tolerancia: float = 1e-4, max_iter: int = 25) -> None:
        tol = float(tolerancia)
        if tol <= 0.0:
            raise ValueError("La tolerancia debe ser mayor que 0.")
        if isinstance(max_iter, bool) or not isinstance(max_iter, int) or max_iter < 1:
            raise ValueError("El máximo de iteraciones debe ser un entero mayor o igual a 1.")

        self.tolerancia = tol
        self.max_iter = max_iter
        self.historial: list[dict] = []

    def resolver(self, polinomio: PolinomioNumerico, x0: float) -> dict:
        """Aproxima una raíz de polinomio.evaluar(x) = 0 a partir de x0."""
        x_actual = float(x0)
        iteraciones_detalle: list[dict] = []
        estado = "max_iter_alcanzado"
        error_final = None
        iteraciones_realizadas = 0

        for k in range(1, self.max_iter + 1):
            fx = polinomio.evaluar(x_actual)
            dfx = polinomio.evaluar_derivada(x_actual)

            if abs(dfx) < 1e-12:
                estado = "derivada_nula"
                iteraciones_realizadas = k
                iteraciones_detalle.append(
                    {
                        "iter": k,
                        "x_k": x_actual,
                        "fx": fx,
                        "dfx": dfx,
                        "x_sig": None,
                        "error": None,
                    }
                )
                break

            x_siguiente = x_actual - (fx / dfx)
            error = abs(x_siguiente - x_actual)
            iteraciones_realizadas = k
            error_final = error

            iteraciones_detalle.append(
                {
                    "iter": k,
                    "x_k": x_actual,
                    "fx": fx,
                    "dfx": dfx,
                    "x_sig": x_siguiente,
                    "error": error,
                }
            )

            x_actual = x_siguiente
            if error <= self.tolerancia:
                estado = "convergio"
                break

        resultado = {
            "funcion": polinomio.formato_funcion(),
            "x0": float(x0),
            "raiz": round(x_actual, 8),
            "error_final": round(error_final, 8) if error_final is not None else None,
            "iteraciones": iteraciones_realizadas,
            "estado": estado,
            "detalle": iteraciones_detalle,
        }
        self.historial.append(resultado)
        return resultado

    def contar_convergentes(self) -> int:
        """Cuenta cuántas resoluciones en el historial convergieron."""
        total = 0
        for item in self.historial:
            if item["estado"] == "convergio":
                total += 1
        return total