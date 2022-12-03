#simular 100 jogadas de um dado de 6 lados e mostrar a frequencisa que dada lado cai

import random

laladodo = []
lado1 = []
lado2 = []
lado3 = []
lado4 = []
lado5 = []
lado6 = []

for lado in range(0,100):
    ladodado = random.randint (1, 6)
    laladodo.append(ladodado)

print(laladodo)

def funcaoLado(x, ladox):
    for ladodo in laladodo:
        if ladodo == x:
            ladox.append(ladodo)
    print(f"lado {x} apareceu {len(ladox)}x em 100 tentativas")

funcaoLado(1, lado1)
funcaoLado(2, lado2)
funcaoLado(3, lado3)
funcaoLado(4, lado4)
funcaoLado(5, lado5)
funcaoLado(6, lado6)
