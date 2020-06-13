def maximo(numero1, numero2):
    if numero1 > numero2:
        return numero1
    return numero2

def main():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    maior = maximo(numero1, numero2)
    print(maior)

main()