def ordenacao(num1, num2, num3):
    if num3 > num2 and num2 > num1:
        return(print("crescente"))
    return(print("não está em ordem crescente"))

def main():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))
    num3 = int(input("Digite um número: "))
    ordenacao(num1, num2, num3)

main()