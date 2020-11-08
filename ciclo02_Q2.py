a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

b_c = b-c
if b_c < 0:
    b_c = b_c * -1

a_c = a-c
if a_c < 0:
    a_c = a_c * -1

a_b = a-b
if a_b < 0:
    a_b = a_b * -1

if ( b_c < a < b + c ) and ( a_c < b < a + c ) and ( a_b < c < a + b):
   print("\nArea:",(a*b)/2)

else:
    print("Não é um triângulo.")