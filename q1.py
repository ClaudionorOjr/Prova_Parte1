lista = []
contador = 0
cont1 = 0
cont2 = 19
contl = 0

while contador < 20:
    x = int(input("Valor a ser adicionado na lista:"))
    lista.append(x)
    contador = contador + 1
print("Lista:")
print(lista)

while contl < 10:
    aux = lista[cont1]
    lista[cont1] = lista[cont2]
    lista[cont2] = aux
    cont1 = cont1 + 1
    cont2 = cont2 -1
    contl = contl + 1

print("Lista com os elementos trocados:")
print(lista)
