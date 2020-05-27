import pymongo
from dados import Clientes, Calcado, Funcionario, Venda, Loja
from datetime import date
import jsons

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["P1_Python"]
mycalcado = mydb["Calcado"]
myfuncionario = mydb["Funcionario"]
mycliente = mydb["Cliente"]
myvenda = mydb["Venda"]
myloja = mydb["Loja"]

controle = True

def select (mycol):
    print("Digite o campo / descricao de qual Objeto quer selecionar")
    filter_query = {input("CAMPO: "): input("VALOR: ")}
    select = mycol.find(filter_query)
    return select[0]


def selectvenda (mycol):
    idvendas = "_id"
    filter_query = {idvendas : input("Digite o id: ")}
    select = mycol.find(filter_query)
    return select[0]


def altera (mycol):
        print("Digite o campo e a descricao de qual Objeto quer ALTERAR")  ## ESCOLHENDO QUAL OPCAO VAI ALTERAR
        mydocp = {input("CAMPO: "): input("DESCRICAO: ")}
        print("Digite o campo e a nova DESCRICAO.")
        new_docp = {"$set": {input("CAMPO: "): input("DESCRICAO: ")}}
        mycol.update_one(mydocp, new_docp)

def exclui (mycol):
        print("Digite o campo e a descricao de qual Objeto deseja EXCLUIR !")
        myquery = {input("CAMPO: "): input("DESCRICAO: ")}
        try:
            mycol.delete_one(myquery)
        except:
            print("ERRO!! Objeto nao existe ou nao foi encontrado!!!")
            controle = False

while controle == True:
    opcao = int(input("1-Inserir Calcado | 2- Cadastrar Funcionario | 3- Casdastrar Cliente | 4- Cadastrar Venda | 5-Alterar | 6-Excluir | 7- Cadastrar loja | 0-Sair"
                      "\n"))


    # === AS OPCOES 1, 2, 3, 4 E 7 INSERE OS VALORES QUE DESEJA ===
    if opcao == 1:
        _id = input("Digite o id do calcado: ")
        dataentrada = input("Digite a data de entrada: ")
        datasaida = "Em estoque"
        nome = input("Digite o nome do calcado: ")                   ## INSERINDO OS VALORES NAS VARIAVEIS ##
        preco = input("Digite o preco do calçado: ")
        calcado = Calcado(_id, dataentrada, datasaida, nome, preco)
        x = mycalcado.insert_one(jsons.dump(calcado))
        print(x)
        print("\nCalcado inserido: ", calcado.nomecalcado+"\n")

    if opcao == 2:

        _id = input("Digite o id do novo funcionario: ")
        nomefuncionario = input("Digite o nome do funcionario: ")
        telefonefuncionario = input("Digite o telefone do funcionario: ")
        enderecofuncionario = input("Digite o endereco do funcionario: ")
        cidadefuncionario = input("Digite a cidade do funcionario: ")              ## INSERINDO OS VALORES NAS VARIAVEIS ##
        estadofuncionario = input("Digite o estado do funcionario: ")
        datanascimentofuncionario = input("Digite a data de nascimento do funcionario: ")
        salariofuncionario = input("Digite o salario do funcionario: ")

        # PASSANDO OS VALORES INSERIDOS
        funcionario = Funcionario(_id, nomefuncionario, telefonefuncionario, enderecofuncionario, cidadefuncionario,estadofuncionario, datanascimentofuncionario, salariofuncionario)
        x = myfuncionario.insert_one(jsons.dump(funcionario))
        print(x)
        print("Funcionario cadastrado: ", funcionario.nomefuncionario+"\n")

    if opcao == 3:
        print("Opcao Cadastrar novo cliente escolhida !\n")
        _id = input("Digite o id do novo Cliente: ")
        nomecliente = input("Digite o nome do cliente: ")
        telefonecliente = input("Digite o telefone do cliente: ")
        enderecocliente = input("Digite o endereco do cliente: ")
        cidadecliente = input("Digite a cidade do cliente: ")
        estadocliente = input("Digite o estado do cliente: ")
        datanascimentocliente = input("Digite a data de nascimento do cliente: ")

        # PASSANDO OS VALORES INSERIDOS
        clientes = Clientes(_id, nomecliente, telefonecliente, enderecocliente, cidadecliente, estadocliente, datanascimentocliente)
        x = mycliente.insert_one(jsons.dump(clientes))
        print(x)
        print("Cliente cadastrado: ", clientes.nomecliente+"\n")

    if opcao == 4:

        idvenda = input("Digite o id da nova venda: ")
        descricaovenda = input("Digite a descricao da venda: ")

        print("\nDigite o id do calcado: ")
        idcalcado = selectvenda(mycalcado)

        print("\nDigite o id do funcionario que efetuara a venda:")
        idfuncionario = selectvenda(myfuncionario)

        print("\nDigite o id do cliente: ")
        idcliente = selectvenda(mycliente)

        datavenda = (str(date.today()))  # Colocando o dia atual na data da venda.

        print("\nInforme o id da loja: ")
        try:
            idloja = selectvenda(myloja)
        except:
            print("Ainda não existe nenhuma loja cadastrada! ")
            continue

        venda = Venda(idvenda, descricaovenda, idcalcado, idfuncionario, idcliente, datavenda, idloja)
        x = myvenda.insert_one(jsons.dump(venda))
        print(x)
        print("Venda cadastrada com sucesso!\n")

    if opcao == 7:
        _id = input("Informe o id da nova loja: ")
        quantidadefuncionarios = input("Informe a quantidade de funcionarios nesta loja: ")
        telefoneloja = input("Informe telefone da loja: ")
        enderecoloja = input("Informe o endereco da loja: ")
        cidadeloja = input("Informe a cidade da loja: ")
        estadoloja = input("Informe o estado em que fica a loja: ")

        loja = Loja(_id, quantidadefuncionarios, telefoneloja, enderecoloja, cidadeloja, estadoloja)
        x = myloja.insert_one(jsons.dump(loja))
        print(x)
        print("Parabéns pela nova loja, ela foi cadastrada com sucesso !!!\n")
    #///////////////////////////////////////////////////////////////

    ## ====== OPCAO 5 ONDE ALTERA A OPCAO DESEJADA  ====== ##
    if opcao == 5:
        ALTERAR = int(input("ALTERAR: 1- Calcados | 2- Funcionarios | 3-Clientes | 4-Vendas | 5- Lojas 0-Sair"
                           "\n"))
        if ALTERAR == 1:
            altera(mycalcado)

        if ALTERAR == 2:
            altera(myfuncionario)

        if ALTERAR == 3:
            altera(mycliente)

        if ALTERAR == 4:
            altera(myvenda)

        if ALTERAR == 5:
            altera(myloja)

    ## ================= ##

    # ===OPCAO 6 ONDE EXCLUI A OPCAO DESEJADA=== #
    if opcao == 6:
        EXCLUIR = int(input("EXCLUIR: 1-Calcados | 2-Funcionarios | 3-Clientes | 4-Vendas | 0-Sair"
                           "\n"))
        if EXCLUIR == 1:
            exclui(mycalcado)

        if EXCLUIR == 2:
            exclui(myfuncionario)

        if EXCLUIR == 3:
            exclui(mycliente)

        if EXCLUIR == 4:
            exclui(myvenda)

        if EXCLUIR == 5:
            exclui(myloja)

    if opcao == 0:
        break

    if opcao > 7 or opcao < 0:
        print("Opção Inválida! Digite Novamente.")
