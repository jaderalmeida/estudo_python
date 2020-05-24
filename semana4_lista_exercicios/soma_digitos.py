def soma(numero):
    soma = 0
    while (numero > 10):
        soma += numero % 10
        numero = numero // 10
    
    soma += numero

    return print(soma)     

def main():
    numero = int(input("Digite um numero inteiro: "))
    soma(numero)

main()