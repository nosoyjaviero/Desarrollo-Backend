import numpy as np

#generar los 100 numeros naturales y elevarlos al cubo
def numeros(cantidad):
    numeros={   
    }
    for numero in range (1,cantidad+1):
        numeros[numero]=numero**3;
    print(numeros)
    return numeros
#numeros que no sean divisibles entre 3
def numeros_diferentes_de_3(cantidad):
    numeros={   
    }
    for numero in range (1,cantidad+1):
        if (numero%3)!=0:
            numeros[numero]=numero;
    print(numeros);
    




if __name__=='__main__':
    # numeros(300)
    # numeros_diferentes_de_3(100);
    
     #lo anterior pero en Dictionary comprehensions
    # my_dict = {i: i**3 for i in range(1,101) if i%3 !=0 } 
     
    #reto: crear, con un Dictionary comprehensions, un diccionario cuyas llaves sean los 1000 primeros numeros naturales con sus raices cuadradas como valores
    
    my_dict={i: np.sqrt(i) for i in range(1,1001)} 
      
    print(my_dict) 
    
    
#generar esos numeros pero al cubo