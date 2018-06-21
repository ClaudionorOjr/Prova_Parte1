lista = []
contador = 0

while contador < 25:
    x = int(input("Digite um valor para ser adicionado na lista:"))
    lista.append(x)
    if len(lista) == 1:
        menor = x
        maior = x
        posicao1 = contador
        posicao2 = contador
    if x > maior:
        posicao1 = contador
        maior = x
    if x < menor:
        posicao2 = contador
        menor = x
    contador = contador + 1
print("Maior valor da lista: {}, posicão: [{}]".format(maior,posicao1))
print("Menor valor da lista: {}, posição: [{}]".format(menor,posicao2))
print("Lista:",lista)

#Média

total = 0
for i in lista:
    total =  total + i
print("Total da soma dos valores:",total)

media = (total / len(lista))
print("A média da soma dos valores:",media)

#Desvio-padrão

pad=0
for i in lista:
    p = (i - media)**2
    pad+= p/(len(lista) - 1)
print("Desvio-padrão:",pad**0.5)
 

