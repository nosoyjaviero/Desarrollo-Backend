Mylist=list(range(1,101));
# print(Mylist);

numeros_al_cuadrado=[]
for numero in range (1, len(Mylist)+1):
    
    numeros_al_cuadrado.append(numero**2);   
    
print(numeros_al_cuadrado)


#sin ciclos
alCuadrado= [i**2 for i in Mylist]
NumerosDivisiblesEntre3= [i**2 for i in Mylist if i%3==0]
print(NumerosDivisiblesEntre3);

# Nuevo reto
# crear, con un list comprehension todos los multiplos de 4 que a la vez son multiplos de 6,9 hasta 5 digitos


Multiplos=[i for i in range(1,99999) if i%4==0 and i%6==0 and i%9==0]
print(Multiplos)
print(len(Multiplos))
