def main():
    nome_cliente = input("Digite o nome do cliente: ")
    data_vencimento = input("Digite o dia de vencimento: ")
    mes_vencimento = input("Digite o mês de vencimento: ")
    valor_fatura = input("Digite o valor da fatura: ")

    print("Olá,", nome_cliente)
    print("A sua fatura com vencimento em", data_vencimento, "de", mes_vencimento, "no valor de R$", valor_fatura, "está fechada.")

main()