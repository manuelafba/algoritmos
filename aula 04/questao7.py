a = int(input('Digite o lado A: '))
b = int(input('Digite o lado B: '))
c = int(input('Digite o lado C: '))

if a > b + c:
    print("Esses valores não compõem um triângulo")
elif a == b == c:
    print("Triângulo equilátero")
elif a != b == c or a == b != c:
    print("Triângulo isósceles")
elif a != b != c:
    print("Triângulo escaleno")