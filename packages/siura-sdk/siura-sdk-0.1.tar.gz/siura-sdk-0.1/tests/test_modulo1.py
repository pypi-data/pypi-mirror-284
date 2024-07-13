import unittest
from test_modulo1.modulo1 import funcion1

class TestModulo1(unittest.TestCase):
    def test_funcion1(self):
        self.assertEqual(funcion1(), "Hola desde modulo1")

if __name__ == '__main__':
    unittest.main()