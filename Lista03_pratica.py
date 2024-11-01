# Lista 03 - Prática
# 1 - Crie uma classe "Carro" com os atributos marca, ano e cor.
# Em seguid, crie um objeto dessa classe e imprima seus atributos.

class Carro():
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def informacaoSaida(self):
        print(f'Marca do Carro: ',self.marca, 'Modelo: ', self.modelo, 'Ano: ',self.ano, 'Cor: ',self.cor )

carro1 = Carro(input('Marca do carro: '),input('Modelo: '),input('Ano: '), input('Cor: '))

carro1.informacaoSaida()


# 2 - Crie uma classe "Pessoa" com os atributos dados pessoais fictícios.
# Crie um objeto e exiba uma mensagem usando esses atributos.

class Pessoa():
    def __init__(self,nome_completo, cpf, rg, idade, cidade_que_reside, estado_que_reside, estado_civil):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
        self.cidade_que_reside = cidade_que_reside
        self.estado_que_reside = estado_que_reside
        self.estado_civil = estado_civil

    def informacaoSaida(self):
        print(f'Informe o Nome completo: ',self.nome_completo),print('Informe o seu CPF: ',self.cpf),print('Informe o seu RG: ',self.rg),print('Informe sua Idade: ',self.idade),print('Informe a Cidade em que resíde: ',self.cidade_que_reside),print('Informe o Estado que resíde: ',self.estado_que_reside),print('Informe o Estado Cívil',self.estado_civil)
pessoa1 = Pessoa(input('Nome Completo: '),input('CPF: '),input('RG: '),input('Idade: '),input('Cidade que Reside: '),input('Estado que Reside: '),input('Estado Civil: '))


pessoa1.informacaoSaida()




# 3 - Crie uma classe "ContaBancária" contendo os dados da conta, incluindo o atributo "saldo" e igual a R$ 1000,00.
# 3 - Crie uma classe "ContaBancária" contendo os dados da conta, incluindo o atributo "saldo" e igual a R$ 1000,00.
# Adicione métodos para depositar valor a essa conta e em seguida imprima o saldo atual e nome do cliente.


class ContaBancaria:
    def __init__(self, nome_cliente, numero_conta, saldo=1000):
        self.nome_cliente = nome_cliente
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        valor = float(valor)
        self.saldo += valor
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')

    def informacaoSaida(self):
        print(f'Nome do cliente: {self.nome_cliente}')
        print(f'Número da conta: {self.numero_conta}')
        print(f'Saldo atual: R$ {self.saldo:.2f}')


conta1 = ContaBancaria(input('Nome do cliente: '), input('Número da conta: '))

conta1.depositar(input('Valor do depósito: '))

conta1.informacaoSaida()