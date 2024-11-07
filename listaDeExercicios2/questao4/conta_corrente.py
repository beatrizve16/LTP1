from conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numero, titular, saldo=0, limite_cheque_especial=100):
        super().__init__(numero, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo - valor >= -self.limite_cheque_especial:
            self.saldo -= valor
        else:
            print("Saldo insuficiente com cheque especial.")

    def exibir_informacoes(self):
        print(f"Conta Corrente - Número: {self.numero}, Titular: {self.titular}, Saldo: {self.saldo}")
