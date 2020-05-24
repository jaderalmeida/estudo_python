def n_impares(numero):

    i = 1
  
    while (i <= numero*2):
        if i % 2 != 0:
            print(i)
        i += 1   

def main():
    numero = int(input("Digite o valor de n: "))
    n_impares(numero)

main()