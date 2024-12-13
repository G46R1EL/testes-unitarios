import unittest

class ContaBancaria():
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito realizado com sucesso."
        else:
            return "Valor inválido."
        
    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente."
        elif valor <= 0:
            return "Valor inválido."
        else:
            self.saldo -= valor
            return f"Saque realizado com sucesso."
    
    def verificar_saldo(self):
        return self.saldo

class TestContaBancaria(unittest.TestCase):

    def test_deposito(self):
        conta = ContaBancaria()
        conta.depositar(1500)
        self.assertEqual(conta.verificar_saldo(), 1500)
        self.assertEqual(conta.depositar(100), "Depósito realizado com sucesso.")
        self.assertEqual(conta.verificar_saldo(), 1600)

    def test_saque(self):
        conta = ContaBancaria(3000)
        self.assertEqual(conta.sacar(200), "Saque realizado com sucesso.")
        self.assertEqual(conta.verificar_saldo(), 2800)
        self.assertEqual(conta.sacar(3500), "Saldo insuficiente.")
        self.assertEqual(conta.verificar_saldo(), 2800)
        self.assertEqual(conta.sacar(-30), "Valor inválido.")

    def test_saldo(self):
        conta = ContaBancaria(2000)
        conta.depositar(800)
        conta.sacar(320)
        conta.sacar(200)
        self.assertEqual(conta.verificar_saldo(), 2280)

if __name__ == '__main__':
    unittest.main()
