import unittest
from main import Cajero


class Pruebas(unittest.TestCase):

    def setUp(self):
        self.cajero = Cajero({50000: 2, 20000: 5, 10000: 5})

    def test_mayores_primero(self):
        self.assertEqual(self.cajero.retirar(70000), {50000: 1, 20000: 1})

    def test_descuenta(self):
        self.cajero.retirar(70000)
        self.assertEqual(self.cajero.inventario, {50000: 1, 20000: 4, 10000: 5})

    def test_retroceso(self):
        c = Cajero({50000: 1, 20000: 3})
        self.assertEqual(c.retirar(60000), {20000: 3})

    def test_imposible(self):
        antes = dict(self.cajero.inventario)
        with self.assertRaises(ValueError):
            self.cajero.retirar(15000)
        self.assertEqual(self.cajero.inventario, antes)

    def test_monto_muy_grande(self):
        with self.assertRaises(ValueError):
            self.cajero.retirar(10000000)

    def test_monto_invalido(self):
        for malo in (0, -5000, 1.5, "100"):
            with self.assertRaises(ValueError):
                self.cajero.retirar(malo)


if __name__ == "__main__":
    unittest.main()
