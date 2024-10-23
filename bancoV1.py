op = -1
saldo = 0
TOTAL_SAQUE = 1

historico = []

while(op != 0):

    print("\n BEM-VINDO AO SISTEMA BANCÁRIO \n")
    print(" 1 - DEPOSITAR \n 2 - SACAR \n 3 - EXTRATO \n \n 0 - SAIR \n")
    op = int(input("Digite o número da operação que deseja realizar: "))

    if(op == 1):
        print("\n")
        valor = float(input("Qual o valor do deposito?: "))

        if(valor <= 0):
            print("Informe um valor acima de R$ 0,00 ")
        else:
            saldo += valor
            print("Deposito realizado com sucesso! \n")
            historico.append(f"+ deposito de R${valor:06.2f}")

    elif(op == 2):
        print("\n")
        if(TOTAL_SAQUE > 3):
            print("Você atingiu o limite de saques diário.")
        else:   
            valor = float(input("Quanto você deseja sacar?: "))

            if(valor <= 0):
                print("Informe um valor acima de R$ 0,00 ")
            elif(valor > 500):
                print("Seu limite por saque é de R$ 500,00 \n")
            elif(valor <= saldo):  
                saldo -= valor
                print("Saque realizado com sucesso! \n")
                TOTAL_SAQUE += 1
                historico.append(f"- saque de R${valor:06.2f}")
            else:
                print("Saldo insificiente \n")

    elif(op == 3):
        print("\n")
        if(len(historico)==0):
            print("Não foram realizadas movimentações.")
        else:
            print("\n==============EXTRATO============== \n")
            for operacao in historico:
                print(f"# {operacao}")
                print("________________________________")
            
            print(f"\n SALDO ATUAL: R$ {saldo:06.2f}")
            print("===================================")
    elif(op == 0):
        break
    else:
        print("Informe um número das opções válidas")

print("Até a próxima!")
