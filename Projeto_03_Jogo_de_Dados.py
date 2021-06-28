from os import system               # Limpar o console.
from random import choices          # Sorteia aleatoriamente uma lista de valores com reposição numa amostra.
from time import sleep              # Pausa entre uma linha e outra.
from rich import print              # Cores e emojis no print.
from art import tprint, text2art    # Converte texto para ASCII Art.

system('cls')   # Inicia limpando a tela.
# Cabeçalho até a linha 13.
casino = text2art('$$$    CASINO   BLUE    $$$')
print(f'\n[blue]{casino}[/blue]')
print('''\n🎲♣🎲♦🎲♠🎲♥ Bem-vindo ao [bold blue]Casino Blue![/bold blue] ♥🎲♠🎲♦🎲♣
Aqui você terá a oportunidade de levar para casa uma grande bolada!
Se você tiver [italic]sorte...[/italic]\n\n''')
sleep(3) # Pausa de 3 segundos.
# Regras do jogo até a linha 26.
print('''[italic red]▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▖ REGRAS ▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▖[/italic red]\n
O jogo realizado nessa mesa será o de 🎲🎲 DADOS 🎲🎲\n
✔️ Para uma partida precisamos de 4 jogadores.
✔️ Decidam entre si quem será o Jogador 1, Jogador 2, Jogador 3 e Jogador 4.
✔️ Na próxima tela, vocês escolherão a quantidade de rodadas que terá a partida.
✔️ Nosso sistema sorteará os 4 dados aleatoriamente.
✔️ O jogador com o dado de maior número será o vencedor da rodada.
✔️ Caso a rodada fique empatada, todos os jogadores que obtiveram o maior valor pontuarão.
✔️ Façam suas apostas para o 1º lugar 🏆, considerando casos de empate.
✔️ Após todas as rodadas serem efetuadas, vocês conhecerão o grande campeão.
✔️ Torça muito!''')
sleep(3)
# Pergunto ao usuário se ele está pronto, assim o jogo não fica automática demais.
continuar = input('\n\n\nQuando vocês estiverem prontos digite "P": ').strip().upper()[0]
while continuar != 'P': # Bloco de while garante que o jogo só avançará se o usuário teclar 'P'.
    continuar = input('Ainda não estão prontos? Digite "P" quando estiverem prontos: ').strip().upper()[0]
while True:
    system('cls')
    rodadas = int(input('\n\nQuantas rodadas vocês desejam fazer? '))   # Pergunta ao usuário quantas rodadas serão feitas.
    while rodadas < 1:  # Bloco de while garante que o usuário digitará um número maior que 0.
        rodadas = int(input('Quantidade inválida. Digite um número maior que 0: '))
    system('cls')
    vitorias = [0,0,0,0]    # Variável usada para contar as vitórias de cada um dos 4 jogadores.
    # Nesse bloco de for serão feitas todas as rodadas pedidas pelo usuário.
    for i in range(rodadas):
        rodada = text2art(f'RODADA#{i+1}', font='block')
        contagem = ["3...", "2...", "1..."]    # Variável declarada para fazer o efeito de contagem em ASCII Art.
        print(f'[red]{rodada}[/red]\n')
        sleep(1)
        # Nesse bloco de for será feita a contagem declarada acima, aparecendo cada item um a um.
        for c in contagem:  
            tprint(c)
            sleep(1)
        system('cls')
        jogadores = dict()  # Esse dicionário vai armazenar os dados de cada jogador em cada rodada.
        jogadas = choices(range(1,7), k=4)  # Comando choices gerará 4 números aleatórios entre 1 e 7, exclusive.
        # Nesse bloco de for serão armazenados os valores gerados pelo choices nas chaves do dicionario de cada jogador.
        for j in range(1,5):
            jogadores[j] = jogadas[j-1]
        print(f'\n[red]{text2art("RESULTADO:")}[/red]\n')
        sleep(1)
        # Nesse bloco de for o dicionário será organizado em ordem decrescente em relação ao valor do dado.
        for index, valor in sorted(jogadores.items(), key=lambda x: x[1], reverse=True):
            # Esse bloco de if e else servirá para adicionar uma unidade aos index dos jogadores com maior valor na variável vitória.
            if valor == max(jogadas):
                vitorias[index-1] += 1
                print(f'✔️ [green]+1 PONTO PARA O JOGADOR {index}![/green] O 🎲 caiu em {valor}.')
            else: # Se não foi o maior valor, simplesmente mostra na tela
                print(f'O 🎲 do Jogador {index} caiu em {valor}.')
            sleep(1)
        # Esse bloco de if serve para mostrar informações diferentes na tela caso seja a última rodada.
        if i < rodadas - 1:
            continuar = input('\n\n\nQuando vocês estiverem prontos para a próxima rodada digite "P": ').strip().upper()[0]
            while continuar != 'P': # Bloco de while garante que o jogo só avançará se o usuário teclar 'P'.
                continuar = input('Ainda não estão prontos? Digite "P" quando estiverem prontos: ').strip().upper()[0]
            system('cls')
        else:   # Se for a última rodada vai mostrar que é final de jogo.
            sleep(1)
            print(f'\n\n[red]{text2art("FINAL DE JOGO!", font="larry3d")}[/red]')
            sleep(1.5)
            print('\n\n\nSomando os pontos de todos os jogadores', end='')
            sleep(.5)
            # Esse bloco de for é apenas para aparecer pontinhos na tela, para fazer um suspense.
            for k in '.'*10:
                print(k, end='', flush=True)    # Parâmetro flush serve garantir que aparecerá os pontos um após o outro.
                sleep(.5)
    system('cls')
    vencedores = list()    # Essa variável armazenará o index de todos os vencedores
    # Bloco de for utilizando o enumerate para comparar o número de vitórias de cada jogador com o max(vitorias) e adiconando seu index à variável 'vencedores '.
    for index, valor in enumerate(vitorias):
        if valor == max(vitorias):          
            vencedores.append(index+1)
    vitoria = '1 vitória' if max(vitorias) == 1 else f'{max(vitorias)} vitórias'    # Garantinando o plural na palavra 'vitória', caso seja maior que 1.
    # Bloco de if, elife e else, para mostrar na tela todos os vencedores, independete de quantos tenham sido.
    if len(vencedores) == 1:    # Caso só tenha 1 vencedor.
        print(f'\n[italic red]Com {vitoria}, o grande campeão 🏆 é.....[/italic red]\n')
        sleep(2)
        tprint(f'Jogador   {vencedores[0]}')
    elif len(vencedores) == 2:  # Caso tenha 2 vencedores.
        print(f'\n[italic red]Foi uma partida muuuito acirrada... Com {vitoria} cada, os vencedores 🏆 são:[/italic red]')
        sleep(2)
        tprint(f'Jogador   {vencedores[0]}\nJogador   {vencedores[1]}')
    elif len(vencedores) == 3:  # Caso tenha 3 vencedores.
        print(f'\n[italic red]Foi uma partida muuuito acirrada... Com {vitoria} cada, os vencedores 🏆 são:[/italic red]')
        sleep(2)
        tprint(f'Jogador   {vencedores[0]}\nJogador   {vencedores[1]}\nJogador   {vencedores[2]}')  
    else:   # Caso tenha 4 vencedores.
        print(f'\n[italic red]Essa foi uma partida incrível!!! Com {vitoria} cada, os 4 jogadores......[/italic red]')
        sleep(2)
        tprint('EMPATARAM!')
    continuar = input('\n\n\nDeseja jogar novamente? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':    # Bloco de while garante que o usuário teclará "S" ou "N"
        continuar = input('Comando inválido. Digite novamente: [S/N] ').strip().upper()[0]
    if continuar == 'N':    # Se teclar "N", o programa agradece, limpa a tela e finaliza
        sleep(1)
        print('[italic]\n\nObrigado por jogar![/italic]')
        sleep(3)
        system('cls')
        break
    system('cls')