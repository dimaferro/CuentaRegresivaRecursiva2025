# main.py - Programa principal

import contador

def main():
    """
    Función principal que solicita un número al usuario y ejecuta la cuenta regresiva.
    """
    print("=== CUENTA REGRESIVA RECURSIVA 2025 ===")
    print()
    
    try:
        # Solicitar número al usuario
        numero = int(input("Ingresa un número entero positivo para la cuenta regresiva: "))
        
        # Validar que sea positivo
        if numero < 0:
            print("⚠️  Por favor, ingresa un número positivo.")
            return
        
        print(f"\n🚀 Iniciando cuenta regresiva desde {numero}...\n")
        
        # Llamar a la función recursiva
        contador.cuenta_regresiva(numero)
        
    except ValueError:
        print("❌ Error: Por favor, ingresa un número entero válido.")
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()
