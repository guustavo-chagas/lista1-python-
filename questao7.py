limite = int(input("Digite até onde quer a sequência de Fibonacci: "))

a, b = 0, 1
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b
