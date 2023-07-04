class Calculadora:
    def __init__(self, n1, n2, n3, n4):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4

    def calcular(self):
        if self.n1 != "x":
            self.n1 = int(self.n1)
        if self.n2 != "x":
            self.n2 = int(self.n2)
        if self.n3 != "x":
            self.n3 = int(self.n3)
        if self.n4 != "x":
            self.n4 = int(self.n4)

        if self.n1 == "x":
            resultado = (self.n2 * self.n3) / self.n4
            return resultado
        elif self.n2 == "x":
            resultado = (self.n1 * self.n4) / self.n3
            return resultado
        elif self.n3 == "x":
            resultado = (self.n1 * self.n4) / self.n2
            return resultado
        elif self.n4 == "x":
            resultado = (self.n2 * self.n3) / self.n1
            return resultado

print("Digite o primeiro valor | Superior Esquerdo: ")
n1 = input()

print("Digite o segundo valor | Inferior Esquerdo: ")
n2 = input()

print("Digite o terceiro valor | Superior Direito: ")
n3 = input()

print("Digite o quarto valor | Inferior Direito: ")
n4 = input()

calculadora = Calculadora(n1, n2, n3, n4)
resultado = calculadora.calcular()
print(resultado)