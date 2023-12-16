LIMITE_DIARIO = 3
LIMITE_SAQUE = 500
saldo = 0
extrato = ""

menu = """
********** BANCO PYTHON **********
1 - SALDO
2 - DEPOSITO
3 - SAQUE
4 - EXTRATO
5 - SAIR

Digite a opção desejada:
"""

while True:
    opcao = int(input(menu))
    if opcao == 1:
        print(f"Seu saldo é: {saldo}")
    elif opcao == 2:
        valor = float(input("Digite o valor do deposito: "))
        saldo += valor
        extrato += f"[DEPOSITO] {valor}\n"
    elif opcao == 3:
        if LIMITE_DIARIO > 0:
            valor = float(input("Digite o valor do saque: "))
            if valor <= LIMITE_SAQUE:
                if valor <= saldo:
                    saldo -= valor
                    LIMITE_DIARIO -= 1
                    extrato += f"[SAQUE] {valor}\n"
                else:
                    print("Saldo insuficiente!")
            else:
                print("Valor acima do limite!")
        else:
            print("Limite diario atingido!")
    elif opcao == 4:
        print(extrato)
        print(f'====================\n')
        print(f"Seu saldo é: {saldo}")
        print(f'====================\n')
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
