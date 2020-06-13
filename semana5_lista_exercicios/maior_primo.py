def eh_primo(numero_teste):
    mult = 0
    for count in range(2, numero_teste):
        if (numero_teste % count == 0):
            mult +=1
    
    if (mult == 0):
        return True
    return False

def maior_primo(numero):
    primo = False
    while primo == False:
        primo = eh_primo(numero)
        if primo == False:
            numero -= 1        
    return numero

def main():
    numero = int(input("Digite um número: "))
    primo = maior_primo(numero)
    print(primo)

main()