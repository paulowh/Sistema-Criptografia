
def abrirArquivo():
    # d->0; n->1; z->2; e->3
    try:
        arq = open('dados.txt')
        linhas = arq.readlines()
        i = 0
        for linha in linhas:
            if '\n' in linha:
                linhas[i] = int(linha[:-1])
            else:
                linhas[i] = int(linha)
            i+=1
        return linhas
    except:
        arquivo = open('dados.txt', 'a')
        #Uma configuração padrão onde o Q = 17 e P = 7
        texto = ['37\n', '119\n', '96\n','13\n'] 
        arquivo.writelines(texto)
        arquivo.close()
        return texto


def cripto(config):
    calc = []
    textCripto = []
    text = input('Digite a frase: ')

    for i in text:
        textCripto.append(ord(i))
    for i in textCripto:
        calc.append((i**int(config[3]))%int(config[1]))
    print('Compartilhe o texto: ', calc)
    input('press enter...')


def descCripto(config):
    calc = []
    textDescripto = []
    # print('ALERTA !!!')
    # print('Para fechar o sistema digite S')

    while True:
        dig = input('Digite o cod ou (S)air: ')
        if dig in 'Ss':
            break
        else:
            textDescripto.append(int(dig))
    
    for i in textDescripto:
        calc.append((i**int(config[0]))%int(config[1]))

    print('A mensagem é: ', end='')
    for i in calc:
        print(chr(i), end='')
    print()
    input('press enter...')


def calculoPrimo(e):
    while True:
        cont = 0
        i = 0
        e += 1
        while i <= e or cont < 2:
            i += 1
            x = e % i
            if x == 0:
                cont += 1
        if cont <= 2:
            break
    return e


def configg():

    valorQ = int(input('digite o valor de Q: '))
    valorP = int(input('digite o valor de P: '))
    valorN = valorP*valorQ
    valorZ = (valorP-1)*(valorQ-1)
    
    e = calculoPrimo(1)
    mmc = valorZ
    while True: #valorE
        
        if mmc <= e:
            valorE = calculoPrimo(e)
            break
        elif mmc % e != 0:
            e = calculoPrimo(e)
            print(e)
        elif mmc % e == 0:
            mmc = mmc//2

    d = 1
    while True: #valorD

        if 1 == (d*valorE)%valorZ:
            valorD = d
            print(d)
            break
        d += 1
    
    print('Valor public (', valorE, ',',valorN,')')
    print('Valor private (', valorD, ',',valorN,')')
    
    arq = open('dados.txt', 'w')
    # d->0; n->1; z->2; e->3
    config = ['{}\n'.format(valorD),'{}\n'.format(valorN),'{}\n'.format(valorZ),'{}\n'.format(valorE)] 
    arq.writelines(config)
    arq.close()


def criptoParc():
    calc = []
    textCripto = []
    valorE = input('Digite a 1º Chave: ')
    valorN = input('Digite a 2º Chave: ')
    text = input('Digite a frase: ')

    for i in text:
        textCripto.append(ord(i))
    for i in textCripto:
        calc.append((i**int(valorE))%int(valorN))
    print('Compartilhe o texto: ', calc)
    input('press enter...')


while True:
    
    print(f'''
    1-Criptografar Mensagem
    2-Descriptografar Mensagem
    3-Criptografar Mensagem Parceiro
    4-Configurar
    5-Sair''')
    esc = input('escolha (1-5): ')

    if esc == '1':
        cripto(abrirArquivo())
    elif esc == '2':
        descCripto(abrirArquivo())
    elif esc == '3':
        criptoParc()
    elif esc == '4':
        configg()
        print('olá')
    elif esc == '5':
        break
    else:
        print('escolha uma das opções')
        