
from time import time

n = 10000
k = 0

tempo_inicial = time()
# for i in range(n):
#     for j in range(n):
#         k += 1

# for i in range(n):
#     k = 1
#     while (k < n):
#         k *= 2

k = 1
while (k < n):
    k *= 2

tempo_de_execucao = time() - tempo_inicial
print(f'Tempo de Execução: {tempo_de_execucao}')