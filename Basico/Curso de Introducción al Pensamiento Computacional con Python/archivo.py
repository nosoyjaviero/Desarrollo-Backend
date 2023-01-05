
# #7
# print(f'{"Hip "*3} Hurra')

# #recibir nombre del usuario y decir cual es la longitud de la cadena
# Saludo= "Digite su nombre "
# nombre= input(Saludo)
# print(f'La longitud de la cadena es {len(nombre)+len(Saludo)}')

#10


# frutas = ['manzana', 'pera', 'mango']
# print(type(frutas))
# iterador = iter(frutas)
# next(iterador)
# manzana
#  next(iterador)
# pera
# >>> next(iterador)
# mango

estudiantes = {
    #keys,values y ambos juntos seria items
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}



for pais in estudiantes:
    print(pais)

for pais in estudiantes.keys():
    print(estudiantes.keys());
    # dict_keys(['mexico', 'colombia', 'puerto_rico'])

    print(pais);
    # mexico
    # colombia
    # puerto_rico

for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)
        # 10
        # 15
        # 4

for pais, numero_de_estudiantes in estudiantes.items():
    print(estudiantes.items());
    # dict_items([('mexico', 10), ('colombia', 15), ('puerto_rico', 4)])
    #   dict_items([('mexico', 10), ('colombia', 15), ('puerto_rico', 4)])
    #   dict_items([('mexico', 10), ('colombia', 15), ('puerto_rico', 4)])