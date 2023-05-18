paisA = 35000000
paisB = 48000000
anos = 0

while paisA <= paisB:
    paisA = paisA + paisA * 0.03
    paisB = paisB + paisB * 0.02
    anos += 1
    
print(f"Serão necessários {anos} para que a população de A seja maior que a de B")