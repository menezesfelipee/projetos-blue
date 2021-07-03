from datetime import datetime
from os import system
from tabulate import tabulate
from time import sleep

def autoriza_voto(anoNascimento):
    idade = anoAtual - anoNascimento
    if idade < 16:
        autorizacao = 'NEGADO'
    elif 18 <= idade < 70:
        autorizacao = 'OBRIGATÓRIO'
    else:
        autorizacao = 'OPCIONAL'
    return autorizacao

def votacao(autorizacao, voto = 0):
    if autorizacao == 'NEGADO':
        print('\nVocê não tem idade para votar!')
    else:
        for index, candidato in enumerate(votos.keys()):
            if index == voto - 1:
                votos[candidato] += 1
                if voto <= 3:
                    votosValidos[candidato] += 1
        print('\nVoto computado com sucesso!')
    
def tabela(votos):
    tabelaVotos = list(votos.items()) + [('TOTAL', sum(votos.values()))]
    return tabulate(tabelaVotos, ("CANDIDATO", "VOTOS"), tablefmt="psql")

def grafico(votos):
    if sum(votos.values()) > 0:
        visualizacao = list()
        for candidato, quantidade in votos.items():
            graficoLinha = ''
            porcentagem = round(quantidade / sum(votos.values()) * 100)
            for i in range(porcentagem):
                graficoLinha += '|'
            visualizacao.append([candidato, str(porcentagem)+" %", graficoLinha])
        return tabulate(visualizacao, ["CANDIDATO", " %", "GRÁFICO"], tablefmt="simple")
    else:
        return 'Ainda não temos votos suficientes para gerar um gráfico.'

def escolha(opcao):
    if opcao == 1:
        print(f'\n{tabela(votos)}')
    elif opcao == 2:
        print(f'\n{grafico(votos)}')
    elif opcao == 3:
        print(f'\n{tabela(votosValidos)}')
    elif opcao == 4:
        print(f'\n{grafico(votosValidos)}')

def vencedor():
    if sum(votosValidos.values()) == 0:
        return '\nNenhum candidato foi eleito, pois não foi computado nenhum voto válido!'
    elif max(votosValidos.values()) / sum(votosValidos.values()) > 0.5:
        porcentagemMax = max(votosValidos.values()) / sum(votosValidos.values())
        for candidato, votos in votosValidos.items():
            if votos == max(votosValidos.values()):
                return f'\nO vencedor foi {candidato} com {porcentagemMax*100:.2f}% dos votos válidos!'
    else:
        segundoTurno = sorted(votosValidos.items(), key=lambda x: x[1], reverse=True)
        return f'''\nTeremos segundo turno entre:
        {segundoTurno[0][0]:<8} ({segundoTurno[0][1]/sum(votosValidos.values())*100:.2f}% dos votos válidos)
        {segundoTurno[1][0]:<8} ({segundoTurno[1][1]/sum(votosValidos.values())*100:.2f}% dos votos válidos)'''

        
votos = {'Augusto': 180, 'Beatriz': 70, 'Carlos': 97, 'Votos Nulos': 10, 'Votos Brancos': 10}
votosValidos = dict(list(votos.items())[:3])


anoAtual = datetime.now().year

system('cls' if system == 'nt' else 'clear')

while True:
    anoNascimento = int(input('\nDigite o ano de nascimento no formato AAAA: '))
    while anoNascimento not in range(1900, anoAtual+1):
        anoNascimento = int(input('Parece que você digitou errado. Tente novamente: '))
    if autoriza_voto(anoNascimento) != 'NEGADO':
        print('''\nCANDIDATOS\n
    [ 1 ] Augusto
    [ 2 ] Beatriz
    [ 3 ] Carlos
    [ 4 ] Voto Nulo
    [ 5 ] Voto Branco''')
        voto = int(input('\nDigite o seu voto: '))
        while voto not in range(1, 6):
            voto = int(input('Opção inválida. Tente novamente: '))
    for c in '.'*15:
        print(c, end='', flush=True)
        sleep(.1)
    votacao(autoriza_voto(anoNascimento), voto)
    sleep(3)
    system('cls' if system == 'nt' else 'clear')
    opcoes = '''\n\nO que deseja visualizar agora?\n
    [ 1 ] Distribuição dos votos
    [ 2 ] Gráfico dos votos
    [ 3 ] Distribuição dos votos válidos
    [ 4 ] Gráfico dos votos válidos\n
    [ 5 ] Ir para o próximo eleitor
    [ 6 ] Finalizar votação\n'''
    opcao = ''
    while opcao in range(1,5) or opcao == '':
        print(opcoes)
        opcao = int(input('\nEscolha uma das opções: '))
        while opcao not in range(1,7):
            opcao = int(input('Comando inválido. Escolha uma das opções: '))
        system('cls' if system == 'nt' else 'clear')
        escolha(opcao)
        if opcao in [5, 6]:
            break
    if opcao == 6:
        break
    system('cls' if system == 'nt' else 'clear')

print('Calculando o vencedor da eleição', end='')
for c in '.'*20:
    print(c, end='', flush=True)
    sleep(0.3)
print(f'\n\n    {vencedor()}')

opcoes = '''\n\nO que deseja visualizar agora?\n
    [ 1 ] Distribuição dos votos
    [ 2 ] Gráfico dos votos
    [ 3 ] Distribuição dos votos válidos
    [ 4 ] Gráfico dos votos válidos\n
    [ 5 ] Finalizar programa\n'''
opcao = ''
while opcao in range(1,5) or opcao == '':
    print(opcoes)
    opcao = int(input('\nEscolha uma das opções: '))
    while opcao not in range(1,7):
        opcao = int(input('Comando inválido. Escolha uma das opções: '))
    system('cls' if system == 'nt' else 'clear')
    escolha(opcao)
    if opcao == 5:
        break