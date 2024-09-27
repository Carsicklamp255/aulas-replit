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

matriz = criar_matriz(quant_linhas, quant_colunas)

imprimir_matriz(matriz)

