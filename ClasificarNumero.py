def main():
    while True:
        print("Menú de opciones:")
        print("1. Determinar si el número es par o impar")
        print("2. Determinar si es positivo, negativo o cero")
        print("3. Verificar si es múltiplo de 5")
        print("4. Verificar si es divisible entre 3 y 4 al mismo tiempo")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))

        if 1 <= opcion <= 4:
            numero = int(input("Ingrese un número: "))
        else:
            numero = 0

        if opcion == 1:
            if numero % 2 == 0:
                print("El número es par.")
            else:
                print("El número es impar.")
        elif opcion == 2:
            if numero > 0:
                print("El número es positivo.")
            elif numero < 0:
                print("El número es negativo.")
            else:
                print("El número es cero.")
        elif opcion == 3:
            if numero % 5 == 0:
                print("El número es múltiplo de 5.")
            else:
                print("El número no es múltiplo de 5.")
        elif opcion == 4:
            if numero % 3 == 0 and numero % 4 == 0:
                print("El número es divisible entre 3 y 4 al mismo tiempo.")
            else:
                print("El número NO es divisible entre 3 y 4 al mismo tiempo.")
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
        print()

if __name__ == "__main__":
    main()
