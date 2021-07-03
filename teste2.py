from datetime import datetime
from os import system
from tabulate import tabulate

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
        print('Você não tem idade para votar!')
    else:
        for index, quantidade in enumerate(votos.values()):
            if index == voto - 1:
                quantidade += 1
        print('Voto computado com sucesso!')
    
def tabela(votos):
    return tabulate(list(votos.items()), ("CANDIDATO", "VOTOS"), tablefmt="psql")

def grafico(votos):
    # visualizacao = ''
    visualizacao = list()
    for candidato, quantidade in votos.items():
        graficoLinha = ''
        porcentagem = round(quantidade / sum(x for x in votos.values()) * 100)
        for i in range(porcentagem):
            graficoLinha += '|'
        # visualizacao += f'\n{candidato:<15}{str(porcentagem)+"%":^6}{graficoLinha}'
        visualizacao.append([candidato, str(porcentagem)+" %", graficoLinha])
    return tabulate(visualizacao, ["CANDIDATO", " %", "GRÁFICO"], tablefmt="simple")

def escolha(opcao):
    if opcao == 1:
        print(tabela(votos))
    elif opcao == 2:
        print(grafico(votos))
    elif opcao == 3:
        print(tabela(votosValidos))
    elif opcao == 4:
        print(grafico(votosValidos))
    else:
        pass

votos = {'Augusto': 30, 'Beatriz': 22, 'Carlos': 13, 'Votos Nulos': 17, 'Votos Brancos': 18}
votosValidos = dict(list(votos.items())[:3])



for index, quantidade in enumerate(votos.values()):
    if index == 0:
        quantidade += 1
    print(index, quantidade)

for i in votos.values():
    i += 1

print(votos.values())

anoAtual = datetime.now().year

# system('cls')

# while True:
#     anoNascimento = int(input('Digite o ano de nascimento no formato AAAA: '))
#     while anoNascimento not in range(1900, anoAtual+1):
#         anoNascimento = int(input('Parece que você digitou errado. Tente novamente: '))

#     voto = int(input('Digite o seu voto: '))
#     while voto not in range(1, 6):
#         voto = int(input('Opção inválida. Tente novamente: '))

#     votacao(autoriza_voto(anoNascimento), voto)

#     opcoes = '''O que deseja visualizar agora?
#     [ 1 ] Distribuição dos votos
#     [ 2 ] Gráfico dos votos
#     [ 3 ] Distribuição dos votos válidos
#     [ 4 ] Gráfico dos votos válidos
#     [ 5 ] Ir para o próximo eleitor
#     [ 6 ] Finalizar votação\n'''

#     opcao = ''
#     while opcao in range(1,5) or opcao == '':
#         print(opcoes)
#         opcao = int(input('Escolha uma das opções: '))
#         while opcao not in range(1,7):
#             opcao = int(input('Comando inválido. Escolha uma das opções: '))
#         escolha(opcao)
#         if opcao in [5, 6]:
#             break

#     if opcao == 7:
#         break

#     system('cls')