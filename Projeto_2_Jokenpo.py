# A biblioteca 'rich' precisa ser instalada anteriormente no seu computador pelo terminal de sua preferência com o comando "pip install rich". Após instalada, ela pode ser importada para o projeto
from os import system # Biblioteca para limpar a tela durante a execução do código
from random import randint # Biblioteca para gerar números aleatórios (servirá para sortear pedra, papel ou tesoura para o computador)
from time import sleep # Biblioteca para fazer colocar tempo entre execução de linhas de código
from rich import print # Biblioteca para melhorar o print, colocando cores, itálico, negrito, etc
system('cls') # Inicia o programa limpando a tela
print('''\n[italic red]Bem-vindo ao JOKENPÔ.[/italic red]
\nSerá que você consegue vencer o computador?
Tente a sorte!''')
sleep(3)
# Declarando as variáveis no início para o código ficar mais limpo
pedra = 'Pedra ✊'
papel = 'Papel ✋'
tesoura = 'Tesoura ✌'
nome = input('\n\nDiga-me o seu nome: ').capitalize() # O programa sempre chamará o usuário pelo nome
while True:
    vitoriasUser = vitoriasComp = 0 # Contadores de vitórias do usuário e do computador
    rodadas = int(input('Você quer fazer quantas rodadas? '))
    # Esse bloco de 'while' serve para garantir que o usuário escolherá um número maior que 0
    while rodadas < 1:
        rodadas = int(input('Quantidade inválida. Digite um número maior que 0: '))
    system('cls') # Limpa a tela
    for i in range(rodadas): # Esse 'for' fará todas as rodadas declaradas pelo usuário
        print('[red]------------ JOKENPÔ ------------[/red]')
        print(f'''\nRodada {i+1}:\n
    [ 1 ] {pedra}
    [ 2 ] {papel}
    [ 3 ] {tesoura}''')
        user = int(input('\nEscolha a sua jogada: ')) # Usuário escolhe 1, 2 ou 3, entre Pedra, Papel ou Tesoura, respectivamente
        # Esse bloco de 'while' serve para garantir que o usuário escolherá entre 1, 2 e 3
        while not (1 <= user <= 3):
             user = int(input('Opção inválida. Escolha novamente: '))
        comp = randint(1,3) # Aleatoriamente o computador escolhe
        sleep(0.2)
        print('[red]JO[/red]')
        sleep(0.4)
        print('[red]KEN[/red]')
        sleep(0.4)
        print('[red]PÔ![/red]\n')
        sleep(0.4)
        print('=-' *18)
        # Nesse bloco de 'if' estão todas as possibilidades para quando o usuário escolhe Pedra
        if user == 1:
            if comp == 1: # Computador escolhe Pedra
                print(f'\nComputador jogou {pedra}\n{nome} jogou {pedra}\n\n[bold]EMPATE![/bold]\n')
            if comp == 2: # Computador escolhe Papel
                print(f'\nComputador jogou {papel}\n{nome} jogou {pedra}\n\n[bold]COMPUTADOR VENCEU![/bold]\n')
                vitoriasComp += 1
            if comp == 3: # Computador escolhe Tesoura
                print(f'\nComputador jogou {tesoura}\n{nome} jogou {pedra}\n\n{nome.upper()} VENCEU!\n')
                vitoriasUser += 1
        # Nesse bloco de 'if' estão todas as possibilidades para quando o usuário escolhe Papel
        if user == 2:
            if comp == 2: # Computador escolhe Papel
                print(f'\nComputador jogou {papel}\n{nome} jogou {papel}\n\n[bold]EMPATE![/bold]\n')
            if comp == 3: # Computador escolhe Tesoura
                print(f'\nComputador jogou {tesoura}\n{nome} jogou {papel}\n\n[bold]COMPUTADOR VENCEU![/bold]\n')
                vitoriasComp += 1
            if comp == 1: # Computador escolhe Papel
                print(f'\nComputador jogou {pedra}\n{nome} jogou {papel}\n\n{nome.upper()} VENCEU!\n')
                vitoriasUser += 1
        if user == 3:
        # Nesse bloco de 'if' estão todas as possibilidades para quando o usuário escolhe Papel
            if comp == 3: # Computador escolhe Tesoura
                print(f'\nComputador jogou {tesoura}\n{nome} jogou {tesoura}\n\n[bold]EMPATE![/bold]\n')
            if comp == 1: # Computador escolhe Pedra
                print(f'\nComputador jogou {pedra}\n{nome} jogou {tesoura}\n\n[bold]COMPUTADOR VENCEU![/bold]\n')
                vitoriasComp += 1
            if comp == 2: # Computador escolhe Papel
                print(f'\nComputador jogou {papel}\n{nome} jogou {tesoura}\n\n{nome.upper()} VENCEU!\n')
                vitoriasUser += 1
        print('=-' *18)
        # Nesse bloco de 'if' aparece o placar, exceto na última rodada (para fazer um suspense)
        if i != rodadas - 1:
            print(f'''\n[red]PONTUAÇÃO[/red]
    Computador 💻 {vitoriasComp} x {vitoriasUser} 😀 {nome}\n''')
            print('=-' *18)
            proximaRodada = input('\nQuando você estiver pronto para a próxima rodada, digite "P": ').strip().upper() # Para o jogo ficar mais organizado, pedi ao usuário para apertar "P" para ir para a próxima rodada
            # Esse bloco de 'while' serve para garantir que o usuário escolherá "P"
            while not proximaRodada.startswith('P'):
                proximaRodada = input('Não entendi o que você quis dizer.\nDigite "P" quando estiver pronto: ').strip().upper()
            system('cls') # Limpa a tela
    print('\n[bold]Final de jogo![/bold]') # Esse print aparece aparece apenas na última rodada, pois está fora do 'for' das rodadas
    sleep(4)
    print('\n[italic red]O grande campeão é[/italic red]', end='') # O próximo 'print' será executado ao lado desse graças ao " end='' "
    # Esse bloco de 'for' serve para ir acrescentando pontos ao 'print' anterior, para fazer o suspense
    for a in range(10):
        print('[red].[/red]', end='', flush=True) # Parâmetro 'flush=True' para que cada ponto seja impresso um após o outro. Se eu não colocasse, o programa esperaria todos os índices do 'for' serem executados e imprimiria um bloco de pontos de uma só vez
        sleep(0.4)
    system('cls') # Limpa a tela
    # Esse bloco de 'if', 'elif' e 'else' serve para verificar quem foi o campeão
    if vitoriasComp == vitoriasUser:
        print('\n    [italic red]PARTIDA EMPATADA![/italic red]\n\nParabéns aos dois jogadores pela incrível partida!\n')
    elif vitoriasUser > vitoriasComp:
        print(f'    \n[italic red]{nome.upper()} É O CAMPEÃO!!![/italic red]\n\nDessa vez você conseguiu vencer, mas sua sorte não vai perdurar...\n')
    else:
        print(f'\n    [italic red]COMPUTADOR É O CAMPEÃO!!![/italic red]\n\n{nome}, você precisará treinar muito mais para vencê-lo!\n')
    print('=-' *18)
    print(f'''\n[red]RESULTADO FINAL:[/red]
    Computador 💻 {vitoriasComp} x {vitoriasUser} 😀 {nome}\n''')
    print('=-' *18)
    sleep(3)
    novoJogo = input('\nVocê quer jogar novamente? [S/N] ').strip().upper()[0]
    # Esse bloco de 'while' serve para garantir que o usuário escolherá "S" ou "N" na pergunta anterior
    while novoJogo not in 'SN':
        novoJogo = input('Opção inválida. Escolha novamente: [S/N] ').strip().upper()[0]
    if novoJogo == 'S': # Se a resposta for SIM, pergunta se quer trocar o nome do jogador
        novoNome = input(f'Quer trocar o nome do jogador? [S/N] ').strip().upper()[0]
        # Esse bloco de 'while' serve para garantir que o usuário escolherá "S" ou "N" na pergunta anterior
        while novoNome not in 'SN':
            novoNome = input(f'Opção inválida. Escolha novamente: [S/N] ').strip().upper()[0]
        system('cls') # Limpa a tela
        if novoNome == 'S': # Se a resposta for SIM, pergunta o nome do jogador
            nome = input('\nDiga-me o seu nome: ').capitalize()
    else: # Se a resposta ao novo jogo for NÃO, o programa agradece pelo jogo, limpa a tela e finaliza
        print('\n[italic]Obrigado por jogar![/italic]')
        sleep(2)
        system('cls') # Limpa a tela
        break
