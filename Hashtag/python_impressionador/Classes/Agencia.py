class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def caixa_agencia(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa atual: R${self.caixa:.2f}')
        else:
            print(f'O valor de caixa está ok. Caixa atual: R${self.caixa:.2f}')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            self.caixa -= valor
        else:
            print(f'Não há dinheiro suficiente para emprestar R${valor:.2f}')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
        self.caixa += patrimonio
        print(f'Cliente {nome} adicionado com sucesso')
        

class AgenciaVirtual(Agencia):

    pass

class AgenciaComun(Agencia):

    pass

class AgenciaPremium(Agencia):

    pass






agencia1 = Agencia(22434563, 123158761, 8943)

agencia_virtual = AgenciaVirtual(33334444, 152000000, 1000)
agencia_virtual.caixa = 15000
agencia_virtual.caixa_agencia()