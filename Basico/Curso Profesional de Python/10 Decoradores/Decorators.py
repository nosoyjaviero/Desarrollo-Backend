# def decorador(func):
# 	defenvoltura():
# 	  print('Esto se añade a mi función original')
# 	return envoltura

# @decorador
# def saludo():
#  print('Hola!')

# saludo() # Esto se añade a mi función original. Hola!

# def mayusculas(func):
# 	def envoltura(texto):
# 		return func(texto).upper()
# 	return envoltura

# @mayusculas
# def mensaje(nombre):
# 	return f'{nombre} recibiste un mensaje'

# print(mensaje('Cesar'))

from datetime import datetime

# def execution_time(func):
#     def wrapper():
#         initial_time=datetime.now()
#         func()
#         final_time= datetime.now()
#         time_elapsed = final_time - initial_time  
#         print('Pasaron '+ str(time_elapsed.total_seconds()) + " segundos")
#     return wrapper


    

def execution_time(func):
    """_summary_
    Sirve para medir el tiempo de ejecucuon de una funcion
No importa que parametros le pasemos, el los leera.
    Args:
        func (_any_): _Cualquiera_
    """
    def wrapper(*args, **kwargs):
        initial_time=datetime.now()
        func(*args, **kwargs)
        final_time= datetime.now()
        time_elapsed = final_time - initial_time  
        print('Pasaron '+ str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,10000000):
        pass

@execution_time
def suma (a:int, b: int)->int:
    return a+b

@execution_time
def saludo(nombre="Javier"):
    print(f"Hola mi nombre es {nombre}")
    
random_func()
print(suma(1,2))
saludo()
