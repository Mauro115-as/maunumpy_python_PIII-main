if __name__ == '__main__':
    print('Comenzamos a ponernos serios!')

    padron = ['A', 'E', 'J', 'T']

    nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel',
               'Alejandro', 'Leonel', 'Antonio', 'Omar', 'Antonia', 'Amalia',
               'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']

    # Filtrar nombres que empiezan con letras en el padrón
    nombres_filtrados = [nombre for nombre in nombres if nombre[0] in padron]

    print('Nombres Filtrados:', nombres_filtrados)
    print("Terminamos")
