import random
import math

contador=0
def busqueda_binaria(lista, comienzo, final, objetivo):
    global contador
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    contador +=1
    if comienzo > final:
        
        return False, contador

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        
        return True
    elif lista[medio] < objetivo:
        
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo),


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, tamano_de_lista) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'El numero de veces que se itero fue {contador}')
   