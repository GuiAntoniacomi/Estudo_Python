from datetime import datetime
import pytz


class ContaCorrente:
    """
    Cria um objeto conta corrente para gerenciar as contas dos clientes.

    Atributos:
        titular (str): Nome completo do titular da conta.
        cpf (str): Número de CPF do titular.
        saldo (float): Saldo atual da conta.
        limite (float): Limite de cheque especial disponível.
        agencia (int): Número da agência da conta.
        num_conta (int): Número da conta corrente.
        transacoes (list): Lista de transações realizadas na conta, armazenando
            uma tupla com (valor, saldo, data e hora) para cada operação.

    Métodos:
        consultar_saldo(): Imprime o saldo atual da conta.
        depositar(valor): Adiciona o valor depositado ao saldo da conta e 
            registra a transação no histórico.
        sacar_dinheiro(valor): Realiza o saque do valor, se o saldo permitir, e 
            registra a transação no histórico.
        consultar_limite_chuequeespecial(): Imprime o limite de cheque especial
            da conta.
        consultar_historico(): Imprime o histórico de transações da conta.
        transferir(valor, conta_destino): Transfere o valor para a conta de 
            destino e registra as transações em ambas as contas.
    """
     
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, titular, cpf, agencia, num_conta):
        self.titular = titular
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print(f'Seu saldo atual é de R${self.saldo:,.2f}')

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Saldo insuficiente para realizar a operação')
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consultar_limite_chuequeespecial(self):
        print(f'Seu limite de cheque especial é de R${self._limite_conta():,.2f}')

    def consultar_historico(self):
        print('Histórico de transações: ')
        print('Valor, Saldo, Data e Hora')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


#programa
conta_Guizo = ContaCorrente('Guizo',  '000.000.000-01', 1234, 0000-1)
conta_Guizo.consultar_saldo()

# Depositando um dinheirinho na conta
conta_Guizo.depositar(10000)
conta_Guizo.consultar_saldo()
#sacando um dinheirinho da conta
conta_Guizo.sacar_dinheiro(2000)
conta_Guizo.consultar_saldo()
conta_Guizo.consultar_limite_chuequeespecial()

print('-=' * 20)
conta_Guizo.consultar_historico()

print('-=' * 20)
conta_Ge = ContaCorrente('Eugenia', '111.222.333-02', 1234, 0000-2)
conta_Guizo.transferir(1000, conta_Ge)


conta_Ge.consultar_saldo()
conta_Guizo.consultar_saldo()

conta_Guizo.consultar_historico()
conta_Ge.consultar_historico()