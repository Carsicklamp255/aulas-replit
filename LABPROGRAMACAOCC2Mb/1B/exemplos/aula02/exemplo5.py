#strings

x = 'assim'
y = "assim"
if x == y.casefold():
 print("iguais")




  #slicing
  
  x = "wagner Perin"

  print(x[7:])

print(x.upper())
print(x.strip())

x = "wagner perin"
y = x.replace("W", "V")

print(x)
print(y)

nomes = "Wagner Carlos Andre"
alunos = nomes.split(" ")

print(alunos)

nome = "Wagner"
sobrenome = "Perin"

nome_completo = nome + " " + sobrenome 
print(nome_completo)

#strings formatadas
idade = 19
nome = "gabriel barreto"

saida = f"O {nome} tem {idade} anos"


print(saida)

produto = "pizza"
preco = 40.00

saida = f"O produto {produto} custa R$ {preco:.2f}"

#escapes

frase = 'e o nicolas disse: \n "nao vai dar!""' \\

print(frase)