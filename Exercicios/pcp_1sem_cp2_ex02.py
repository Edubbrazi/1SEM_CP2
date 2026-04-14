# Coleta de valores dos lados do triângulo
triangulo = input("Digite os tres valores do triangulo: ").split()

# Transforma os valores digitados em int
numeros = [int(x) for x in triangulo]

# Organiza os valores em ordem decrescente
a, b, c = sorted(numeros, reverse=True)
print(f"Ordenados: A={a}, B={b}, C={c}")

# Evita que a mensagem de não existir triângulo apareça junto de algum outro
if a >= b + c:
    print("\nNao forma triangulo")

# Apenas ocorre depois que a primeira afirmação seja falsa
else:
    if a**2 == b**2 + c**2:
        print("\nTriangulo retangulo")
    elif a**2 > b**2 + c**2:
        print("\nTriangulo obtusangulo")
    elif a**2 < b**2 + c**2:
        print("\nTriangulo acutangulo")

    if a == b == c:
        print("\nTriangulo equilatero")
    elif a == b or b == c or a == c:
        print("\nTriangulo isoceles")