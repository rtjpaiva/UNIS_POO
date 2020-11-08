dia = int(input("Insira o dia do seu nascimento: "))
mes = int(input("Insira o mês do seu nascimento: "))
ano = int(input("Insira o ano do seu nascimento: "))

dia2 = int(input("\nInsira o dia atual: "))
mes2 = int(input("Insira o mês atual: "))
ano2 = int(input("Insira o ano atual: "))

idade_anos = ano2 - ano

if mes >= mes2:
    if mes == mes2:
        if dia > data2:
            idade_anos - 1

    else:
        idade_anos - 1

dias_vividos =  (30 - dia) + ((12 - mes)*30) + ((mes2 - 1)*30) + dia2 + (idade_anos)*365


print("Vivo a ",dias_vividos,"dias.")
