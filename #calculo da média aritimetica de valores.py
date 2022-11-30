#calculo da média aritimetica de valores positivos, o programa finalizab quaanod o valor for negativo

print('digite 6 valores positivos inteiros para saber a média\n')

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

media = ((a + b + c + d + e + f)/6)
if media < 0:
    print ('a média é negativa')
    quit
else:
    print(media)
