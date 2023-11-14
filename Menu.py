from Menu import *
from Anuncio import *
from Computador import *

vitorias = 0
empates = 0
derrotas = 0

cores = {'erro': '\033[1:31m', 'amarelo': '\033[33m',
         'azul': '\033[34', 'padrao': '\033[m'}

opcoes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

Inicial('JOKENPO')

while True:
    Computador = jogadaComputador()
    Escolhas()

    try:
        Jogador = int(input('Escolha: '))

    except (ValueError, TypeError):
        print(f'{cores["erro"]}Erro! Escolha um número inteiro válido!')
        continue
    else:

        if Jogador == 0:
            Resultados(vitorias, empates, derrotas)
            quit()
        
        if Jogador not in opcoes:
            print(f'{cores["erro"]}Erro! Escolha um número inteiro válido!')
            continue

        if Jogador == 1 or Jogador == 2 or Jogador == 3:
            print('-' * 40)
            print(f'''Jogador escolheu {opcoes[Jogador]}
    Computador escolheu: {opcoes[Computador]}''')
            print('-' * 40)

            if Jogador == Computador:
                print('EMPATE!')
                empates += 1

            elif Jogador == 1:

                if Computador == 2:
                    print('Computador WIN!')
                    derrotas += 1

                if Computador == 3:
                    print('Jogador WIN!')
                    vitorias += 1

            elif Jogador == 2:
                        
                if Computador == 1:
                    print('Jogador WIN!')
                    vitorias += 1

                if Computador == 3:
                    print('Computador WIN!')
                    derrotas += 1

            elif Jogador == 3:
                        
                if Computador == 1:
                    print('Computador WIN!')
                    derrotas += 1

                if Computador == 2:
                    print('Jogador WIN!')
                    vitorias += 1

        else:
            print(f'{cores["erro"]}ERRO! Escolha uma opção válida!')
            continue
    print('-' * 40)
  
