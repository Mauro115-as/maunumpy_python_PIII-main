# Ejercicio 1: Lambda que eleva al cuadrado + uso de map

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")

    # 1) Lambda que eleva al cuadrado
    potencia_2 = lambda x: x**2
    pot_3 = potencia_2(3)
    print('El número 3 elevado al cuadrado es:', pot_3)

    # 2) Map con lambda inline
    numeros = [1, -5, 4, 3]
    numeros_potencia = list(map(lambda x: x**2, numeros))
    print('Lista con potencias de 2:', numeros_potencia)

    print("terminamos")
