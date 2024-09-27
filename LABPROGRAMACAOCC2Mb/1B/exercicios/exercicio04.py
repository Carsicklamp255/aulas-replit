#1) crie uma função chamada "divisao_segura" que receba dois números como arguemtos, calcule e retorne a divisão deles. caso o divsor seja zero, emita uma mensagem de erro.

#2) escreva uma função chamada "calculo_salario" qye aceite o salario base de um funcionario, um bonus opcional(com valor padrão zero), e um numero cariavél de deduções. A função deve calcular e retornar final de um funcionário.

def divisao_segura(n1, n2):
  
  if n1/n2 == 0:
    print("não é possível dividir por zero")






def divisao_segura(a, b):
  if b!= 0:
    return a/b
  else:
    raise Exception("não tem como dividir por zero")

try:
  print(divisao_segura(10, 0))

except Exception as e:
  print("aconteceu o seguinte erro:" + repr(e))


print(divisao_segura(10,5))