saldo = 0
valor = 0
saques = 3
extrato = []
funcionando = True
def depositar(n):
    if valor <= 0:
        print("Você não pode realizar depósitos negativos ou nulos!")
    else:
        global saldo
        saldo += valor
        extrato.append(f"Foi depositado um valor de R$ {valor:.2f}")
        return saldo
def saque(n):
    global saldo
    if valor <=0:
        print ("Você não pode realizar saques negativos ou nulos!")
    elif valor > 500:
        print("O valor de saque não pode exceder R$ 500")
    elif valor > saldo:
        print("Você não possui saldo suficiente para efetuar esta operação!")
    else:
        saldo -= valor
        extrato.append(f"Foi realizado um saque de R$ {valor:.2f}")
        return saldo
def ver_extrato():
    print ("Seu histórico de operações:")
    print(extrato, sep= "")
    print(f"Seu saldo atual é de R${saldo:.2f}")
while funcionando == True:
    operação= (input("""
        Qual operação deseja realizar:
        Depósito (1)
        Saque (2)
        Ver extrato (3)
        Sair (4)    
        
        """))
    if operação == ("Depósito" or operação == "depósito") or operação == "1":
        valor = float(input("Qual valor deseja depositar? "))
        depositar(valor)
    elif operação == ("Saque" or operação == "saque") or operação == "2":
        if saques > 0:
            saques -= 1
            print(f"Você pode realizar mais {saques} saque(s) hoje!")
            valor = float(input("Qual valor deseja sacar? "))
            saque(valor)
        else:
            print("Você não pode mais realizar saques hoje!")
    elif (operação == "Extrato" or operação == "extrato") or (operação == "Ver extrato" or operação == "ver extrato") or (operação == "3"):
        ver_extrato()
    elif (operação == "Sair" or operação == "sair") or operação == "4":
        funcionando = False
        continue
    else:
        print("Opção invalida, por favor tente novamente!")
print ("Agradecemos sua prefêrencia!")