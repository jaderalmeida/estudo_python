def primos(numero):
    primo = True
    for count in range(2,numero):
        if numero % count == 0:
            primo = False
    if primo:
        return(print("primo"))
    return(print("não primo"))

def main():
    numero = int(input("Digite um número inteiro: "))
    primos(numero)

main()