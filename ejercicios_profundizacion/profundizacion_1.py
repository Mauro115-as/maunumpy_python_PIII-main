# Ejercicio de profundización: juego con suma aleatoria

import random
import numpy as np

if __name__ == '__main__':
    print('Comenzamos a divertirnos!')

    num_aleatorios = [random.randint(1, 10) for _ in range(3)]
    suma_aleatorios = np.sum(num_aleatorios)

    if suma_aleatorios <= 21:
        print('Números aleatorios:', num_aleatorios)
        print('La suma de los aleatorios es:', suma_aleatorios)
    else:
        print('Perdiste!!!!')

    print("terminamos")
