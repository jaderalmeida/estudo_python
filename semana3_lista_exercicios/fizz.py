def divide_por_3(numero):
    if numero % 3 != 0:
        return(print(numero))
    return(print("Fizz"))

def main():
    numero = int(input("Digite um número: "))
    divide_por_3(numero)

main()