# Ejercicio 4: Conversor string a int con validación

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")

    list_numeros_str = ['5', '2', '3', '', '7', 'NaN']
    lista_numeros = [int(x) if x.isdigit() else 0 for x in list_numeros_str]
    print('Lista convertida:', lista_numeros)

    list_numeros_str = ['-5', '-2', '3', '', '7', 'NaN']
    lista_numeros = [int(x) if x.lstrip('-').isdigit() else 0 for x in list_numeros_str]
    print('Lista con negativos procesados:', lista_numeros)

    print("terminamos")
