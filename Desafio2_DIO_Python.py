import datetime as dt
import pytz
import textwrap

def menu():
    menu = """\n
    ==== Qual operação deseja realizar? ====
        [1]\tDepósito
        [2]\tSaque
        [3]\tExtrato
        [4]\tNova conta
        [5]\tListar contas
        [6]\tNovo usuário
        [0]\tSair
    ==========================================

    Digite o número da operação a ser realizada: """
    return int(input(textwrap.dedent(menu)))

def depositar(saldo, dep, extrato, data_agr, /): 

    if dep > 0:
        saldo += dep
        extrato += f"Depósito realizado: R${dep:.2f} - {data_agr}\n"
        print(f"\n Depósito de R${dep: .2f} - {data_agr} realizado com sucesso!")
    else:
        print("\n Operação falhou! Valor inválido.") 

    return saldo, extrato

def sacar(saque, limite, saldo, extrato, numero_saques, data_agr, LIMITE_SAQUES):
    if saque > limite:
        print("Essa transação não é possível de ser realizada. Limite de R$ 500 excedido.")
    elif saque > saldo:
        print("Saldo insuficiente para saque!")
    elif numero_saques >= LIMITE_SAQUES:
        print("Número máximo de saques excedido.")
    elif saque > 0:
        saldo -= saque
        extrato += f"Saque realizado: R${saque:.2f} - {data_agr}\n" 
        numero_saques += 1
        print(f"\n Saque de R${saque: .2f} - {data_agr} realizado com sucesso!")
    else:
        print("\n Operação falhou! Valor inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n -------------- Extrato --------------")
    print("Não houveram movimentações na sua conta bancária!" if not extrato else extrato)
    print(f"\nSaldo: R${saldo: .2f}")
    print("--------------------------------------")
    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 10
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    d = dt.datetime.now(pytz.timezone('America/Sao_Paulo'))
    data_agr = d.strftime("%d/%m/%Y - %H:%M")

    while True:

        opcao = menu()

        if opcao == 1:
            dep = float(input("Digite o valor de depósito: "))
            saldo, extrato = depositar(saldo, dep, extrato, data_agr)

        elif opcao == 2:
            saque = float(input("Digite o valor de saque: ")) 
            saldo, extrato = sacar(
                saque=saque,
                limite=limite,
                saldo=saldo,
                extrato=extrato,
                numero_saques=numero_saques,
                data_agr=data_agr,
                LIMITE_SAQUES=LIMITE_SAQUES
            )
        
        elif opcao == 3:
           exibir_extrato(saldo, extrato=extrato) 

        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            criar_usuario(usuarios)
        
        elif opcao == 0:
            break

        else:
            print("\n Opção inválida, selecione novamente a opção correta.")

main()
