paisa = 15000000
paisb = 20000000
anos = 0

while paisa < paisb:
    paisa += paisa * 0.03
    paisb += paisb * 0.02
    anos += 1

print(f"Levarão {anos} anos para que a população do país A ultrapasse a população do país B")