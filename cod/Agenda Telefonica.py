from time import sleep
#Função criada para salvar os contatos e consultar, logo que o algoritmo é reiniciado os dados que estão salvos são apagados e os novos adicionados ficam.
def salvar_contatos(agenda):

    arquivo = open ("contatos.txt", "w")
    
    for contato in agenda: 
        arquivo.write("{} # {} # {} # {} # {}\n".format(contato["nome"], contato["telefone"], contato["Email"], contato["Estado"], contato["Cidade"]))
    arquivo.close()

#Funçao criada para ver se já tem contato adicionado, não vai aceitar numeros repetidos. 
def existe_contato(agenda, telefone):

    if len (agenda) > 0:
        for contato in agenda:
            if contato["telefone"] == telefone:
                return True
    return False
    

def adicionar (agenda):

    while True: 
        telefone = int (input ("Informe seu telefone para cadastro: "))

        if not existe_contato (agenda, telefone):
            break
        else: 
            print("Esse número já foi informado, por favor informe outro número!!!")

    contato = {
        "telefone" : telefone,
        "nome" : input("Informe seu nome: "),
        "Email" : input("Email: "),
        "Estado" : input("Estado: "),
        "Cidade" : input("Cidade: ")
    }
    agenda.append(contato) 
    print("O contato {} foi adicionado!".format(contato["nome"]))

#Função criada para excluir contato existente
def retirar(agenda):
    print("="*3, "Excluir contato", "="*3)
    if len(agenda) > 0:
        #for i, contato in enumerate(agenda):
        del agenda[len(agenda)-1]
       
        print("O contato foi excluido!")
    else: ("Não existe nenhum contato cadastrado!!!")

#Função criada para mostrar os dados que foram informados.
def listar(agenda): 

    print("="*35)
    if len(agenda) > 0: 
        for i, contato in enumerate(agenda): 
            print("Contato: {}".format(i+1))
            print("\t Nome: {}".format(contato["nome"]))
            print("\t Telefone: {}".format(contato["telefone"]))
            print("\t Email: {}".format(contato["Email"]))
            print("\t Estado: {}".format(contato["Estado"]))
            print("\t Cidade: {}".format(contato["Cidade"]))
        print("Total de contatos na agenda: {}".format(len(agenda))) 
        print("="*35)
    else:
        print("\nNão existe nenhum contato cadastrado!!!\n")

#Primeiro contato da agenda       
def topo(agenda): 

    print("="*35)
    if len(agenda) > 0: 
        print("Valor do TOPO da agenda: ", agenda[len(agenda)-1])
                                      
    else:
        print("\nNão existe nenhum contato cadastrado!!!\n")
                 
def vazia(agenda): 
    vazia = len(agenda) 
    if vazia == 0:
        print("Agenda vazia.")
    else:
        print("Agenda não vazia.")

#Função criada para buscar usuarios pelo telefone. 
def consultar (agenda):
 
    print("="*35)
    if len(agenda) > 0: 
            telefone = int(input ("Informe o numero do usuario que você está procurando: "))
            if existe_contato(agenda, telefone):
                for  contato in agenda: 
                    if contato["telefone"] == telefone:
                        print("Nome: {}".format(contato["nome"]))
                        print("Telefone: {}".format(contato["telefone"]))
                        print("Email: {}".format(contato["Email"]))
                        print("Estado: {}".format(contato["Estado"]))
                        print("Cidade: {}".format(contato["Cidade"]))
                        print("="*35)
            else:
                print("Esse contato não existe!")          
    else:
        print("\nNão existe nenhum contato cadastrado!!!\n")

def menu():

    agenda=[] #Iniciando agenda vazia 
   

    while True: 
        print("-------- MENU --------")
        print("1 - Cadastrar um novo usuario")
        print("2 - Excluir ")
        print("3 - Informar um resumo dos dados da agenda")
        print("4 - Consultar o TOPO da agenda")
        print("5 - Indicar se a agenda está vazia")
        print("6 - Consultar um usuario por telefone")
        print("7 - Terminar o sistema")
        op = int (input("Escolha uma opção: ")) 

        if op == 1:
            adicionar(agenda) 
            salvar_contatos(agenda)
        elif op == 2: 
            retirar(agenda)
            salvar_contatos(agenda)
        elif op ==3:
            listar(agenda)
        elif op ==4:
            topo(agenda)
        elif op ==5:
            vazia(agenda)
        elif op ==6:
             consultar(agenda)
        elif op ==7:
            print("Aguarde...")
            sleep(1)
            print("Sistema Encerrado")
            break
        else: 
            print("Opção inválida, tente novamente")

menu()