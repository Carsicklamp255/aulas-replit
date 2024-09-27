'''
sets - é uma coleção não ordenada, não-indexada e não duplicada.
'''

frutas = {'uva', 'maça', 'morango'}

print(frutas)
print(type(frutas))

coisas = {10,1, 2, 3, 4, 5, 6, 7, 8, 9, "abacaxi", True,}
print(coisas)


coisas.add("novo item")
for c in coisas:
print(c)

minhas_compras = {"carne", "coração de galinha", "coca"}
compras_amigo = {"cerveja", "carvão", "gelo"}

minhas_compras.update(compras_amigo)

for item in minhas_compras:
  print(item)

minhas_compras.remove("coraçãp de galinha")

compras_amigo.discard("carvão")
for item in minhas_compras: 
  print(item)

#conjuntos 
alunos_gp1 = {"joão", "maria", "jorge", "antonio"}

alunos_gp2 = {'clara', 'ronaldo' 'pedro', 'caio'}

alunos_gp = alunos_gp1.union(alunos_gp2)

print(alunos_gp)

alunos_2grupos = alunos_gp1.intersection(alunos_gp2)

print(alunos_2grupos)