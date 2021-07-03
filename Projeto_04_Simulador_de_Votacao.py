from datetime import datetime
from os import system

def autoriza_voto(anoNascimento):
    idade = anoAtual - anoNascimento
    if idade < 16:
        autorizacao = 'NEGADO'
    elif 18 <= idade < 70:
        autorizacao = 'OBRIGATÓRIO'
    else:
        autorizacao = 'OPCIONAL'
    return autorizacao

def votacao(autorizacao, voto):
    if autorizacao == 'NEGADO':
        print('Você não pode votar!')
    else:
        contagem[voto-1] += 1
    print(f'''
    ┏{"━"*15}┳{"━"*9}┓
    ┃{"Nome":^15}┃{"Votos":^9}┃
    ┣{"━"*15}╋{"━"*9}┫
    ┃{"Candidato 1":<15}┃{contagem[0]:^9}┃
    ┃{"Candidato 2":<15}┃{contagem[1]:^9}┃
    ┃{"Candidato 3":<15}┃{contagem[2]:^9}┃
    ┃{"Votos Nulos":<15}┃{contagem[3]:^9}┃
    ┃{"Votos Brancos":<15}┃{contagem[4]:^9}┃
    ┗{"━"*15}┻{"━"*9}┛''')

anoAtual = datetime.now().year
contagem = [0, 0, 0, 0, 0, 0]
system('cls')

while True:
    anoNascimento = int(input('Digite seu ano de nascimento no formato AAAA: '))
    while anoNascimento not in range(1900, anoAtual+1):
        anoNascimento = int(input('Parece que você digitou errado. Tente novamente: '))

    voto = int(input('Digite o seu voto: '))
    while voto not in range(1, 6):
        voto = int(input('Opção inválida. Tente novamente: '))

    votacao(autoriza_voto(anoNascimento), voto)

    continuar = input('\nQuer continuar votando? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Opção inválida. Tente novamente:')

    system('cls')

    if continuar == 'N':
        break
