class PolinomioNumerico:
    """Representa un polinomio f(x) de grado n y permite evaluar f(x) y f'(x)."""

    def __init__(self, coeficientes: list[float]) -> None:
        if not isinstance(coeficientes, list) or len(coeficientes) == 0:
            raise ValueError("Debe proporcionar al menos un coeficiente para el polinomio.")
        self.coeficientes: list[float] = [float(c) for c in coeficientes]
        self.validar_polinomio()

    def validar_polinomio(self) -> None:
        """Valida que el coeficiente principal no sea cero."""
        if self.coeficientes[0] == 0.0:
            raise ValueError("El coeficiente de mayor grado no puede ser 0.")

    def evaluar(self, x: float) -> float:
        """Evalúa f(x) en un punto x usando el método de Horner."""
        x_val = float(x)
        resultado = 0.0
        for coef in self.coeficientes:
            resultado = resultado * x_val + coef
        return float(resultado)

    def evaluar_derivada(self, x: float) -> float:
        """Evalúa f'(x) en un punto x."""
        x_val = float(x)
        grado = len(self.coeficientes) - 1
        if grado == 0:
            return 0.0

        derivada = 0.0
        for idx, coef in enumerate(self.coeficientes[:-1]):
            potencia = grado - idx
            derivada += (potencia * coef) * (x_val ** (potencia - 1))
        return float(derivada)

    def formato_funcion(self) -> str:
        """Devuelve una representación legible del polinomio."""
        grado = len(self.coeficientes) - 1
        partes: list[str] = []
        for idx, coef in enumerate(self.coeficientes):
            potencia = grado - idx
            if coef == 0.0 and len(self.coeficientes) > 1:
                continue
            signo = "-" if coef < 0 else "+"
            abs_coef = abs(coef)
            if potencia == 0:
                termino = f"{abs_coef}"
            elif potencia == 1:
                termino = f"{abs_coef}x"
            else:
                termino = f"{abs_coef}x^{potencia}"

            if not partes:
                partes.append(f"-{termino}" if coef < 0 else termino)
            else:
                partes.append(f"{signo} {termino}")

        return " ".join(partes) if partes else "0.0"