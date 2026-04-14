#----------------------- SEQUÊNCIA DE FIBONACCI ------------------------------------------------
n = int(input("DIGITE A QUANTIDADE DE TERMOS: "))
contador = 0
a = 0
b = 1

while contador < n:
    print(a)
    proximo = a + b
    a = b
    b = proximo
    contador += 1
    
