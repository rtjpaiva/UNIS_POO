n = int(input("Digite um número: "))

maior = n
menor = n

x = 0

while x < 2:
    n = int(input("Digite um número: "))
    if n < menor:
        menor = n
    if n > maior:
        maior = n

    x += 1
print("Menor número:", menor)