

def read():
    numbers =[]
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
       for line in f:
        numbers.append(int(line))
    print(numbers)
             

def write():
    names = ["Facundo", "Gregorio", "Marta", "Susana", "Jose"]
    with open("./archivos/names.txt", "w") as f:
        for name in names: 
            f.write(name)
            f.write("\n")

def writeAppend():
    """_Actualizar archivo_
    
    """
    names = ["Lucy", "Sara", "RoseMary"]
    with open("./archivos/names.txt", "a") as f:
        for name in names: 
            f.write(name)
            f.write("\n")

def run():
    writeAppend()
 
if __name__ == '__main__':
    run()
    help(writeAppend)