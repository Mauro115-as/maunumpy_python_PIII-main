# Ejercicio 5: Filtrado de listas con comprensión

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")

    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]

    # 1) IDs entre 1 y 10
    personal_1_10 = [x for x in accesos if 1 <= x <= 10]
    print('Personal del 1 al 10:', personal_1_10)
    print('Cantidad:', len(personal_1_10))

    # 2) IDs válidos
    id_validos = [3, 4, 7, 8, 15]
    personal_valido = [x for x in accesos if x in id_validos]
    print('Personal con acceso válido:', personal_valido)

    print("terminamos")
