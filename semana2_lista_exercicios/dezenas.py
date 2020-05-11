def main():
    dezena = 0
    inteiro = input("Digite um número inteiro: ")
    
    if len(inteiro) >= 2:
        dezena = inteiro[-2]   
    
    print("O dígito das dezenas é", dezena)

main()
