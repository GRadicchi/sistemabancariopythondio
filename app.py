menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    sem_depositos = True
    if opcao == "d":
        print("Deposito")
        deposito = []
        while True:
            valor_deposito = float(input("Digite o valor que deseja depositar ou 0 para sair: "))
            saldo += valor_deposito
            sem_depositos = False
            if valor_deposito == 0:
                if saldo == 0:
                    break
            deposito.append(valor_deposito)
            
    elif opcao == "s":
        print("Saque")
        saque = []
        while numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor que deseja sacar ou 0 para sair: "))
            if valor_saque > 500.00:
                valor_saque = float(input("Limite excedido. Digite o valor que deseja sacar: "))
            elif valor_saque > saldo:
                valor_saque = float(input("Saldo Insuficiente. Digite o valor que deseja sacar: "))
            saldo -= valor_saque
            if valor_saque == 0:
                break
            saque.append(valor_saque)
            numero_saques += 1
        print ("Você chegou ao limite de saques diários")
       
    elif opcao == "e":
        print("Extrato")
        if sem_depositos == True:
            print ("Não Foram Realizadas Movimentações.")
        else:
            print("Saldo:")
            print(f"Seu saldo é de: R${saldo:.2f}", end="\n")
            print("Depósitos:")
            for i in range (0, len(deposito)):
                print(f"Deposito {i+1}: R${deposito[i]:.2f}", end="\n")
            print("\nSaques:")
            for i in range (0, len(saque)):
                print(f"Saque {i+1}: R${saque[i]:.2f}", end="\n")
    
    elif opcao == "q":
        break
    else:
        print("Opção Inválida. Por favor digite novamente a opção desejada.")
