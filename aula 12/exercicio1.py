from dataclasses import dataclass
@dataclass
class RegCliente:
    idade: int
    freq: int
    av: int
    sug: str

menor18 = 0
meio = 0 
maior65 = 0
exc = 0
boa = 0
mel = 0
sugest = []

cliente = [0]*50
for i in range(50):
    cliente[i] = RegCliente(0,0,0,'')
for i in range(50):
    cliente[i].idade = int(input("Digite sua idade:"))
    if cliente[i].idade < 18:
        menor18 += 1
    elif cliente[i].idade < 65:
        meio += 1
    else:
        maior65 += 1

    cliente[i].freq = int(input("Com qual frequência você vem ao shopping? (Digite 1 para diariamente, 2 para semanalmente ou 3 para eventualmente): "))
    cliente[i].av = int(input("Como você avalia a praça de alimentação? (Digite 1 para excelente, 2 para boa ou 3 para precisa melhorar): "))
    if cliente[i].av == 3:
        mel += 1
        cliente[i].sug = input("Por favor, digite uma sugestão de melhoria para a praça: ")
        sugest.append(cliente[i].sug) 
    elif cliente[i].av == 1:
        exc += 1
    else: 
        boa += 1

porcmenor = (menor18 / 50) * 100
porcmeio = (meio / 50) * 100
porcmaior = (maior65 / 50) * 100
porcexc = (exc / 50) * 100
porcboa = (boa / 50) * 100
porcmel = (mel / 50) * 100

print(f"{porcmenor} % dos clientes são menores de 18 anos, {porcmeio} % têm idade entre 18 e 65 e {porcmaior} % têm mais de 65 anos")
print(f"{porcexc} % dos clientes avaliam a praça de alimentação como excelente, {porcboa} % avaliam como boa e {porcmel} % acreditam que a praça precisa de melhorias")
print("Sugestões dos clientes: ")
print(sugest)
        




