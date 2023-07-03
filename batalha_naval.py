from random import randint

# Criação do tabuleiros
tabuleiro1 = [["O"]*8 for i in range(8)]
tabuleiro2 = [["O"]*8 for i in range(8)]
tabuleiroR1 = [["A"]*8 for i in range(8)]
tabuleiroR2 = [["A"]*8 for i in range(8)]

# Função para exibir o tabuleiros
def exibir_tabuleiros (tabuleiro1, tabuleiro2):
    print("")
    print('   A  B  C  D  E  F  G  H ')
    for linha in range (len(tabuleiro1)):
        print(linha+1,end='  ')
        for coluna in range (len(tabuleiro1[0])):
            print(f'{tabuleiro1[linha][coluna]:3}',end='')
        print()
    print("")
    print('   A  B  C  D  E  F  G  H ')
    for linha in range (len(tabuleiro2)):
        print(linha+1,end='  ')
        for coluna in range (len(tabuleiro2[0])):
            print(f'{tabuleiro2[linha][coluna]:3}',end='')
        print()
    print("")

# Função para posicionar os navios aleatoriamente
def posicionar_navios(tabuleiro, num_navios):
    for i in range(num_navios):
        while True:
            linha = randint(0, 7)
            coluna = randint(0, 7)
            if validar_posicao(tabuleiro, linha, coluna):
                tabuleiro[linha][coluna] = "N"
                break
    return tabuleiro

# Função para validar a posição de um navio
def validar_posicao(tabuleiro, linha, coluna):
    for i in range(linha-1, linha+2):
        for j in range(coluna-1, coluna+2):
            if i >= 0 and i < 8 and j >= 0 and j < 8:
                if tabuleiro[i][j] == "N":
                    return False
    return True

# Conversão de LETRA para NÚMERO (coluna)
def converter_coluna (coluna):
    match coluna:
        case 'A':
            coluna = 0
        case 'B':
            coluna = 1
        case 'C':
            coluna = 2
        case 'D':
            coluna = 3
        case 'E':
            coluna = 4
        case 'F':
            coluna = 5
        case 'G':
            coluna = 6
        case 'H':
            coluna = 7
        case other:
          coluna = 10
    return coluna

# Função para os turnos de jogo
def turno1 ():
    # Leitura do tiro do primeiro jogador
    global navios_afundados1
    acertou = True
    print("\nTIRO DO JOGADOR 1: ")
    linha_tiro = int(input("Digite a linha do tiro (1-8, ou 9 para exibir frota): ")) - 1
    if linha_tiro == 8:
      exibir_tabuleiros(tabuleiroR1, tabuleiroR2)
      acertou=True
    else:
      coluna_letra = input("Digite a coluna do tiro (A-H, ou X para salvar o jogo): ").upper()
      coluna_tiro = converter_coluna(coluna_letra)
      # <---- ADIÇÃO ----
      # Salvar jogo e terminar
      if coluna_letra == 'X' or coluna_letra == 'x':
          print("Salvando jogo...")
          salvar_jogo(tabuleiro1, tabuleiro2, tabuleiroR1, tabuleiroR2, navios_afundados1, navios_afundados2)
          print("Jogo salvo.")
          exit()
        # ---- ADIÇÃO ---->
      if (linha_tiro < 0 or coluna_tiro < 0 or linha_tiro > 7 or coluna_tiro > 7):
          print("\nCaraca, marujo, você atirou fora do tabuleiro. Perdeu a vez, hein!?.")
          acertou = False
      else:
        if tabuleiroR2[linha_tiro][coluna_tiro] == "N":
            print("\nFOOOOGO! Parabéns, marujo, você acertou um navio adversário!")
            tabuleiro2[linha_tiro][coluna_tiro] = "F"
            acertou = True
            navios_afundados1 += 1
        else:
            acertou = False
            if tabuleiro1[linha_tiro][coluna_tiro] == "A" or tabuleiro1[linha_tiro][coluna_tiro] == "F":
              print("\nFicou maluco, marujo? Você já atirou nessa posição. Perdeu a vez, hein!?")
            else:
              print("\nEssa passou longe, marujo! Você errou!")
              tabuleiro2[linha_tiro][coluna_tiro] = "A"
    exibir_tabuleiros(tabuleiro1, tabuleiro2)
    return acertou

def turno2 ():
    # Leitura do tiro do primeiro jogador
    global navios_afundados2
    acertou = True
    print("\nTIRO DO JOGADOR 2: ")
    linha_tiro = int(input("Digite a linha do tiro (1-8, ou 9 para exibir frota): ")) - 1
    if linha_tiro == 8:
      exibir_tabuleiros(tabuleiroR1, tabuleiroR2)
      acertou=True
    else:
      coluna_letra = input("Digite a coluna do tiro (A-H, ou X para salvar o jogo): ").upper()
      coluna_tiro = converter_coluna(coluna_letra)
      # <---- ADIÇÃO ----
      # Salvar jogo e terminar
      if coluna_letra == 'X' or coluna_letra == 'x':
          print("Salvando jogo...")
          salvar_jogo(tabuleiro1, tabuleiro2, tabuleiroR1, tabuleiroR2, navios_afundados1, navios_afundados2)
          print("Jogo salvo.")
          exit()
        # ---- ADIÇÃO ---->
      if (linha_tiro < 0 or coluna_tiro < 0 or linha_tiro > 7 or coluna_tiro > 7):
          print("\nCaraca, marujo, você atirou fora do tabuleiro. Perdeu a vez, hein!?.")
          acertou = False
      else:
        if tabuleiroR1[linha_tiro][coluna_tiro] == "N":
            print("\nFOOOOGO! Parabéns, marujo, você acertou um navio adversário!")
            tabuleiro1[linha_tiro][coluna_tiro] = "F"
            acertou = True
            navios_afundados2 += 1
        else:
            acertou = False
            if tabuleiro1[linha_tiro][coluna_tiro] == "A" or tabuleiro1[linha_tiro][coluna_tiro] == "F":
              print("\nFicou maluco, marujo? Você já atirou nessa posição. Perdeu a vez, hein!?")
            else:
              print("\nEssa passou longe, marujo! Você errou!")
              tabuleiro1[linha_tiro][coluna_tiro] = "A"
    exibir_tabuleiros(tabuleiro1, tabuleiro2)


    exibir_tabuleiros(tabuleiro1, tabuleiro2)
    return acertou

# <---- ADIÇÃO ----
# Carregar jogo salvo
def carregar_tabuleiro(tabuleiro, nome_arquivo):
    tabuleiro = []
    with open(nome_arquivo, 'r') as file_object:
        for linha in file_object:
            linha_separada = linha
            tabuleiro.append(linha_separada.replace("\n", ""))
    return tabuleiro

# Salvar jogo
def salvar_tabuleiro(tabuleiro, nome_arquivo):
    with open(nome_arquivo, 'w') as file_object:
        for linha in tabuleiro:
            linha_separada = ''.join(linha)
            file_object.write(linha_separada + "\n")
    return tabuleiro

#Salvar navios afundados
def salvar_navios_afundados(navios_afundados, nome_arquivo):
    with open(nome_arquivo, 'w') as file_object:
        file_object.write(str(navios_afundados))

#Carregar navios afundados
def carregar_navios_afundados(nome_arquivo):
    with open(nome_arquivo, 'r') as file_object:
        navios_afundados = file_object.read()
    return int(navios_afundados) 

#Salvar número de navios
def salvar_numero_navios(numero_de_navios):
    with open('numero_de_navios', 'w') as file_object:
        file_object.write(numero_de_navios)

#Carregar número de navios
def carregar_numero_navios(nome_arquivo):
    with open(nome_arquivo, 'r') as file_object:
        numero_de_navios = file_object.read()
    return int(numero_de_navios)

#Carregar jogo
def carregar_jogo_salvo():
    global tabuleiro1, tabuleiro2, tabuleiroR1, tabuleiroR2, navios_afundados1, navios_afundados2, numero_de_navios
    tabuleiro1 = carregar_tabuleiro(tabuleiro1, 'tabuleiro1.txt')
    tabuleiro2 = carregar_tabuleiro(tabuleiro2, 'tabuleiro2.txt')
    tabuleiroR1 = carregar_tabuleiro(tabuleiroR1, 'tabuleiroR1.txt') 
    tabuleiroR2 = carregar_tabuleiro(tabuleiroR2, 'tabuleiroR2.txt')
    navios_afundados1 = carregar_navios_afundados('navios_afundados1.txt')
    navios_afundados2 = carregar_navios_afundados('navios_afundados2.txt')
    numero_de_navios = carregar_numero_navios('numero_de_navios.txt')

#Salvar jogo
def salvar_jogo(tabuleiro1, tabuleiro2, tabuleiroR1, tabuleiroR2, navios_afundados1, navios_afundados2):
    tabuleiro1 = salvar_tabuleiro(tabuleiro1, 'tabuleiro1.txt')
    tabuleiro2 = salvar_tabuleiro(tabuleiro2, 'tabuleiro2.txt')
    tabuleiroR1 = salvar_tabuleiro(tabuleiroR1, 'tabuleiroR1.txt')
    tabuleiroR2 = salvar_tabuleiro(tabuleiroR2, 'tabuleiroR2.txt')
    navios_afundados1 = salvar_navios_afundados(navios_afundados1, 'navios_afundados1.txt')
    navios_afundados2 = salvar_navios_afundados(navios_afundados2, 'navios_afundados2.txt')

#Iniciar novo jogo
def iniciar_jogo_novo():
    numero_de_navios = int(input("Digite a quantidade de navios desejados (máximo 6): "))
    while numero_de_navios > 6:
        print("O número de navios não pode ser maior que 6! Digite novamente.")
        numero_de_navios = int(input("Digite a quantidade de navios desejados (máximo 6): "))

    # Posiciona os navios aleatoriamente, verificando adjacências e diagonais próximas
    posicionar_navios(tabuleiroR1, numero_de_navios)
    posicionar_navios(tabuleiroR2, numero_de_navios)
    venceu1 = False
    venceu2 = False
    exibir_tabuleiros(tabuleiro1, tabuleiro2)

    while navios_afundados1 < numero_de_navios  or navios_afundados2 < numero_de_navios:
        primeiro_acertou = True
        segundo_acertou = True
        while primeiro_acertou:
            if navios_afundados1 == numero_de_navios:
              venceu1 = True
              break
            elif not turno1():
                primeiro_acertou = False
        if venceu1:
            break
        while segundo_acertou:
            if navios_afundados2 == numero_de_navios:
              venceu2 = True
              break
            elif not turno2():
                segundo_acertou = False
        if venceu2: break

    if venceu1:
      print("\nFim de jogo! Parabéns, jogador 1, você ganhou!. Obrigado por jogarem, marujos!")
    elif venceu2:
      print("\nFim de jogo! Parabéns, jogador 2, você ganhou!. Obrigado por jogarem, marujos!")
    else:
        print("\nAlgum erro aconteceu, por favor, reinicie o jogo.")

def iniciar_jogo_salvo():
    venceu1 = False
    venceu2 = False
    carregar_jogo_salvo()
    exibir_tabuleiros(tabuleiro1, tabuleiro2)
    while navios_afundados1 < numero_de_navios  or navios_afundados2 < numero_de_navios:
        primeiro_acertou = True
        segundo_acertou = True
        while primeiro_acertou:
            if navios_afundados1 == numero_de_navios:
              venceu1 = True
              break
            elif not turno1():
                primeiro_acertou = False
        if venceu1:
            break
        while segundo_acertou:
            if navios_afundados2 == numero_de_navios:
              venceu2 = True
              break
            elif not turno2():
                segundo_acertou = False
        if venceu2: break

    if venceu1:
      print("\nFim de jogo! Parabéns, jogador 1, você ganhou!. Obrigado por jogarem, marujos!")
    elif venceu2:
      print("\nFim de jogo! Parabéns, jogador 2, você ganhou!. Obrigado por jogarem, marujos!")
    else:
        print("\nAlgum erro aconteceu, por favor, reinicie o jogo.")
# ---- ADIÇÃO ---->

# JOGO
print("Bem-vindo ao Jogo de Batalha Naval!")
print("Afunde todos os navios adversários para ganhar.")

# <---- ADIÇÃO ----
novo_jogo = input("Novo jogo? (S/N): ").upper()
if novo_jogo == 'N':
   print("Carregando jogo anterior...")
   print("Jogo carregado.")
   iniciar_jogo_salvo()
elif novo_jogo == 'S':
    navios_afundados1 = 0
    navios_afundados2 = 0
    iniciar_jogo_novo()