from conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, titular, saldo=0, taxa_juros=0.02):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def calcular_juros(self):
        self.saldo += self.saldo * self.taxa_juros

    def exibir_informacoes(self):
        print(f"Conta Poupança - Número: {self.numero}, Titular: {self.titular}, Saldo: {self.saldo}")
