import progressbar 
import time 
 
def abrirArquivo():
    # d->0; n->1; z->2; e->3
    try:
        arq = open('config.txt')
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
        arquivo = open('config.txt', 'a')
        #Uma configuração padrão onde o Q = 17 e P = 7
        texto = ['37\n', '119\n', '96\n','13\n'] 
        arquivo.writelines(texto)
        arquivo.close()
        return texto
    
def salvarArquivo(texto):
    arq = open('mensagem.txt', 'w')
    arq.writelines(texto)
    arq.close()

def cripto(config):
    calc = []
    textCripto = []
    textArquivo = []
    text = input('Digite a frase: ')

    for i in text:
        textCripto.append(ord(i))
    for i in textCripto:
        calc.append((i**int(config[3]))%int(config[1]))
    for i in calc:
        txt = str(i) + '\n'
        textArquivo.append(txt)

    # print(textArquivo)

    salvarArquivo(textArquivo)

    print('\033[0;32mCompartilhe o texto: ', calc,'\033[0;0m')
    input('press enter...')


def descCripto(config):
    widgets = [ 'Decodificando : ', progressbar.AnimatedMarker(), ' [' , progressbar.Timer(format='%s'), ']'] 
    calc = []
    linhas = []
    while True:

        escolha = input('Deseja (D)igitar ou (A)brir um arquivo? ')
        if escolha in 'Dd':
            while True:
                dig = input('Digite o cod ou (S)air: ')
                if dig in 'Ss':
                    break
                else:
                    linhas.append(int(dig))
            break
        elif escolha in 'Aa':
            try:
                arq = open('mensagem.txt')
                linhas = arq.readlines()
                for i, linha in  enumerate(linhas):
                    # print(linha[:-1], '->', i)
                    if '\n' in linha:
                        linhas[i] = int(linha[:-1])
                    else:
                        linhas[i] = int(linha)
                break
            except:
                print('Arquivo não encontrado !!!')
        else:
            print('\033[1;31m   -AVISO!!! ESCOLHA UMA DAS OPÇÕES\033[0;0m')
            time.sleep(0.5)
    
    bar = progressbar.ProgressBar(widgets=widgets).start() 

    for i in linhas:
        calc.append((i**int(config[0]))%int(config[1]))
        bar.update() 
    print()

    print('A mensagem é: ', end='')
    for i in calc:
        print(chr(i), end='')
    print()
    time.sleep(1)
    # input('press enter...')


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
    widgets = [ 'Criando : ', progressbar.AnimatedMarker(), ' [' , progressbar.Timer(format='%s'), ']'] 
    
    valorQ = int(input('digite o valor de Q: '))
    valorP = int(input('digite o valor de P: '))
    valorN = valorP*valorQ
    valorZ = (valorP-1)*(valorQ-1)
    
    e = calculoPrimo(1)
    mmc = valorZ
    bar = progressbar.ProgressBar(widgets=widgets).start() 
    while True: #valorE
        
        if mmc <= e:
            valorE = calculoPrimo(e)
            break
        elif mmc % e != 0:
            e = calculoPrimo(e)
            # print(e)
        elif mmc % e == 0:
            mmc = mmc//2
        bar.update() 
    d = 1
    while True: #valorD

        if 1 == (d*valorE)%valorZ:
            valorD = d
            # print(d)
            break
        d += 1
        bar.update() 
    print()
    print('Valor public (', valorE, ',',valorN,')')
    print('Valor private (', valorD, ',',valorN,')')
    
    arq = open('config.txt', 'w')
    # d->0; n->1; z->2; e->3
    config = ['{}\n'.format(valorD),'{}\n'.format(valorN),'{}\n'.format(valorZ),'{}\n'.format(valorE)] 
    arq.writelines(config)
    arq.close()


def criptoParc():
    mensagem = []
    textCripto = []
    valorE = input('Digite a 1º Chave: ')
    valorN = input('Digite a 2º Chave: ')
    text = input('Digite a frase: ')

    for i in text:
        textCripto.append(ord(i))
    for i in textCripto:
        mensagem.append((i**int(valorE))%int(valorN))
    print('	\033[0;31mCompartilhe o texto: ', mensagem,'\033[0;0m')
    # input('press enter...')
    salvarArquivo(mensagem)
    time.sleep(1)


while True:
    
    print(f'''====================================
  1-Criptografar Mensagem
  2-Descriptografar Mensagem
  3-Criptografar Mensagem Parceiro
  4-Configurar
  5-Sair
====================================''')
    esc = input('escolha (1-5): ')

    if esc == '1':
        cripto(abrirArquivo())
    elif esc == '2':
        descCripto(abrirArquivo())
    elif esc == '3':
        criptoParc()
    elif esc == '4':
        configg()
   
    elif esc == '5':
        break
    else:
        print('\033[1;31m   -AVISO!!! ESCOLHA UMA DAS OPÇÕES\033[0;0m')
        time.sleep(0.5)
        