interface = """
=======Banco=======
Extrato
Sacar
Depositar
Sair
===================
"""
extrato = ""
saldo = 0
saques = 0
while True:
    print(interface)
    escolha = str(input("O que pretendes? "))
    if escolha.title() == "Extrato":
        if not extrato:
            print("=======Extrato=======")
            print("Não há movimentações recentes.")
            print(f"Saldo: R${saldo:.2f}")
            print("=====================")
        else:
            print("=======Extrato=======")
            print(extrato)
            print(f"Saldo: R${saldo:.2f}")
            print("=====================")
    if escolha.title() == "Sacar":
        valor = float(input("Quanto pretendes sacar? "))
        if valor <= 0:
            print("Valor inválido.")
        if valor > saldo:
            print("Saldo insuficiente.")
        if valor > 500:
            print("Limite máximo de saque atingido.")
        if saques >= 3:
            print("Limite diário de saques expirado. Tente novamente amanhã.")
        if valor <= saldo:
            saldo -= valor
            saques += 1
            extrato += f"Saque: R${valor:.2f}\n"
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
    if escolha.title() == "Depositar":
        valor = float(input("Quanto pretendes depositar? "))
        if valor <= 0:
            print("Valor inválido.")
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R${valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    if escolha.title() == "Sair":
        print("Obrigado por usar meu banco.")
        break
