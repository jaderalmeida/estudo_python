def adjacentes(numero):
    digito_anterior = numero % 10
    numero = numero // 10
    digito_atual = 0

    while numero > 0:
        digito_atual = numero % 10
        numero = numero // 10
        if digito_anterior == digito_atual:
            return print("sim")
        digito_anterior = digito_atual
    return print("não")

def main():
    numero = int(input("Digite um número inteiro: "))
    adjacentes(numero)

main()