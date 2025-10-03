lista = [int(x) for x in input("Digite números separados por espaço: ").split()]

pares = [x for x in lista if x % 2 == 0]

if len(pares) > 0:
    media = sum(pares) / len(pares)
    print("Média dos pares:", media)
else:
    print("Não há números pares na lista")
