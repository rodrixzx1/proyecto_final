from clases.polinomio_numerico import PolinomioNumerico
from clases.resolutor_newton_raphson import ResolutorNewtonRaphson


def mostrar_menu() -> None:
    print("\n=== MÉTODO DE NEWTON-RAPHSON (ANÁLISIS NUMÉRICO) ===")
    print("1. Resolver ecuación polinomial f(x) = 0")
    print("2. Ver historial de resoluciones")
    print("3. Ver cantidad de resoluciones convergentes")
    print("4. Salir")


def leer_flotante(mensaje: str) -> float:
    while True:
        texto = input(mensaje).strip()
        try:
            return float(texto)
        except ValueError:
            print("Entrada inválida. Ingresa un número real (ej. 3.0, -1.5).")


def leer_coeficientes() -> list[float]:
    while True:
        texto = input(
            "Ingresa coeficientes de mayor a menor grado separados por coma (ej. 1, 0, -4): "
        ).strip()
        partes = [p.strip() for p in texto.split(",") if p.strip() != ""]
        if not partes:
            print("Debes ingresar al menos un coeficiente.")
            continue
        try:
            return [float(p) for p in partes]
        except ValueError:
            print("Coeficiente inválido. Asegúrate de separar números reales con comas.")


def opcion_resolver(resolutor: ResolutorNewtonRaphson) -> None:
    coeficientes = leer_coeficientes()
    x0 = leer_flotante("Ingresa el valor inicial x0: ")

    try:
        polinomio = PolinomioNumerico(coeficientes)
        resultado = resolutor.resolver(polinomio, x0)

        print("\n--- Resultado de Newton-Raphson ---")
        print(f"Función f(x):     {resultado['funcion']}")
        print(f"Valor inicial x0: {resultado['x0']}")
        print(f"Estado:           {resultado['estado']}")
        print(f"Raíz aproximada:  {resultado['raiz']}")
        print(f"Error final:      {resultado['error_final']}")
        print(f"Iteraciones:      {resultado['iteraciones']}")
    except ValueError as error:
        print(f"Error de validación: {error}")


def opcion_historial(resolutor: ResolutorNewtonRaphson) -> None:
    if not resolutor.historial:
        print("\nAún no hay resoluciones registradas.")
        return

    print("\n--- Historial de resoluciones ---")
    for indice, item in enumerate(resolutor.historial, start=1):
        print(
            f"{indice}. f(x) = {item['funcion']} | x0={item['x0']} | "
            f"Raíz={item['raiz']} | Iter={item['iteraciones']} | Estado={item['estado']}"
        )


def main() -> None:
    resolutor = ResolutorNewtonRaphson(tolerancia=1e-4, max_iter=25)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            opcion_resolver(resolutor)
        elif opcion == "2":
            opcion_historial(resolutor)
        elif opcion == "3":
            convergentes = resolutor.contar_convergentes()
            print(f"\nResoluciones convergentes: {convergentes}")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Selecciona un número del 1 al 4.")


if __name__ == "__main__":
    main()