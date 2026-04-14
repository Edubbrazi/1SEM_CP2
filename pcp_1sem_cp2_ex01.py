#Coleta de dados
from numba.core.cgutils import printf

cod_origem = int(input("Insira o código de origem da carga do caminhão(1-5): "))
cod_carga = int(input("Insira o código da carga(10-40): "))
peso_carga = float(input("Insira o peso da carga do caminhão em toneladas: "))

#conversão de toneladas para quilos

peso = peso_carga * 1000
if 10<= cod_carga <= 20:
    preco = peso * 100
    print(f"O valor da carga respectivamente a seu código: {preco}")
elif 21<= cod_carga <= 30:
    preco = peso * 250
    print(f"O valor da carga respectivamente a seu código: {preco}")
elif 31 <= cod_carga <= 40:
    preco = peso * 340
    print(f"O valor da carga respectivamente a seu código: {preco}")
#Valor do imposto