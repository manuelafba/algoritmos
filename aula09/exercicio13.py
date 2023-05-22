vet1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
vet2 = [0]*12

for i in range(0, 12):
    if i % 2 != 0:
        vet2[i] += vet1[i]
        
print(vet1)
print(vet2)