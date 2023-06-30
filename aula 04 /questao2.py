a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

delta = b**2-4*a*c
raizdelta = delta**0.5

x1 = (-b+raizdelta)/(2*a)
x2 = (-b-raizdelta)/(2*a)

print('Raizes: ',x1,' e ',x2)
