inventario_inicial = {50000: 10, 20000: 10, 10000: 10, 5000: 10}


class Cajero:
    def __init__(self, inventario):
        self.inventario = dict(inventario)

    def total(self):
        t = 0
        for d in self.inventario:
            t += d * self.inventario[d]
        return t

    def buscar(self, monto, lista, i):
        if monto == 0:
            return {}
        if i == len(lista):
            return None
        d = lista[i]
        maximo = min(monto // d, self.inventario[d])
        for c in range(maximo, -1, -1):
            r = self.buscar(monto - c * d, lista, i + 1)
            if r is not None:
                if c > 0:
                    r[d] = c
                return r
        return None

    def retirar(self, monto):
        if type(monto) != int or monto <= 0:
            raise ValueError("Monto invalido")
        if monto > self.total():
            raise ValueError("Sin dinero suficiente")
        lista = sorted(self.inventario, reverse=True)
        entrega = self.buscar(monto, lista, 0)
        if entrega is None:
            raise ValueError("No se puede entregar ese monto")
        for d in entrega:
            self.inventario[d] -= entrega[d]
        return entrega


if __name__ == "__main__":
    cajero = Cajero(inventario_inicial)
    print("Total:", cajero.total())
    print("Retiro:", cajero.retirar(130000))
    print("Inventario:", cajero.inventario)
