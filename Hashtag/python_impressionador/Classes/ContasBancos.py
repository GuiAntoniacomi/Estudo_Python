from datetime import datetime
import pytz
from random import randint


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
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self._cartoes = []

    def consultar_saldo(self):
        print(f'Seu saldo atual é de R${self._saldo:,.2f}')

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Saldo insuficiente para realizar a operação')
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chuequeespecial(self):
        print(f'Seu limite de cheque especial é de R${self._limite_conta():,.2f}')

    def consultar_historico(self):
        print('Histórico de transações: ')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{randint(1, 12)}/{datetime.now().year + 4}'
        self.cod_seguranca = f'{randint(0 ,9)}{randint(0 ,9)}{randint(0 ,9)}'
        self.limite = None
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) == 4 and nova_senha.isnumeric():
            self._senha = nova_senha
        else:
            print('A senha deve conter 4 dígitos numéricos')


