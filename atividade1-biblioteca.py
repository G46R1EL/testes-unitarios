import unittest

class Biblioteca():
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo):
        if titulo in self.livros:
            return "Livro já adicionado anteriormente"
        else:
            self.livros.append(titulo)
            return "Livro adicionado com sucesso."
        
    def buscar_livro(self, titulo):
        if titulo in self.livros:
            return "Livro encontrado!"
        else:
            return "Livro não encontrado!"
        
    def remover_livro(self, titulo):
        if titulo in self.livros:
            self.livros.remove(titulo)
            return "Livro removido com sucesso."
        else:
            return "Livro não encontrado!"
        
class TestBiblioteca(unittest.TestCase):

    def test_adicionar_livro(self):
        biblioteca = Biblioteca()
        biblioteca.adicionar_livro("Harry Potter")
        self.assertTrue(biblioteca.adicionar_livro("Harry Potter"))

    def test_buscar_livro(self):
        biblioteca = Biblioteca()
        biblioteca.adicionar_livro("Moby Dick")
        self.assertEqual(biblioteca.buscar_livro("Moby Dick"), "Livro encontrado!")
        self.assertEqual(biblioteca.buscar_livro("Percy Jackson"), "Livro não encontrado!")

    def test_remover_livro(self):
        biblioteca = Biblioteca()
        biblioteca.adicionar_livro("O mar de monstros")
        self.assertEqual(biblioteca.remover_livro("O mar de monstros"), "Livro removido com sucesso.")
        self.assertEqual(biblioteca.buscar_livro("O mar de monstros"), "Livro não encontrado!")

if __name__ == '__main__':
    unittest.main()