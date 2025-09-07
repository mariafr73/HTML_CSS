#Peça um número e informe se esse número e Positivo ou Negativo e se é Par ou Impar

x = int(input("Informe um número: "))

if x > 0:
    print(x, "é positivo")
else:
    print(x, "é negativo")

if x % 2 == 0:
    print(x, "é par!")
else:
    print(x, "é impar!")