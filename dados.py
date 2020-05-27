
class Clientes:
    def __init__(self, _id, nomecliente, telefonecliente, enderecocliente, cidadecliente, estadocliente, datanascimentocliente):
        self._id = _id
        self.nomecliente = nomecliente
        self.telefonecliente = telefonecliente
        self.enderecocliente = enderecocliente
        self.cidadecliente = cidadecliente
        self.estadocliente = estadocliente
        self.datanascimentocliente = datanascimentocliente

class Calcado:
    def __init__(self, _id, dataentrada, datasaida, nomecalcado,  preco):
        self._id = _id
        self.dataentrada = dataentrada
        self.datasaida = datasaida
        self.nomecalcado = nomecalcado
        self.preco = preco


class Funcionario:
    def __init__(self, _id, nomefuncionario, telefonefuncionario, enderecofuncionario, cidadefuncionario, estadofuncionario, datanascimentofuncionario, salariofuncionario):
        self._id = _id
        self.nomefuncionario = nomefuncionario
        self.telefonefuncionario = telefonefuncionario
        self.enderecofuncionario = enderecofuncionario
        self.cidadefuncionario = cidadefuncionario
        self.estadofuncionario = estadofuncionario
        self.datanascimentofuncionario = datanascimentofuncionario
        self.salariofuncionario = salariofuncionario

class Venda:
    def __init__(self, _id, descricao, calcado, funcionario, cliente, datavenda, loja):
        self._id = _id
        self.descricao = descricao
        self.calcado = calcado
        self.funcionario = funcionario
        self.cliente = cliente
        self.datavenda = datavenda
        self.loja = loja

class Loja:
    def __init__(self, _id, quantidadefuncionarios, telefoneloja, enderecoloja, cidadeloja, estadoloja):
        self._id = _id
        self.quantidadefuncionarios = quantidadefuncionarios
        self.telefoneloja = telefoneloja
        self.enderecoloja = enderecoloja
        self.cidadeloja = cidadeloja
        self.estadoloja = estadoloja