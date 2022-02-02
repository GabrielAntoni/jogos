from random import shuffle


def bem_vindo():
    print('''
******************************************
******  Bem Vindo ao Roleta Russa!!*******
******************************************
''')


def bombas():
    global bomba1, bomba2
    bomba1 = []
    bomba2 = []
    for a in range(1, 21, 1):
        bomba1.append('$')
        bomba2.append(a)
    for x in range(1, 3, 1):
        bomba1.append('@')
        del bomba1[0]
    shuffle(bomba1)


def jgum():
    global bomba1, bomba2
    jogadoum = int(input(f'''jogador um ecolha uma posição:
      {bomba2[0]}  |  {bomba2[1]}  |  {bomba2[2]}  |  {bomba2[3]}  |  {bomba2[4]}
      {bomba2[5]}  |  {bomba2[6]}  |  {bomba2[7]}  |  {bomba2[8]}  |  {bomba2[9]}
      {bomba2[10]} |  {bomba2[11]} |  {bomba2[12]} |  {bomba2[13]} |  {bomba2[14]}
      {bomba2[15]} |  {bomba2[16]} |  {bomba2[17]} |  {bomba2[18]} |  {bomba2[19]}
      '''))
    if 0 >= jogadoum or 21 <= jogadoum:
        print('apenas os numeros demostrados.')
        print(jogadoum)
        jgum()
    elif bomba2[jogadoum - 1] == '*':
        print('apenas os numeros demostrados.')
        jgum()
    else:
        del bomba2[jogadoum - 1]
        bomba2.insert(jogadoum - 1, bomba1[jogadoum - 1])
        return bomba1[jogadoum - 1]


def jgdois():
    global bomba1, bomba2
    jogadodois = int(input(f'''jogador dois ecolha uma posição:
      {bomba2[0]}  |  {bomba2[1]}  |  {bomba2[2]}  |  {bomba2[3]}  |  {bomba2[4]}
      {bomba2[5]}  |  {bomba2[6]}  |  {bomba2[7]}  |  {bomba2[8]}  |  {bomba2[9]}
      {bomba2[10]} |  {bomba2[11]} |  {bomba2[12]} |  {bomba2[13]} |  {bomba2[14]}
      {bomba2[15]} |  {bomba2[16]} |  {bomba2[17]} |  {bomba2[18]} |  {bomba2[19]}
      '''))
    if 0 >= jogadodois or 21 <= jogadodois:
        print('apenas os numeros demostrados.')
        jgdois()

    elif bomba2[jogadodois - 1] == '$':
        print('apenas os numeros demostrados.')

        jgdois()
    else:
        del bomba2[jogadodois - 1]
        bomba2.insert(jogadodois - 1, bomba1[jogadodois - 1])
        return bomba1[jogadodois - 1]


def jogo():
    global bomba1, bomba2
    print(f'''
      {bomba2[0]}  |  {bomba2[1]}  |  {bomba2[2]}  |  {bomba2[3]}  |  {bomba2[4]}
      {bomba2[5]}  |  {bomba2[6]}  |  {bomba2[7]}  |  {bomba2[8]}  |  {bomba2[9]}
      {bomba2[10]} |  {bomba2[11]} |  {bomba2[12]} |  {bomba2[13]} |  {bomba2[14]}
      {bomba2[15]} |  {bomba2[16]} |  {bomba2[17]} |  {bomba2[18]} |  {bomba2[19]}
    ''')

    for a in range(0, 21, 1):
        if a % 2 == 0:
            bomba = jgum()
            print(bomba)
            if bomba == '@':
                print("jogador um explodiu o jogador dois é vitorioso!! ")
                break
        elif a % 2 == 1:
            bomba = jgdois()
            print(bomba)
            if bomba == '@':
                print("jogador dois explodiu o jogador um é vitorioso!! ")
                break


bem_vindo()
bombas()
jogo()
