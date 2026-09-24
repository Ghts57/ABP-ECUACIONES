"""
Calculadora de Interes Compuesto para un CDT
Formula utilizada (tasa efectiva anual, calculada por dias):

    P(D) = P0 * (1 + i)^(D/365)

Donde:
    P0 -> Capital inicial invertido
    i  -> Tasa de interes efectiva anual
    D  -> Numero de dias que dura la inversion
    P(D) -> Capital final (con intereses) despues de D dias
"""


def pedir_numero(mensaje):
    """Pide un numero al usuario y valida que sea valido (>= 0)."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor ingresa un valor positivo.\n")
                continue
            return valor
        except ValueError:
            print("Entrada invalida. Debes ingresar un numero.\n")


def calcular_interes_compuesto(p0, i, d):
    """
    Calcula el capital final usando la formula:
    P(D) = P0 * (1 + i)^(D/365)
    """
    return p0 * (1 + i) ** (d / 365)


def main():
    print("=" * 55)
    print("     CALCULADORA DE INTERES COMPUESTO - CDT")
    print("     Formula: P(D) = P0 * (1 + i)^(D/365)")
    print("=" * 55)

    # Solicitar datos al usuario
    p0 = pedir_numero("Ingresa el capital inicial (P0) en pesos: $")
    tasa_porcentaje = pedir_numero("Ingresa la tasa de interes efectiva anual (%): ")
    i = tasa_porcentaje / 100  # convertir de porcentaje a decimal
    d = pedir_numero("Ingresa el numero de dias de la inversion (D): ")

    # Calcular resultado
    capital_final = calcular_interes_compuesto(p0, i, d)
    interes_generado = capital_final - p0

    # Mostrar resultados
    print("\n" + "=" * 55)
    print("                    RESULTADOS")
    print("=" * 55)
    print(f"Capital inicial (P0):     ${p0:,.2f}")
    print(f"Tasa efectiva anual (i):  {tasa_porcentaje:.2f}%")
    print(f"Dias de inversion (D):    {d:.0f} dias")
    print(f"Interes generado:         ${interes_generado:,.2f}")
    print(f"Capital final P(D):       ${capital_final:,.2f}")
    print("=" * 55)


if __name__ == "__main__":
    main()
