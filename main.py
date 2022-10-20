import progressbar 
import time 
import qrcode
from PIL import Image

import climage

class bcolors:
    HEADER = '\033[95m'
    INFORMATION = '\033[94m'
    AVISO = '\033[96m'
    OKGREEN = '\033[92m'
    ALERT = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def abrirArquivo():
    # d->0; n->1; z->2; e->3
    try:
        arq = open('config.txt')
        linhas = arq.readlines()
        i = 0
        for linha in linhas:
            if '\n' or ';' in linha:
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
    arq = open('texto.txt', 'w')
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

    print(bcolors.AVISO + 'Compartilhe o texto: {}'.format(calc) + bcolors.ENDC)
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
                arq = open('texto.txt')
                linhas = arq.readlines()
                try:    
                    for i, linha in  enumerate(linhas):
                        # print(linha[:-1], '->', i)
                        if '\n' in linha:
                            linhas[i] = int(linha[:-1])
                            # print (linhas)
                        else:
                            linhas[i] = int(linha)
                    break
                except:
                    # print('oi')

                    for linhas in linha:
                        linhas = linha.split(';')
                    # print(type(linhas))
                    break
            except:
                print('Arquivo não encontrado !!!')
        else:
            print('-AVISO!!! ESCOLHA UMA DAS OPÇÕES')
            time.sleep(0.5)
    
    bar = progressbar.ProgressBar(widgets=widgets).start() 
    print(linhas)
    for i in linhas:
        if i:
            calc.append((int(i)**int(config[0]))%int(config[1]))
        bar.update() 

    print('A mensagem é: ', end='')
    for i in calc:
        print(chr(i), end='')
    print()
    time.sleep(1)
   

def verificarNumPrimo(n):
    count = 0
    if n == 0:
        print('O numero digitado é 0')
    else:
        for i in range(1, n):
            if (n % i == 0):
                # print(n % i, '=>', i)
                count += 1
        if (count != 1):
            print('O numero {} não é PRIMO'.format(n))
            return False
        else:
            # print('O numero {} é PRIMO'.format(n))
            return True
    # print ('oi')

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
    
    while True:
        valorQ = int(input('digite o valor de Q: '))
        if verificarNumPrimo(valorQ):
            break
    while True:
        valorP = int(input('digite o valor de P: '))
        if verificarNumPrimo(valorP):
            break

    valorN = valorP*valorQ
    valorZ = (valorP-1)*(valorQ-1)
    
    e = calculoPrimo(1)
    mmc = valorZ
    bar = progressbar.ProgressBar(widgets=widgets).start() 
    while True: #valorE
        
        print('mmc: ', mmc, '| e: ', e )
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
    textArquivo = []
    valorE = input('Digite a 1º Chave: ')
    valorN = input('Digite a 2º Chave: ')
    text = input('Digite a frase: ')

    for i in text:
        textCripto.append(ord(i))
    for i in textCripto:
        mensagem.append(str((i**int(valorE))%int(valorN)))

    for i in mensagem:
        txt = str(i) + '\n'
        textArquivo.append(txt)
    print('Compartilhe o texto: ', mensagem)
    # input('press enter...')
    salvarArquivo(textArquivo)
    time.sleep(1)

def whats():
    telefone = input('Digite o numero com o DDD: ')
    mensagem = ''

    arq = open('texto.txt')
    linhas = arq.readlines()
    for i, linha in  enumerate(linhas):
        # print(linha[:-1], '->', i)
        if '\n' in linha:
            mensagem += linha[:-1] + ';'
        else:
             mensagem += linha
    # print(linhas) 
    link = 'https://wa.me/55{}?text={}'.format(telefone, mensagem)
    qr = qrcode.QRCode(version = 1, 
                   box_size = 30, 
                   border = 10) 
    qr.add_data(link) 
    qr.make(fit = True) 
    img = qr.make_image()
    img.save('qrcode.png')

    with Image.open('qrcode.png') as img:
        img.show()
    
    #Exibe img no console, mas esta distorcido
    # output = climage.convert('qrcode.png', True, False, False, True, False, 20)
    # print(output)

while True:
    
    print(f'''====================================
  1-Criptografar Mensagem
  2-Descriptografar Mensagem
  3-Criptografar Mensagem Parceiro
  4-Enviar Mensagem WhatsApp
  5-Configurar
  6-Sair
====================================''')
    esc = input('escolha (1-6): ')

    if esc == '1':
        cripto(abrirArquivo())
    elif esc == '2':
        descCripto(abrirArquivo())
    elif esc == '3':
        criptoParc()
    elif esc == '4':
        whats()
    elif esc == '5':
        configg()
    elif esc == '6':
        break
    else:
        print('-AVISO!!! ESCOLHA UMA DAS OPÇÕES')
        time.sleep(0.5)
