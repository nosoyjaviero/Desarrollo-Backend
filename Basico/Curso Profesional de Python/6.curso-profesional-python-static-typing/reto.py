def primo(numero: int ) ->bool:
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def run():
    print(primo(12))
    
if __name__== '__main__':
     run()