def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    
    # num = input('Ingresa un número: ')
    # assert num.isnumeric(), "Debes ingresar un número"
    # print(divisors(int(num)))
    # print("Terminó mi programa")
    
 # reto  
     num=(input('Ingresa un número: '))
    
     assert num.lstrip('-').isdigit() , "Debes ingresar un número"
    
     assert int(num) >= 0, "Numero no debe ser negativo"    
     print(divisors(int(num)))
     print("Terminó mi programa")





if __name__ == '__main__':
    run()
