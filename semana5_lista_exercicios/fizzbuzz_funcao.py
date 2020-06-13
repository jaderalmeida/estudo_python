def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return("FizzBuzz")
    elif numero % 3 == 0:
        return("Fizz")
    elif numero % 5 == 0:
        return("Buzz")
    return(numero)

def main():
    numero = int(input("Digite um número: "))
    print(fizzbuzz(numero))

main()
