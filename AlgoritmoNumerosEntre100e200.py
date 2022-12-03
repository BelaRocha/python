#informar quantos números esrtão então entre 100 e 200
#limpa a tela
import os
os.system('cls')
#listas
listNum = []
listEntre = []

print("insira 10 número inteiros e positivos e veja quantos deles estão entre 100 e 200")
#insere os números 
for num in range(0,10): 
    while True:
        try:
            num = int(input(f"{num +1}: "))
        except ValueError:
            print("idiota")
            continue
        if num < 0:
            print("positivooo")
            continue
        else:
            listNum.append(num)
            break
#verifica se o número está entre 100 e 200
for numE in listNum:
    if numE < 200 and numE > 100:
        listEntre.append(numE)
#mostra a quantidade de números 
numNum = len(listEntre)

os.system('cls')

print(numNum,'estão entre 100 e 200')