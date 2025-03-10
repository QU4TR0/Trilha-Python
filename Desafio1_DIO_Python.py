menu = """
==== Qual operação deseja realizar? ====
    [1] Extrato
    [2] Saque
    [3] Depósito
    [0] Sair
==========================================

Digite o número da operação a ser realizada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print("\n -------------- Extrato --------------")
        print("Não houveram movimentações na sua conta bancária!" if not extrato else extrato)
        print(f"\nSaldo: R${saldo: .2f}")
        print("--------------------------------------")

    elif opcao == 2:
        saque = float(input("Digite o valor de saque: "))

        if saque > limite:
            print("Essa transação não é possível de ser realizada. Limite de R$ 500 excedido.")
        elif saque > saldo:
            print("Saldo insuficiente para saque!")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques excedido.")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque realizado: R${saque:.2f}\n" 
            numero_saques += 1
            print(f"\n Saque de R${saque: .2f} realizado com sucesso!")
        else:
            print("\n Operação falhou! Valor inválido.") 
    
    elif opcao == 3:
        dep = float(input("Digite o valor de depósito: "))
        
        if dep > 0:
            saldo += dep
            extrato += f"Depósito realizado: R${dep:.2f}\n"
            print(f"\n Depósito de R${dep: .2f} realizado com sucesso!")
        else:
            print("\n Operação falhou! Valor inválido.") 
    
    elif opcao == 0:
        break

    else:
        print("\n Opção inválida, selecione novamente a opção correta.")
