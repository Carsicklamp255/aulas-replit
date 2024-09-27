'''
dictionaries - usados para armazenar pares chaves ->valor.
*é uma coleção ordenada, modifícalvel, não-indexada e não aceita duplicatas.
'''

carro = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}

print(carro)
print(type(carro))

print("o modelo do carro é: " +carro["modelo"])
carro["ano"] = 1970
print(carro)

print(len(carro))

carro["cor"] = "azul"
print(carro.get)

chaves = carro.keys()
valores = carro.values()
print(chaves)

print(chaves)
print(valores)

items = carro.items()

print(items)


carro["cores_disponiveis""] = ["preto", "branco", "azul"]
print(carro)

#carro["placa"] = "ABC-1234"

if "placa" in carro:
print("eu sei a placa")
else:
print("não sei a placa")

#carro["ano"] = 2000

carro.updade({"ano": 2000})
print(carro)

del carro["ano"]

for p in carro:
  print(p)

for p in carro:
  print(p + " - " + str(carro[p]))

for 