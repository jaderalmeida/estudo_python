def divide_por_5(numero):
    if numero % 5 != 0:
        return(print(numero))
    return(print("Buzz"))

def main():
    numero = int(input("Digite um número: "))
    divide_por_5(numero)

main()