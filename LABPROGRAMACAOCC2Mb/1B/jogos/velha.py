import random
robo = [O]
tabuleiro = [
[' ', ' ', ' '],
[' ', ' ', ' '],
[' ', ' ', ' ']
]

def exibe_tabuleiro(tabuleiro):
  for linha in tabuleiro:
    print('|'.join(linha))
    print('-'*5)

def movimento_humano(tabuleiro):
  while True:
    try: 
      linha = int(input('escolha uma linha entre 0 e 2: ' ))
      coluna = int(input('escolha uma coluna entre 0 e 2: '))
      if tabuleiro[linha][coluna] == '   ':
        return linha, coluna
      else:
        print('esta casa está ocupada, tene outra!')
    except (ValueError, IndexError):
      print('entrada inválida, tente novamente!')

exibe_tabuleiro(tabuleiro)

#player = 'x'
#while True:
 # print(f'turno do jogador {player}')
  #exibe_tabuleiro(tabuleiro)


def resultado(tabuleiro)
if 

      
    
