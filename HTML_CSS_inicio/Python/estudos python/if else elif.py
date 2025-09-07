# if (se) - elif (se encadeado) - else (senão)
print("Se e senão: if - else: \n")
if 1 == 2:
    print("1 é igual a 2")
elif 1 == 1:
    print("1 é igual a 1")
else:
    print("1 é diferente de 2")

#Operadores de comparação
print("\nOperadores de comparação: \n")
if 1 == 1:
    print("1 é igual a 1")

if 1 != 2:
    print("1 é diferente de 2")

if 1 > 2:
    print("1 é maior que 2")

if 1 < 2:
    print("1 é menor que 2")

if 1 <= 2:
    print("1 é menor ou igual a 2")

if 1 >= 2:
    print("1 é maior ou igual a 2")

#Operadores lógicos
print("\nOperadores logicos: \n")
if 1 == 1 and 2 == 2:
    print("1 é igual a 1 e 2 é igual a 2")

if 1 == 1 or 2 == 2:
    print("1 é igual a 1 ou 2 é igual a 2")

if not 1 == 2:
    print("1 é diferente de 2")

#Operadores de identidade
print("\nOperadores de identidade: \n")
if 1 is 1:
    print("1 é igual a 1")

if 1 is not 2:
    print("1 é diferente de 2")

#Operadores de associação
print("\nOperadores de associação: \n")
lista = [1, 2, 3, 4, 5]

if 1 in lista:
    print("1 está contido na lista")

if 6 not in lista:
    print("6 não está contido na lista")