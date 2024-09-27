nomes = ["gabriel", "arthur", "antonio"]

print(nomes)

print(nomes[0])

nomes[0] = 'gabriela'
print(nomes[0])

dados = ['gabriel', 19, 1.70]


print(dados)

print(len(nomes))

print(type(nomes))
print(type(nomes[2]))

print(nomes[2:])



#in nomes 
if 'arthur' in nomes:
  print("arthur é amigo")
else:
    print("arthur já foi amigo")

print(nomes.__contains__("arthur"))

#nomes[1:3] = ['cataryna', 'bernardo']

print(nomes)

nomes.append("joão")

nomes.insert(1, "joão")

nomes.remove("")
print(nomes)

removido = nomes.pop()
print(nomes)
print(removido)
