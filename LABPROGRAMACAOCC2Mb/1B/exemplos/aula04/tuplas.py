'''
tuplas - é uma coleção não ordenada, não modificavel e que permite duplicatas.
'''
frutas = ('uva', 'maça' , 'morango')

print(frutas)
print(type(frutas))

print (frutas[2])

if "uva in frutas":
  print("com ou sem semente.")
else:
  print("sem semente.")

frutas = list(frutas)
print(frutas)
print(type(frutas))

frutas[2] = "tomate"
print(frutas)

frutas = tuple(frutas)
print(frutas)
print (type(frutas))

minhas_compras = ("carne" , "coração de galinha" "coca")

compras_amigo = ("cerveja" , "carvão", "gelo")

compras_da_festa = minhas_compras + compras_amigo

print(compras_da_festa)

carros = ('cerrato' , 'gol' , 'uno')
#(c1, c2, c3) = carros 

#print(c1)
#print(c2)
#print(c3)


#for c in carros:
  #print(c)

#for i in range(len(carros)):
 # print(carros[i])

carros = carros * 2

for c in carros:
  print(c)

print(carros.count("cerato"))
print(carros.index("cerato"))

