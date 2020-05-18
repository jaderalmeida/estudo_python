def divide_por_5e3(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return(print("FizzBuzz"))
    return(print(numero))

def main():
    numero = int(input("Digite um número: "))
    divide_por_5e3(numero)

main()