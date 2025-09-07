# Declaração de variavel 
x = 5
y = "Hello, World! \n"
print(x)
print(y)

x = 4       
x = "Sally \n" 
print(x)

# Tipos de Variaveis

#Tipos de sequência
x = ["apple", "banana", "cherry"] # list
y = ("apple", "banana", "cherry") # tuple
z = range(6)                     # range
w = "banana"                     # str

#Tipos numéricos
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Tipos de mapeamento
x = {"name" : "John", "age" : 36} # dict

#Tipos de conjunto
x = {"apple", "banana", "cherry"} # set
y = frozenset({"apple", "banana", "cherry"}) # frozenset

#Tipos booleanos
x = True
y = False

#Tipos binários
x = b"Hello"

#Tipos byte
x = bytearray(5)

#Tipos de memória
x = memoryview(bytes(5))

#Tipos de dados definidos pelo usuário
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

#Variáveis globais
x = "awesome"
def myfunc():
    print("\nPython is " + x)
myfunc()