def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    
# opcion 1
  
    try:
      num = int(input('Ingresa un número: '))
      if num >=0:
                  print(divisors(num))
                  print("Terminó mi programa")
      else:
                    print("Este numero debe ser Natural")
    except ValueError:
      print('Debes digitar un numero ')
      
    
         

    
        
          
    
              
            
    
    


if __name__ == '__main__':
    run()
