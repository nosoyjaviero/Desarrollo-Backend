import random
contador=0
def busqueda_lineal(lista, objetivo):
    global contador
    match = False

    for elemento in lista: # O(n)
        contador+=1;
        if elemento == objetivo:            
            match = True
            break

    return match


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, tamano_de_lista) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'El numero de veces que se itero fue {contador}')