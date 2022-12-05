#algoritmo que lê sequencias de 0s e 1s e mostra o decimal que o representa

listaBI = []
listaPo = [1,2,4,8,16,32,64,128]
listaRe = []

print("insira 8 números de sequencia de 0s e 1s: ")

for nums in range(0,8):
    nums = int(input(f"{nums + 1}: "))
    listaBI.append(nums)

listaBI.reverse()

for bibi in range(0,8):
    bobo = listaPo[bibi]
    bebe = listaBI[bibi]
    rere = bebe * bobo
    listaRe.append(rere)

print(sum(listaRe))