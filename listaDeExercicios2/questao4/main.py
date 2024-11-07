# main.py
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

def menu():
    print("\n--- Menu ---")
    print("1 - Conta Corrente")
    print("2 - Conta Poupança")
    print("0 - Sair")

def escolher_conta():
    while True:
        menu()
        escolha = input("Escolha o tipo de conta (1/2): ")
        if escolha == '1':
            return "corrente"
        elif escolha == '2':
            return "poupanca"
        elif escolha == '0':
            print("Saindo...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

def criar_conta():
    tipo_conta = escolher_conta()
    
    numero = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular da conta: ")
    
    if tipo_conta == "corrente":
        limite_cheque_especial = float(input("Digite o limite do cheque especial: "))
        return ContaCorrente(numero, titular, 0, limite_cheque_especial)
    elif tipo_conta == "poupanca":
        taxa_juros = float(input("Digite a taxa de juros da conta poupança (exemplo: 0.02 para 2%): "))
        return ContaPoupanca(numero, titular, 0, taxa_juros)

def operacoes_conta(conta):
    while True:
        print("\n--- Operações ---")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Exibir informações")
        print("4 - Calcular juros (apenas para Conta Poupança)")
        print("0 - Sair")
        
        escolha = input("Escolha uma operação: ")
        
        if escolha == '1':
            valor = float(input("Digite o valor para depósito: "))
            conta.depositar(valor)
        elif escolha == '2':
            valor = float(input("Digite o valor para saque: "))
            conta.sacar(valor)
        elif escolha == '3':
            conta.exibir_informacoes()
        elif escolha == '4' and isinstance(conta, ContaPoupanca):
            conta.calcular_juros()
            print(f"Juros aplicados. Novo saldo: {conta.saldo}")
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


print("Bem-vindo ao sistema bancário!")
conta = criar_conta()
operacoes_conta(conta)


