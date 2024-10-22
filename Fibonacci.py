def fibonacci(limite):
    sequencia_fibonacci=[0, 1]

    while limite > sequencia_fibonacci[-1]:
        sequencia_fibonacci.append(sequencia_fibonacci[-1]+sequencia_fibonacci[-2])

    if limite in sequencia_fibonacci:
        return f"{limite} está na sequência."
    else:
        return f"{limite} não está na sequência."
    
num = int(input("Insira o número: "))
resultado = fibonacci(num)
print(resultado)