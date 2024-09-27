def criar_matriz(quant_linhas, quant_colunas):
    matriz = [[0 for i in range(quant_colunas)]for j in range(quant_linhas)]

    for li in range(quant_linhas):
       for c in range(quant_colunas):
          matriz[li][c] = int(input(f'Digite o valor para [{li},{c}]: '))

    return matriz

def imprimir_matriz(matriz):
    print('-=' * 30)
    for linha in matriz:
      for valor in linha:
         print(f'[{valor:^5}]', end='')
      print()
    print('-=' * 30)

quant_linhas = int(input("Qual o número de linhas? "))
quant_colunas = int(input("Qual o número de colunas? "))

def e_matriz_identidade(matriz):
    n = len(matriz)
    if n != len(matriz[0]):
        return False

    for i in range(n):
        for j in range(n):
            if i == j and matriz[i][j] != 1 or i != j and matriz[i][j] != 0:
                return False
                
    return True

def e_matriz_nula(matriz):
 for linha in matriz:
     for valor in linha:
         if valor != 0:
             return False
 return True

def e_matriz_simetrica(matriz):
    if quant_colunas != quant_linhas:
        return False

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True

def e_matriz_esparsa(matriz):
    T_elementos = len(matriz) * len(matriz[0])
    diferrente_de_zero = sum(1 for linha in matriz for valor in linha if valor != 0)
    return diferrente_de_zero < T_elementos / 2

def imprimir_diagonal(matriz):
    diagonal = []
    
    for i in range(min(len(matriz), len(matriz[0]))):
        diagonal.append(matriz[i][i])
        
    print(f"valores da diagonal: [{', '.join(map(str, diagonal))}]")
        
def calcular_traco(matriz):
    soma = 0
    for i in range(min(len(matriz), len(matriz[0]))):
        soma += matriz[i][i]
    return soma

matriz = criar_matriz(quant_linhas, quant_colunas)

def soma_lihas(matriz):
    linhas_soma = [sum(linha) for linha in matriz]
    print(f"a soma das linhas é: {linhas_soma}")

def soma_colunas(matriz):
    colunas_soma = [sum(matriz[i][j] for i in range(len(matriz))) for j in range(len(matriz[0]))]
    print(f"a soma das colunas é: {colunas_soma}")

imprimir_matriz(matriz)

soma_lihas(matriz)
soma_colunas(matriz)

if e_matriz_nula(matriz):
    print("é nula")
else:
    print("não é nula")

if e_matriz_identidade(matriz):
    print('é identidade')

else:
    print('não é identidade')

if e_matriz_esparsa(matriz):
    print("é esparsa")

else:
    print("não é esparsa")

if quant_linhas == quant_colunas:
    imprimir_diagonal(matriz)
    print(f"A soma dos valores da diagonal é: {calcular_traco(matriz)}")

resposta = input("Você deseja calcular a multiplicação escalar da matriz? responda apenas com 'sim' ou 'não'")
if resposta.lower() == 'sim':
     def multiplicar_escalar(matriz, escalar):
        matriz_resultado_escalar = []
        for linha in matriz:
           nova_matriz = [valor * escalar for valor in linha]
           matriz_resultado_escalar.append(nova_matriz)

        return matriz_resultado_escalar

     escalar = int(input("qual o valor você deseja usar para multiplicar a matriz? "))
     matriz_resultado_escalar = multiplicar_escalar(matriz, escalar)
     for linha in matriz_resultado_escalar:
          print(linha)

else:
    print("ok")

resposta1 = input("Você deseja rotacinar a matriz? responda apenas com 'sim' ou 'não'")
if resposta1.lower() == 'sim':
    def rotacionar_matriz_90(matriz):
        matriz_transposta = [list(row) for row in zip(*matriz)]
        for linha in matriz_transposta:
            linha.reverse()
        return matriz_transposta

    matriz_rotacinada = rotacionar_matriz_90(matriz)

    imprimir_matriz(matriz_rotacinada)
else:
    print("ok")