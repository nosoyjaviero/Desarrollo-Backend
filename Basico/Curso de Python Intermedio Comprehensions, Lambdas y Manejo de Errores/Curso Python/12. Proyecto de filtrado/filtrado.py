DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
     # Comprehensions solutions
     
    #  trabajadores de que utilizen python 
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    
    # trabajadores que trabajen platzi
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    # filtrado por edad, devuelve el diccionario comple
    adults =  [worker["name"] for worker in DATA if worker["age"] > 18]
    
    #suma de dicionario. El diccionario data + uno generado por el filtrado.
    # el | (se denomina pipe) significa suma de diccionarios. 
    # Es una caracteristica de python3.9
    # El diccionario de la izquierda lambda worker: worker, trae el diccionario completo. El diccionario de la derecha y devuelve true si cumple la condicion de que la edad es mayor a 70 y lo suma al diccionario. 
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    for worker in all_python_devs:
        print(worker)




if __name__ == '__main__':
    run()