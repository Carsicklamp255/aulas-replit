def getitem(list, index):
  if index < 0:
    raise Exception('indice invalido')
  return list[index]

students = ['carlos', 'maria', 'jose', 'pedro']

print(getitem(students, -1))

print('um print qq')