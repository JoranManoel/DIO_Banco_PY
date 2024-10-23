from datetime import datetime, date
escolha = ''
saldo = 0
cont = 0
SAQUE = 1
TRASACOES = 1
AGENCIA = '0001'

historico = []
contas = {}
usuarios = {}

def cadastrar_user(cpf):
    global usuarios

    if(cpf in usuarios):
        print("\n")
        print("----------ERRO---------")
        print("Usuário já cadastrado.")
        print("-----------------------")
    else:
        nome = input("Nome do novo usuário: ")

        print("Informações do endereço:\n")
        logradouro = input("1-Logradouro: \n")
        bairro = input("2-bairro: \n")
        cidade = input("3-cidade: \n")
        estado = input("4-estado: \n")
        endereco = f"{logradouro} - {bairro} - {cidade} / {estado}"        
        
        data_str = input("Informe a data de nascimento EX.11/11/1111 : ")
        data_nascimento =  datetime.strptime(data_str, '%d/%m/%Y')

        novo_usuario = {'nome':nome, 'cpf':cpf, 'endereco': endereco, 'data_nascimento':data_nascimento.strftime('%d/%m/%Y')}

        usuarios[cpf] = novo_usuario

        print("\n")
        print("-------------Sucesso------------")
        print("Usuário cadastrado com sucesso !")
        print("--------------------------------")

def criar_conta():
    global cont
    global usuarios

    cpf = input('Informe o cpf: ')

    if cpf in usuarios:
        cont += 1

        if cpf not in contas:
            contas[cpf] = []  

        nova_conta = {
            'Numero' : cont,
            'Saldo' : 0.0
        }

        contas[cpf].append(nova_conta)

        print("\n")
        print("-------------Sucesso------------")
        print("Conta criada com sucesso !")
        print("--------------------------------")
        
    else:
        print("\n")
        print("----------ERRO---------")
        print("CPF não está cadastrado.")
        print("-----------------------")

def listar_user():
    key = ''
    while key != '0':
        print("\n")
        print("======== Usuários Cadastrados ========")
        print("[     CPF     ] [        Nome        ]")
        if len(usuarios) > 0:
            for cpf, usuario in usuarios.items():
                print(f"|   {cpf}   |   {usuario['nome']} ")
        else:
            print(" \n - Nenhum usuário encontrado - \n ")
            print("==========================================")
            return False
        print("\n")
        print("=======================================")

        key = input("Digite o número do CPF para mais informações ou 0 para sair: \n::> ")

        if key == '0':
            break
        else:
            if key in usuarios:
                print("\n")
                print("============= DADOS DO USUÁRIO =============")
                print("Contas do usuário:")
                print(f" Ag. : {AGENCIA}")
                if key in contas:
                    for valor in contas[key]:
                        print(f' Cc. {valor['Numero']} Saldo R${valor['Saldo']:06.2f}')
                else: 
                    print(" Cc. : Conta não criada")
                print(f" ------------------------------------------")
                print(f" CPF : {usuarios[key]['cpf']}")
                print(f" NOME : {usuarios[key]['nome']}")
                print(f" ENDEREÇO : {usuarios[key]['endereco']}")
                print(f" DATA DE NASCIMENTO : {usuarios[key]['data_nascimento']}")
                print('\n')
            else:
                print('Informe um CPF válido ou 0 para SAIR: ')

def depositar():
    global saldo
    global TRASACOES

    valor = float(input("Qual o valor do deposito?: "))

    if(valor <= 0):
        print("Informe um valor acima de R$ 0,00 ")
    else:
        saldo += valor
        TRASACOES += 1
        print("Deposito realizado com sucesso! \n")
        historico.append(f"+ deposito de R${valor:06.2f} | {datetime.now().strftime('%d/%m/%Y %H:%M')}")

def sacar():
    valor = float(input("Quanto você deseja sacar?: "))
    global saldo
    global SAQUE
    global TRASACOES

    if(valor <= 0):
        print("Informe um valor acima de R$ 0,00 ")
    elif(valor > 500):
        print("Seu limite por saque é de R$ 500,00 \n")
    elif(valor <= saldo):  
        saldo -= valor
        print("Saque realizado com sucesso! \n")
        SAQUE += 1
        TRASACOES +=1
        historico.append(f"- saque de R${valor:06.2f}    | {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    else:
        print("Saldo insificiente \n")

def extrato():
    print("\n==================EXTRATO================== \n")
    for operacao in historico:
        print(f"# {operacao}")
        print("-------------------------------------------")
    
    print(f"\n SALDO ATUAL: R$ {saldo:06.2f} no dia {datetime.now().strftime('%d/%m/%Y')}")
    print("===========================================")

def operacoes():
    op = -1
    while(op != 0):

        print("\n =======Menu======= \n")

        print(" 1 - DEPOSITAR \n 2 - SACAR \n 3 - EXTRATO \n \n 0 - SAIR \n")
        op = int(input("Digite o número da operação que deseja realizar: "))

        if(op == 1):
            print("\n")
            if(TRASACOES < 10):
                depositar()
            else:
                print("Você excedeu o número de trasações diárias")
        elif(op == 2):
            print("\n")
            if(TRASACOES < 10):
                if(SAQUE > 3):
                    print("Você atingiu o limite de saques diário.")
                else:   
                    sacar()
            else:
                print("Você exedeu o número de trasações diárias")
        elif(op == 3):
            print("\n")
            if(len(historico)==0):
                print("Não foram realizadas movimentações.")
            else:
                extrato()
        elif(op == 0):
            break
        else:
            print("Informe um número das opções válidas")

while(escolha != 'q'):
    print("\n BEM-VINDO AO SISTEMA BANCÁRIO \n")
    print("\n  [ N ] <= Novo usuário | Visualizar contas  => [ L ]")
    print("\n  [ C ] <= Nova conta   | Realizar operações => [ O ]")
    print("\n  [ Q ] <= Sair")

    escolha = input(" \n Informe sua escolha: ")

    if(escolha == 'o'):
        operacoes()

    elif(escolha == 'n'):
        cpf = input("Informe o cpf: ")
        cadastrar_user(cpf)

    elif(escolha == 'l'):
        listar_user()

    elif(escolha == 'c'):
        criar_conta()

    elif( escolha == 'q'):
        break
    
    else:
        print("Escolha alguma opção válida")

print("Até a próxima!")