limite = int(input("Digite aqui a sequência: "))

a, b = 0, 1
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b
