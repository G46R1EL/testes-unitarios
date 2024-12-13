import unittest

class ConsumoAgua:
    def __init__(self):
        self.historico_consumo = []

    def registrar_consumo(self, litros):
        if litros <= 0:
            return "Valor de consumo inválido."
        elif litros > 10000:
            return "Valor de consumo muito alto."
        else:
            self.historico_consumo.append(litros)
            return f"Consumo registrado com sucesso."
    
    def verificar_consumo_total(self):
        return sum(self.historico_consumo)

class TestConsumoAgua(unittest.TestCase):

    def test_registrar_consumo_valido(self):
        consumo = ConsumoAgua()
        self.assertEqual(consumo.registrar_consumo(130), "Consumo registrado com sucesso.")
        self.assertEqual(consumo.verificar_consumo_total(), 130)

    def test_registrar_consumo_invalido(self):
        consumo = ConsumoAgua()
        self.assertEqual(consumo.registrar_consumo(-10), "Valor de consumo inválido.")
        self.assertEqual(consumo.verificar_consumo_total(), 0)

    def test_registrar_consumo_muito_alto(self):
        consumo = ConsumoAgua()
        self.assertEqual(consumo.registrar_consumo(15000), "Valor de consumo muito alto.")
        self.assertEqual(consumo.verificar_consumo_total(), 0)

    def test_registrar_varios_consumos(self):
        consumo = ConsumoAgua()
        consumo.registrar_consumo(100)
        consumo.registrar_consumo(200)
        consumo.registrar_consumo(300)
        self.assertEqual(consumo.verificar_consumo_total(), 600)

if __name__ == '__main__':
    unittest.main()
