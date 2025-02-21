from datetime import datetime
hoje = datetime.today()
hoje = (hoje.strftime("%d/%m/%y"))

AGENCIA = "0000"
saldo = 0
valor = 0
saques = 3
transf = 10
extrato = []
usuarios = []
contas = []
power = True

def depositar(n):
    if valor <= 0:
        print("Você não pode realizar depósitos negativos ou nulos!")
    else:
        global saldo
        saldo += valor
        extrato.append(f"Depósito de R$ {valor:.2f} em {hoje}")
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
        extrato.append(f"Saque de R$ {valor:.2f} em {hoje}")
        return saldo

def ver_extrato():
    print ("==========Seu histórico de operações==========:")
    for item in reversed(extrato):
        print(item, sep = "")
    print(f"Seu saldo atual é de R${saldo:.2f}")
    print ("==============================================:")
    return

def criar_usuario(usuarios):
    cpf = input("informe seu cpf (somente números)")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("Você já é um usuário!")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("informe sua data de nascimento (dd/mm-aaaa): ")
    endereco = input("Informe seu endereço: (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário registrado com sucesso!")

def filtrar_usuario (cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None 

def criar_conta(agencia,numero_conta, usuarios):
    cpf  = input("Informe seu cpf: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print ("Conta criada com sucesso!")
        return{"agência": agencia, "numero_conta": numero_conta, "usuário": usuario}
    print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = (f"""
    Agência: \t{conta["agencia"]}
    C/C:\t\t{conta["numero_conta"]}
    Titular\t{conta["usuario"]["nome"]}
""")
        print("=" *100)

def funcionamento ():
    global power
    global transf
    global saques
    global valor
    while power == True:
        operação = (input("""
    Qual operação deseja realizar:
    Depósito [1]
    Saque [2]
    Ver extrato [3]
    Novo usuário [4]
    Nova conta [5]
    Lista contas [6]
    Sair [7]
    
    """))
        if operação == ("Depósito" or operação == "depósito") or operação == "1":
            if transf > 0:
                transf -=1
                print(f"Você ainda pode realizar {transf} transferência(s) hoje!\n")
                valor = float(input("Qual valor deseja depositar? "))
                depositar(valor)
            else:
                print("Você não pode mais realizar transações por hoje!")
        elif operação == ("Saque" or operação == "saque") or operação == "2":
            if transf > 0:
                if saques > 0:
                    saques -= 1
                    transf -= 1
                    print(f"Você ainda pode realizar {transf} transferência(s) hoje!\n")
                    print(f"Você pode realizar mais {saques} saque(s) hoje!")
                    valor = float(input("Qual valor deseja sacar? "))
                    saque(valor)
                else:
                    print("Você não pode mais realizar saques hoje!")
            print("Você não pode mais realizar transações por hoje!")
        elif (operação == "Extrato" or operação == "extrato") or (operação == "Ver extrato" or operação == "ver extrato") or (operação == "3"):
            ver_extrato()
        elif (operação == "Novo usuário" or operação == "novo usuário") or operação == "4":
            criar_usuario (usuarios)
        elif (operação == "Nova conta" or operação == "nova conta") or operação == "5":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif (operação == "Listar contas" or operação == "listar contas") or operação == "6":
            listar_contas(contas)
        elif (operação == "Sair" or operação == "sair") or operação == "7":
            power = False
        else:
            print("Opção invalida, por favor tente novamente!")
funcionamento()
print ("Agradecemos sua prefêrencia!")
print (hoje)