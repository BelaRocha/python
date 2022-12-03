#calcular porcentagem de números impar entre 10 números digitados

listaNum = []
listaNumImp = []

print("Insira 10 números positivos e veja quantos deles são impar:\n")

for imp in range(0,10):
    while True:
        try:
            num = int(input(f"{imp + 1}: "))
        except ValueError:
            print("idiota")
            continue
        if num < 0:
            print("P O S I T I V O")
            continue
        else:
            listaNum.append(num)
            break
for nums in listaNum:
    if nums % 2 != 0:
        listaNumImp.append(nums)

porcentagem = 10 * len(listaNumImp)

print(porcentagem,"%")
