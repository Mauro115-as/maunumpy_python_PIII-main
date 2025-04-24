if __name__ == '__main__':
    print("Acercamiento al uso de datos relacionales")

    producto = {
        556070: 'Auto',
        704060: 'Moto',
        42135: 'Celular',
        1264: 'Bicicleta',
        905045: 'Computadora',
    }

    lista_compra_id = [556070, 905045, 42135, 5674, 704060, 1264, 42135, 3654]

    # Traducir los IDs a nombres de productos, usar 'NaN' para IDs desconocidos
    lista_compra_productos = [producto.get(id_, 'NaN') for id_ in lista_compra_id]

    print('Lista de productos:', lista_compra_productos)
    print("Terminamos")
