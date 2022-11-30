#algoritimo que verica o numero maior e finaliza com 0

print("insira 3 números inteiros e positivos e veja qual deles é maior \ndigite 0 para finlizar")

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == 0 or num2 == 0 or num3 == 0:
    print("fim do programa")
    quit
elif num1 > num2 & num2 > num3:
    maior = num1
    meio = num2
    menor = num3
elif num1 > num3 & num3 > num2:
    maior = num1
    meio = num3
    menor = num2
elif num2 > num1 & num1 > num3:
    maior = num2
    meio = num1
    menor = num3
elif num2 > num3 & num3 > num1:
    maior = num2
    meio = num3
    menor = num1
elif num3 > num1 & num1 > num2:
    maior = num2
    meio = num1
    menor = num3
elif num3 > num2 & num2 > num1:
    maior = num2
    meio = num1
    menor = num3
print(maior, meio, menor)