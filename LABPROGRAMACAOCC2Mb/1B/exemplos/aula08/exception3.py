try:
  file = open('dados.txt', 'r')
  content = file.read()
  print(content)
  file.close()

except FileNotFoundError:
  print('arquivo não encontrado')
except Exception as e:
  print(e)