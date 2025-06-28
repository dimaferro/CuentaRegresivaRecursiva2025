# contador.py

def es_par_o_impar(n):
    """Devuelve un string indicando si el número es par o impar."""
    if n % 2 == 0:
        return f"{n} - par"
    else:
        return f"{n} - impar"

def cuenta_regresiva(n):
    """Imprime los números desde n hasta 0, con su paridad."""
    if n < 0:
        return
    print(es_par_o_impar(n))
    if n == 0:
        print("🎉 ¡Llegamos a cero! Misión cumplida. 🚀")
        return
    cuenta_regresiva(n - 1)
