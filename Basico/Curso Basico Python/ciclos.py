# a = list(range(1000))
# print(a)

# i = 1
# while i <= 3:
#     print(i)
#     i += 1
# print("Programa terminado")


# # for contador in range(1, 1001):
# #     print(contador)

# for i in range(10):
#     print(11 * i)
    


# def run():
#     # nombre = input('Escribe tu nombre: ')
#     # for letra in nombre:
#     #     print(letra)

#     frase = input('Escribe una frase: ')
#     for caracter in frase:
#         print(caracter.upper())


#desafio
# #programa que sume la mitad de un numero dado en for y while

def run():
    numero= input("Digite hasta que numero final ")
    numero= int(numero)
    total=0;
    
    for i in range(numero+1):
        total=total+i;
        if i == (numero/2):
            break;
    print(total);   
      
    total=0;
    i=0;
    while i<=numero: 
        total=total+i;
        if i == (numero/2):
            break;     
        i+=1;
        
    print(total);       
        
 

if __name__ == '__main__':
    run()
