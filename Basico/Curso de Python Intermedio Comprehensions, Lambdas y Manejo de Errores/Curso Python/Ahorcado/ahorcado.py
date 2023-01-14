import random
import os

my_dict={
    'palabras':{}
}

def read():
    
    my_list=[]
    with open('./data.txt', "r", encoding="utf-8") as archivo:
        for linea in archivo:
            my_list.append(linea.strip())
            
    my_dict['palabras']=my_list
    
def RandonWord():    
    return random.choice(my_dict['palabras'])
    

def game():
    """_summary_
    Para este juego se genera una palabra aleatora con la funcion RandonWord y se asigna a word.
    Luego se crea una variable de tipo lista llamada palabraCifrada inicialida con la cantidad de digitos de la palabra aleatoria que se genero, Es de tipo lista para poder remplazar cada letra de con facilidad.
    """
    read()
    word= RandonWord()
    palabraCifrada= (len(word))*'_'
    palabraCifrada=list(palabraCifrada)
    Win=False
    
    while (~Win):
        try:
          os.system ("clear") 
          letra=input('Digite una letra: ')
        except :
          print('Debes digitar un caracter valido')       
        
        palabraTemporal=''    
            
        for indice in range(len(word)):
            if word[indice]==letra:
                palabraCifrada[indice]= letra
                               
        for indice in range(len(word)):
          palabraTemporal=palabraTemporal+palabraCifrada[indice]          
        print(palabraTemporal) 
         
        if palabraTemporal == word:
            Win=True
            break
        
    if Win:
      print('Ganaste')   
    


if __name__ == '__main__':
    game()
    