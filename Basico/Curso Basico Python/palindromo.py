

def palindromo (palabra):
    palabra= palabra.replace(' ', '');
    palabra=palabra.lower();
    palabra_invertida =palabra[::-1];
    if palabra == palabra_invertida:
        return True;
    else:
        return False;
    
    
def main():
    palabra= input("digite el palindormo ");
    es_palindromo= palindromo(palabra);
    if es_palindromo == True:
        print("Es Palindromo")
    else:
        print("No es palindromo")
        
if __name__ == '__main__':
    main()
