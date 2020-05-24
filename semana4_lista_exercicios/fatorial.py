def fatorial(numero):
    
    fatorial = 1
    
    if numero == 0:
        return print(fatorial)
    
    while (numero > 1):
        fatorial = fatorial * numero
        numero = numero -1

    return print(fatorial)     

def main():
    numero = int(input("Digite o valor de n: "))
    fatorial(numero)

main()