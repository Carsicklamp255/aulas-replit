import csv

students = [
  {'nome': 'nathan', 'idade': '18', 'naturalidade': 'são paulo'},
  {'nome': 'nicolas', 'idade': '32', 'naturalidade': 'xique xique'},
  {'nome': 'maria', 'idade': '18', 'naturalidade': 'vitoria'},
  {'nome': 'gabriel', 'idade': '26', 'naturalidade': 'vitoria '},
  {'nome': 'kaiky', 'idade': '18', 'naturalidade': 'vitoria da conquista'}
]

file_name = 'students.csv'

with open(file_name, mode= 'w', newline='') as file:
  writer = csv.DictWriter(file, fieldnames=['nome', 'idade', 'naturalidade'])
  writer.writeheader()
  writer.writerows(students)

print(f'o arquivo {file_name} foi criado')