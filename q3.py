lista1 = []
contador1 = 0

while contador1 < 16:
    a = int(input("Digite os valores da matriz A: "))
    lista1.append(a)
    contador1 = contador1 + 1

print("""
    | {} {} {} {} |
A = | {} {} {} {} |
    | {} {} {} {} |
    | {} {} {} {} |""".format(lista1[0],lista1[1],lista1[2],lista1[3],lista1[4],lista1[5],lista1[6],lista1[7],lista1[8],lista1[9],lista1[10],lista1[11],lista1[12],lista1[13],lista1[14],lista1[15]))

lista2 = []
contador2 = 0

while contador2 < 16:
    b = int(input("Digite os valores da matriz B: "))
    lista2.append(b)
    contador2 = contador2 + 1

print("""
    | {} {} {} {} |
B = | {} {} {} {} |
    | {} {} {} {} |
    | {} {} {} {} |""".format(lista2[0],lista2[1],lista2[2],lista2[3],lista2[4],lista2[5],lista2[6],lista2[7],lista2[8],lista2[9],lista2[10],lista2[11],lista2[12],lista2[13],lista2[14],lista2[15]))

print("Soma das Matroze A e B:")
print("""
      | {} {} {} {} |
A+B = | {} {} {} {} |
      | {} {} {} {} |
      | {} {} {} {} |""".format(lista1[0]+lista2[0],lista1[1]+lista2[1],lista1[2]+lista2[2],lista1[3]+lista2[3],lista1[4]+lista2[4],lista1[5]+lista2[5],lista1[6]+lista2[6],lista1[7]+lista2[7],lista1[8]+lista2[8],lista1[9]+lista2[9],lista1[10]+lista2[10],lista1[11]+lista2[11],lista1[12]+lista2[12],lista1[13]+lista2[13],lista1[14]+lista2[14],lista1[15]+lista2[15]))
