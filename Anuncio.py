from time import sleep

def Inicial(msg):
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)

def Escolhas():
    print('''[1] Pedra
[2] Papel
[3] Tesoura
[0] Sair do Programa''')

def Resultados(vitorias, empates, derrotas):
    Inicial('RESULTADOS:')
    print(f'Vitórias: {vitorias}')
    print(f'Empates: {empates}')
    print(f'Derrotas: {derrotas}')
    print('-' * 40)
    print('ENCERRANDO O PROGRAMA...'.center(40))
    sleep(1)
