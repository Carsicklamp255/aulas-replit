nomes = ["gabriel", "arthur", "antonio"]

for nome in nomes:
  print(nome)

for i in range(len(nomes)):
  print(nomes[i])

print('###iterando com wilhe')
i = 0
while i < len(nomes):
  print(nomes[i])
  i += 1

print('###usando list compreension###')
[print(nome) for nome in nomes]