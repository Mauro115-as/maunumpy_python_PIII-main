# Ejercicio 2: Lambda que retorna el len de strings + uso de map

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")

    # 1) Lambda que retorna len
    len_string = lambda x: len(x)
    print('Cantidad de caracteres:', len_string('jesus gonzalez'))

    # 2) Map con lambda inline
    palabras = ['love', 'casa', 'programacion']
    palabras_len = list(map(lambda x: len(x), palabras))
    print('Longitudes de palabras:', palabras_len)

    print("terminamos")
