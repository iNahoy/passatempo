print("Digite o primeiro valor | Superior Esquerdo: ")
n1 = input()

print("Digite o segundo valor | Inferior Esquerdo: ")
n2 = input()

print("Digite o terceiro valor | Superior Direito: ")
n3 = input()

print("Digite o quarto valor | Inferior Direito: ")
n4 = input()

if n1 != "x":
    n1 = int(n1)
if n2 != "x":
    n2 = int(n2)
if n3 != "x":
    n3 = int(n3)
if n4 != "x":
    n4 = int(n4)

if n1 == "x":
        resultado = ((n2 * n3) / n4)
        print(resultado)
elif n2 == "x":
        resultado = ((n1 * n4) / n3)
        print(resultado)
elif n3 == "x":
        resultado = ((n1 * n4) / n2)
        print(resultado)
elif n4 == "x":
        resultado = ((n2 * n3) / n1)
        print(resultado)