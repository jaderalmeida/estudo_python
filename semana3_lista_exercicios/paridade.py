def par_ou_impar(numero):   
    if (numero % 2 == 0):
        return print("par")
    return print("ímpar")

def main():
    numero = int(input("Digite um número: "))
    par_ou_impar(numero)

main()