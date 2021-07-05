from datetime import datetime   # Usado pegar o ano corrente, para calcular idade.
from os import system, name     # Usado para limpar tela.
from tabulate import tabulate   # Usado para gerar tabelas mais facilmente.
from time import sleep          # Usado para esperar determinado tempo entre uma linha e outra.

def autoriza_voto(anoNascimento):   # Função solicitada para verificar a idade do cidadão que vai votar.
    idade = anoAtual - anoNascimento
    if idade < 16:
        autorizacao = 'NEGADO'
    elif 18 <= idade < 70:
        autorizacao = 'OBRIGATÓRIO'
    else:
        autorizacao = 'OPCIONAL'
    return autorizacao   # A função retornará apenas o texto que será usado na próxima função.

def votacao(autorizacao, voto = 0):     # Função usada para contabilizar os votos.
    if autorizacao == 'NEGADO':     # Se a função anterior retornar "NEGADO", o cidadão não poderá votar.
        print('\nVocê não tem idade para votar!')   # Printa que não pode votar.
    else:
        # Estou utilizando um dicionário para armazenar os votos de cada candidato. Nesse passo, usei a lista de Keys junto ao index (com o enumarete) para guardar o voto no lugar certo.
        for index, candidato in enumerate(votos.keys()):
            if index == voto - 1:   # Como as opções de voto começam em 1 e o enumarate começa em 0, é necessário tirar uma unidade para guardar certo.
                votos[candidato] += 1   # Contabilizando mais um voto para o respectivo candidato.
                # Fiz outro dicionário para guardar os votos válidos. Como os votos válidos só vão até a opção 3 se faz necessário esse if abaixo.
                if voto <= 3:
                    votosValidos[candidato] += 1    # Contabilizando mais um voto para o candidato no dicionário de votos válidos.
        print('\nVoto computado com sucesso!')  # Printa que o voto foi computado.
    
# Função extra para retornar tabelas.
def tabela(votos):
    # Essa função receberá o dicionário de votos ou de votos válidos. Na linha abaixo vou adiconar uma lista que conterá uma tupla vazia (para pular linha) e uma tupla com os votos totais.
    tabelaVotos = list(votos.items()) + [('', ''), ('TOTAL', sum(votos.values()))]
    return tabulate(tabelaVotos, ("CANDIDATO", "VOTOS"), tablefmt="psql")   # Retorna a tabela solcitada com o formato "psql".

# Função extra para retornar um "gráfico" com os dados obtidos até o momento.
def grafico(votos):
    # Esse if abaixo se faz necessário pois caso todos os votos fossem Nulos ou Brancos não seria possível calcular a porcentagem dos votos válidos (divisão por zero).
    if sum(votos.values()) > 0:
        visualizacao = list()   # Lista vazia para armazenar cada linha calculada.
        for candidato, quantidade in votos.items(): # Rodando todos candidatos e seus respectivos votos.
            graficoLinha = ''   # String vazia para escrever a linha.
            porcentagem = quantidade / sum(votos.values()) * 100     # Calculando a porcentagem votos de cada candidato.
            # Para cada porcento arredondado de voto, esse 'for' adicionará um tracinho, que será responsável pelo efeito de gráfico.
            for i in range(round(porcentagem)):
                graficoLinha += '|'     # Adicionando os tracinhos.
            visualizacao.append([candidato, f'{porcentagem:.2f}%', graficoLinha])   # Adiciona cada linha na lista de visualização.
        return tabulate(visualizacao, ["CANDIDATO", " %", "GRÁFICO"], tablefmt="simple")    # Retorna a tabela (gráfico) solicitada com o formato "simple".
    else:
        return 'Ainda não temos votos suficientes para gerar um gráfico.'   # Caso não tenha nenhum voto válido vai retornar isso.

# Função extra para printar a tabela ou gráfico que o usuário desejar.
def escolha(opcao):
    if opcao == 1:
        print(f'\n{tabela(votos)}')
    elif opcao == 2:
        print(f'\n{grafico(votos)}')
    elif opcao == 3:
        print(f'\n{tabela(votosValidos)}')
    elif opcao == 4:    # Não utilizei o else pois disponibilizarei outras opções ao usuário. Se colocasse o else, essa função chamaria a opção não desejada em algunas casos.
        print(f'\n{grafico(votosValidos)}')

# Função extra para retornar o vencedor.
def vencedor():
    if sum(votosValidos.values()) == 0:     # Se todos os votos forem Nulos ou Brancos, não terá vencedor.
        return '''
        Nenhum candidato foi eleito, pois não foi computado nenhum voto válido!'''
    elif max(votosValidos.values()) / sum(votosValidos.values()) > 0.5:     # Se a porcentagem do candidato com mais votos for maior que 50%, ele será o vencedor.
        porcentagemMax = max(votosValidos.values()) / sum(votosValidos.values())    # Variável apenas para armazenar a porcentagem o texto ficar mais claro.
        for candidato, votos in votosValidos.items():   # Rodandos todos os candidatos e seus respectivos votos.
            if votos == max(votosValidos.values()):     # Se a quantidade de votos desse candidato for igual ao máximo de votos, ele é o vencedor. Portanto, retornará:
                return f'''
        O vencedor foi {candidato} com {porcentagemMax*100:.2f}% dos votos válidos!'''
    else:   # Caso a quantidade máxima de votos não seja maior que 50% dos votos válidos.
        segundoTurno = sorted(votosValidos.items(), key=lambda x: x[1], reverse=True)   # Ordena decrescentemente o dicionário de votos válidos.
        # Imprime os dois primeiros candidatos.
        return f'''\nTeremos segundo turno entre:
        {segundoTurno[0][0]:<8} ({segundoTurno[0][1]/sum(votosValidos.values())*100:.2f}% dos votos válidos)
        {segundoTurno[1][0]:<8} ({segundoTurno[1][1]/sum(votosValidos.values())*100:.2f}% dos votos válidos)'''


# Começando efetivamente o programa.
votos = {'Augusto': 0, 'Beatriz': 0, 'Carlos': 0, 'Votos Nulos': 0, 'Votos Brancos': 0}     # Cada candidato começando com 0 votos.
votosValidos = dict(list(votos.items())[:3])    # Copiando as 3 primeiras chaves nesse novo dicionário de votos válidos.
anoAtual = datetime.now().year  # Variável que contém o ano corrente.
system('cls' if name == 'nt' else 'clear')  # Limpa a tela.
# Bloco de while abaixo vai rodar até o usuário pedir para parar o programa.
while True:
    anoNascimento = int(input('\nDigite o ano de nascimento no formato AAAA: '))
    # Bloco de while abaixo vai garantir que o usuário está digitando um ano válido (considerei abaixo de 1900 como anoo inválido).
    while anoNascimento not in range(1900, anoAtual+1):
        anoNascimento = int(input('Parece que você digitou errado. Tente novamente: '))
    if autoriza_voto(anoNascimento) != 'NEGADO':    # Se a função autoriza_voto não retornar que o voto foi NEGADO, vai executar:
        print('''\nCANDIDATOS\n
    [ 1 ] Augusto
    [ 2 ] Beatriz
    [ 3 ] Carlos
    [ 4 ] Voto Nulo
    [ 5 ] Voto Branco''')
        voto = int(input('\nDigite o seu voto: '))
        # Bloco de while abaixo vai garantir que o usuário digite um número dentre os disponíveis.
        while voto not in range(1, 6):
            voto = int(input('Opção inválida. Tente novamente: '))
    for c in '.'*15:    # Bloco de 'for' para fazer o efeito de pontinhos sendo colocados.
        print(c, end='', flush=True)    #Parâmetro flush serve para imprimir um ponto em seguida do outro.
        sleep(.1)   # Aguarda 0.1 segundo para imprimir o próximo pontinho.
    votacao(autoriza_voto(anoNascimento), voto)     # Função que verifica a idade e imprime se o voto foi computado ou se o cidadão não pode votar.
    sleep(3)    # Aguarda 3 segundos.
    system('cls' if name == 'nt' else 'clear')  # Limpa a tela
    # Abaixo estão as opções que o cidadão terá após votar.
    opcoes = '''\n\nO que deseja visualizar agora?\n
    [ 1 ] Distribuição dos votos
    [ 2 ] Gráfico dos votos
    [ 3 ] Distribuição dos votos válidos
    [ 4 ] Gráfico dos votos válidos\n
    [ 5 ] Ir para o próximo eleitor
    [ 6 ] Finalizar votação\n'''
    opcao = ''  # String vazia receberá a opção que o usuário desejar.
    while opcao in range(1, 5) or opcao == '':  # Enquanto o usuário escolher entre 1 e 4 ele ficará vendo as opções.
        print(opcoes)   # Imprime as opções.
        opcao = int(input('\nEscolha uma das opções: '))    # Pergunta o que o usuário quer fazer.
        # Bloco de while abaixo vai garantir que o usuário digitará um número entre 1 e 6.
        while opcao not in range(1,7):
            opcao = int(input('Comando inválido. Escolha uma das opções: '))
        system('cls' if name == 'nt' else 'clear')  # Limpa a tela.
        escolha(opcao)  # Função vai retornar o que o usuário desejar. Caso seja 5 ou 6, não vai retornar nada, pois não está definido na função.
        if opcao in [5, 6]:     # Caso escolha 5 ou 6, o programa para de mostrar as opções pro usuário e vai para o próximo eleitor ou finaliza o programa.
            break
    if opcao == 6:  # Caso escolha 6, finalize o programa.
        break
    system('cls' if name == 'nt' else 'clear')  # Limpa a tela.
print('Calculando o vencedor da eleição', end='')   # Fora do programa, só resta calcular o vencedor.
for c in '.'*20:    # Adiconando o efeito de pontinhos.
    print(c, end='', flush=True)
    sleep(0.3)
print(f'\n\n{vencedor()}')      # Imprime o resultado da função vencedor.
# Definando a variável opcoes novamente pois a opção 5 será diferente.
opcoes = '''\n\nO que deseja visualizar agora?\n
    [ 1 ] Distribuição dos votos
    [ 2 ] Gráfico dos votos
    [ 3 ] Distribuição dos votos válidos
    [ 4 ] Gráfico dos votos válidos\n
    [ 5 ] Ver o vencedor novamente
    [ 6 ] Finalizar programa\n'''
opcao = ''  # Zerando a variável opcao com um string vazia.
while opcao in range(1, 6) or opcao == '':  # Enquanto o usuário escolher entre 1 e 5 ele ficará vendo as opções.
    print(opcoes)   # Imprime as opções.
    opcao = int(input('\nEscolha uma das opções: '))    # Pergunta o que o usuário quer fazer.
    # Bloco de while abaixo vai garantir que o usuário digitará um número entre 1 e 6.
    while opcao not in range(1,7):
        opcao = int(input('Comando inválido. Escolha uma das opções: '))
    system('cls' if name == 'nt' else 'clear')  # Limpa a tela.
    if opcao != 5:  # Se não for a opção 5, retonará a função escolha (distribuição e gráficos).
        escolha(opcao)
    elif opcao == 5:    # Se for a opção 5, imprime o vencedor.
        print(f'{vencedor()}')
    else:   # Se for a opção 6, finaliza o programa.
        break