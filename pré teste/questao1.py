invest = 1000
meses = 0

while invest < 15000:
    invest += invest * 0.03
    meses += 1

print(f"Sr. Pantera conseguirá o investimento final de R$15.000 após {meses/12} anos")