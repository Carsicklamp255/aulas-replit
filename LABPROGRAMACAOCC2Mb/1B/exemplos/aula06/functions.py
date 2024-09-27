
def minha_funcao(**kwargs):
 print(f"Seu nome é {kwargs['nome']}")
 print(f"Sua idade é {kwargs['idade']}")
 print(f"Seu peso é {kwargs['peso']}")

 minha_funcao(nome = "wagner", sobrenome="barreto",  idade = 19, peso = 70, sexo="M")



def soma (V1=0, V2=0):
    return   V1+V2

def multiplica(V1=0, V2=0):
  resultado = 0
  for i in range(V2):
    resultado = soma(resultado, V1)
    return resultado 
print(f"a soma deu:{soma(5,5)}")
print(f"a multiplicação deu:{multiplica(5,5)}")