class Cachorro():
    def __init__(self):
        self.nome = ''
        self.peso = 0.0
        self.raca = ''
        self.idade = 0

def Menu():
    print('Menu\n'
          '1 - Cadastrar cachorro\n'
          '2 - Ver cachorros cadastrados\n'
          '3 - Atualizar dados\n'
          '4 - Encontrara cachorro mias velho\n'
          '5 - Excluir cachorro da raça “pitbull”\n'
          '6 - Encontrar percentual de "vira-lata"\n'
          '7 - Encontrar o cachorro mais magro\n'
          '8 - Informar quantidade de cães de cada raça\n'
          '9 - Informar estoqeu de ração')

def Enfeite():
    print('='*30)

def Cadastrar():
    c = Cachorro()
    c.nome = input('Nome: ').title()
    c.raca = input('Raça: ').title()
    c.idade = int(input('Idade: '))
    c.peso = float(input('Peso: '))
    listaCachorro.append(c)
    arquivo = open('cachorro.txt', 'a')
    linha = c.nome + ',' + c.raca + ',' + str(c.idade) + ',' + str(c.peso) + '\n'
    arquivo.write(linha)
    arquivo.closed

def Importar():
    arquivo = open('cachorro.txt','r')
    for linha in arquivo:
        c = Cachorro()
        dados = linha.split(',')
        c.nome = dados[0]
        c.raca = dados[1]
        c.idade = int(dados[2])
        c.peso = float(dados[3])
        listaCachorro.append(c)
        arquivo.closed

def Mostrar():
    for dog in listaCachorro:
        c = Cachorro()
        print('Nome:', dog.nome , '\n'
        'Raça:', dog.raca , '\n'
        'Idade:', dog.idade , '\n'
        'Peso:', dog.peso)
        Enfeite()

def Procurar(nome):
    verificador = False
    for dog in listaCachorro:
        if nome == dog.nome:
            verificador = True
    return verificador

def AtualizaLista(nome):
    c = Cachorro()
    for dog in listaCachorro:
        if nome == dog.nome:
            dog.nome = input('Nome: ').title()
            dog.raca = input('Raça: ').title()
            dog.peso = float(input('Peso: '))
            dog.idade = int(input('Idade: '))

def AtualizaArquivo():
    c = Cachorro()
    arquivo = open('cachorro.txt','w')
    for dog in listaCachorro:
        linha = dog.nome + ',' + dog.raca + ',' +str(dog.idade) + ',' + str(dog.peso) + '\n'
        arquivo.write(linha)
    arquivo.closed

def Velho():
    maior = 0
    nome = ''
    for dog in listaCachorro:
        if dog.idade > maior:
            maior = dog.idade
            nome = dog.nome
    print('O cachorro mais velho é o {} com {} anos'.format(nome, maior))

def Excluir(nome):
    listaNome = []
    for dog in listaCachorro:
        if dog.raca == nome:
            listaCachorro.remove(dog)

def Percentual(nome):
    cont = 0
    for dog in listaCachorro:
        if dog.raca == nome:
            cont += 1
    percentual = ((cont/len(listaCachorro))*100)
    return percentual

def Magro():
    magro = 1000
    nome = ''
    for dog in listaCachorro:
        if dog.peso < magro:
            magro = dog.peso
            nome = dog.nome
    print('O nome do(a) cachorro(a) é {} e ele tem {} kg'.format(nome,magro))

listaRaca = []
def ProcararRaca(nome):
    verificador = False
    for elemento in listaRaca:
        if elemento == nome:
            verificador = True
    return verificador

def Contar():
    for dog in listaCachorro:
        nome = dog.raca
        ProcararRaca(nome)
        verificador = ProcararRaca(nome)
        if verificador == False:
            listaRaca.append(dog.raca)
    for raca in listaRaca:
        print(raca)
        cont = 0
        for dog in listaCachorro:
            if dog.raca == raca:
                cont += 1
        print(cont)

def Estoque(meses):
    peso = 0
    for dog in listaCachorro:
        peso += dog.peso
    soma = peso*meses*2
    print('O seu estoque deverá ser de {} kg'.format(soma))

listaCachorro = []
opcao = -1
Importar()

while opcao != 0:
    Menu()
    opcao = int(input('Informe a opção: '))
    if opcao == 1:
        Enfeite()
        Cadastrar()
        Enfeite()
    elif opcao == 2:
        Mostrar()
    elif opcao == 3:
        Enfeite()
        nome = input('Informe o nome do cachorro: ').title()
        verificador = Procurar(nome)
        if verificador == True:
            AtualizaLista(nome)
            AtualizaArquivo()
            Enfeite()
        else:
            Enfeite()
            print('Cachorro não encontrado!')
            Enfeite()
    elif opcao == 4:
        Enfeite()
        Velho()
        Enfeite()
    elif opcao == 5:
        Enfeite()
        nome = 'Pitbull'
        Excluir(nome)
        AtualizaArquivo()
        print('Cachorro(s) excluídos com sucesso!')
        Enfeite()
    elif opcao == 6:
        Enfeite()
        nome = 'Vira-lata'
        Percentual(nome)
        percentual = Percentual(nome)
        print('{:.0f}% são {}'.format(percentual, nome))
        Enfeite()
    elif opcao == 7:
        Enfeite()
        Magro()
        Enfeite()
    elif opcao == 8:
        Enfeite()
        Contar()
        Enfeite()
    elif opcao == 9:
        Enfeite()
        meses = 12
        Estoque(meses)
        Enfeite()
