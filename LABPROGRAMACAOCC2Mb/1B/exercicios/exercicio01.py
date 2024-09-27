nomes = ['jorge', 'Antonio' , ' fernanda', 'jose', 'joao', 'wagner', 'marie']
         
nomes_com_j = []

for nome in nomes:
  if nome.startswith('j'):
    nomes_com_j.append(nome)


  print("nomes com j: ", nomes_com_j ")

#usando list compreension
nomes_com_j = [nome for nome in nomes if "j" in nome]
print("nomes com j: ", nomes_com_j)