class conta:
    def __init__(self,saldo_inicial):
      self.__saldo = saldo_inicial

    def sacar(self,valor):
      if self.__saldo > valor:
        self.__saldo -= valor

      else:
        raise Exception("saldo insuficiente 'pobre'")

    def depositar(self,valor):
      self.__saldo += valor

    def consultar_saldo(self):
      return self.__saldo
    def transferir(self,valor,conta_destino):
      self.sacar(valor)
      conta_destino.depositar(valor)

      conta = conta(100)

try:
    conta.sacar(250)
except Exception as e:
  print(e)

print('seu saldo é:', conta.consultar_saldo())