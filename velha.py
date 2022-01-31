def bem_vindo():
    print('*' * 39)
    print('**** Bem vindo ao jogo da velha!!! ****')
    print('*' * 39)
    y = input("Deseja escolher o nome dos jogadores?(digite 's' se sim) \n")
    jogadores(y)
def jogadores(y):
    global jogador1, jogador2
    if y.upper() == 'S':
        jogador1 = input('coloque o nome do primeiro jogador: ')
        jogador2 = input('coloque o nome do segundo jogador: ')
        simbolos()
    else:
        jogador1 = 'jogador1'
        jogador2 = 'jogador2'
        simbolos()
def simbolos():
    global js1, js2
    y = input("deseja escolher os simbolos dos jogadores?(digite 's' se sim) \n")
    if y.upper() == 'S':
        js1 = input('coloque o simbolo do primeiro jogador: ')
        js2 = input('coloque o simbolo do segundo jogador: ')
        if len(js1) >= 2 or len(js2) >= 2:
            print('Coloque apenas 1 simbolo!')
            simbolos()
        elif js1 == js2:
            print('Os simbolos devem ser diferentes!')
            simbolos()
    else:
        js1 = 'X'
        js2 = 'O'


def mapa(velha):
    for elemento in range(len(velha)):
        del velha[elemento]
        velha.insert(elemento, elemento + 1)


def jogo():
    velha = []
    for a in range(1, 10, 1):
        velha.append(a)
    print('**** jogo da velha ***')
    print(f'''
        {velha[0]} | {velha[1]} | {velha[2]}  
        {velha[3]} | {velha[4]} | {velha[5]}  
        {velha[6]} | {velha[7]} | {velha[8]}  ''')
    for e in range(0, 9, 1):
        if e % 2 == 0:
            playerx(velha)
        elif e % 2 == 1:
            playero(velha)
        v = verificacao(velha)
        if v == 1:
            break
        if e == 8:
            print('-----====Empate====-----')
    print(f'''
        {velha[0]} | {velha[1]} | {velha[2]}  
        {velha[3]} | {velha[4]} | {velha[5]}  
        {velha[6]} | {velha[7]} | {velha[8]}  ''')
    repetcao(velha)


def repetcao(velha):
    global jogador1, jogador2
    rep = input('''Deseja repetir o jogo?
(1) Sim
(2) Não
(3) renomear jogadores
''')
    if rep == '1':

        mapa(velha)
        jogo()
    elif rep == '2':
        print('obrigado por usar o programa.')
    elif rep == '3':
        y = 'S'
        jogadores(y)

        jogo()
    else:
        repetcao(velha)


def playerx(velha):
    x = int(input(f'''{jogador1} qual posição:
    {velha[0]} | {velha[1]} | {velha[2]}  
    {velha[3]} | {velha[4]} | {velha[5]}  
    {velha[6]} | {velha[7]} | {velha[8]}
'''))
    if 0 <= x >= 10:
        print('apenas os numeros demostrados.')
        print('b')
        playerx(velha)

    elif velha[x - 1] == js2:
        print('apenas os numeros demostrados.')

        playerx(velha)

    elif velha[x - 1] == js1:
        print('apenas os numeros demostrados.')

        playerx(velha)
    else:
        del velha[x - 1]
        velha.insert(x - 1, js1)


def playero(velha):
    o = int(input(f'''{jogador2} qual posição:
    {velha[0]} | {velha[1]} | {velha[2]}  
    {velha[3]} | {velha[4]} | {velha[5]}  
    {velha[6]} | {velha[7]} | {velha[8]}
'''))
    if 0 <= o >= 10:
        print('apenas os numeros demostrados.')

        playero(velha)

    elif velha[o - 1] == js2:
        print('apenas os numeros demostrados.')

        playero(velha)
    elif velha[o - 1] == js1:
        print('apenas os numeros demostrados.')

        playero(velha)
    else:
        del velha[o - 1]
        velha.insert(o - 1, js2)


def verificacao(velha):
    if velha[0] == js1 and velha[1] == js1 and velha[2] == js1:
        print(f'{jogador1} ganhou!')
        return 1
    elif velha[3] == js1 and velha[4] == js1 and velha[5] == js1:
        print(f'{jogador1} ganhou!')
        return 1
    elif velha[6] == js1 and velha[7] == js1 and velha[8] == js1:
        print(f'{jogador1} ganhou!')
        return 1
    elif velha[0] == js1 and velha[3] == js1 and velha[6] == js1:
        print(f'{jogador1} ganhou!')
        return 1
    elif velha[1] == js1 and velha[4] == js1 and velha[7] == js1:
        print(f'{jogador1} ganhou!')
        return 1
    elif velha[2] == js1 and velha[5] == js1 and velha[8] == js1:
        print(f'{jogador1} ganhou!')
        return 1
    elif velha[0] == js1 and velha[4] == js1 and velha[8] == js1:
        print(f'{jogador1} ganhou!')
        return 1
    elif velha[2] == js1 and velha[4] == js1 and velha[6] == js1:
        print(f'{jogador1} ganhou!')
        return 1
    elif velha[0] == js2 and velha[1] == js2 and velha[2] == js2:
        print(f'{jogador2} ganhou!')
        return 1
    elif velha[3] == js2 and velha[4] == js2 and velha[5] == js2:
        print(f'{jogador2} ganhou!')
        return 1
    elif velha[6] == js2 and velha[7] == js2 and velha[8] == js2:
        print(f'{jogador2} ganhou!')
        return 1
    elif velha[0] == js2 and velha[3] == js2 and velha[6] == js2:
        print(f'{jogador2} ganhou!')
        return 1
    elif velha[1] == js2 and velha[4] == js2 and velha[7] == js2:
        print(f'{jogador2} ganhou!')
        return 1
    elif velha[2] == js2 and velha[5] == js2 and velha[8] == js2:
        print(f'{jogador2} ganhou!')
        return 1
    elif velha[0] == js2 and velha[4] == js2 and velha[8] == js2:
        print(f'{jogador2} ganhou!')
        return 1
    elif velha[2] == js2 and velha[4] == js2 and velha[6] == js2:
        print(f'{jogador2} ganhou!')
        return 1

bem_vindo()
jogo()
