#1) crie uma função que receba um inteiro por parâmetro e devolva o fatorial deste número.
def fatorial(n):
 if(n > 1):
   return n * fatorial(n-1) 
 else:
  return 1


def arranjo(n, p):
  return fatorial(n) / fatorial(n-p)

def combinacao(n,p):
  return fatorial(n)/ (fatorial(p) * fatorial(n-p))



print(f"o fatorial de 5 é: {fatorial(5)}")
print(f"o arranjo de 5, 2 a 2 é: {arranjo(5,2)}")
print(f"a combinação de 5, 2 a 2 é: {combinacao(5,2)}")

  



#2) crie as funções arranjo e combinação que utilizam a função fatorial da questão anterior para realizar seus calculos.

#   An,p=n!/(n-p)! , Cn,p=n!/p!(n-p)!

#os resultados devem ser retornados pelas funções 