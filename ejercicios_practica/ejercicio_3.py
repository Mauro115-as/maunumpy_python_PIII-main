# Ejercicio 3: Comprensión de listas + números aleatorios

import random

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")

    # 1) Lista del 0 al 10
    lista_0_10 = [x for x in range(11)]
    print('Lista 0 al 10:', lista_0_10)

    # 2) Tabla del 5
    tabla_5 = [x * 5 for x in range(11)]
    print('Tabla del 5:', tabla_5)

    # 3) 10 números aleatorios entre 1 y 30
    dias_mes = [random.randint(1, 30) for _ in range(10)]
    print('Días aleatorios del mes:', dias_mes)

    print("terminamos")
