# contador.py - Módulo con función recursiva de cuenta regresiva

def es_par_o_impar(numero):
    """
    Función auxiliar que determina si un número es par o impar.
    
    Args:
        numero (int): El número a evaluar
        
    Returns:
        str: "par" si el número es par, "impar" si es impar
    """
    return "par" if numero % 2 == 0 else "impar"


def cuenta_regresiva(n):
    """
    Función recursiva que realiza una cuenta regresiva desde n hasta 0,
    mostrando si cada número es par o impar.
    
    Args:
        n (int): El número desde el cual iniciar la cuenta regresiva
    """
    # Caso base: cuando llegamos a 0
    if n == 0:
        print(f"{n} - {es_par_o_impar(n)}")
        print("🎉 ¡Cuenta regresiva completada! ¡Feliz 2025! 🎊")
        return
    
    # Caso recursivo: imprimir el número actual y llamar recursivamente
    print(f"{n} - {es_par_o_impar(n)}")
    cuenta_regresiva(n - 1)
