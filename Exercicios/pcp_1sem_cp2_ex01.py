#Coleta de dados
cod_origem = int(input("Insira o código de origem da carga do caminhão(1-5): "))
cod_carga = int(input("Insira o código da carga(10-40): "))
peso_carga = float(input("Insira o peso da carga do caminhão em toneladas: "))

#conversão de toneladas para quilos e preços

peso = peso_carga * 1000
print(f"O valor da carga em quilos é: {peso}")
if 10<= cod_carga <= 20:
    preco = peso * 100
    print(f"O preço da carga é: {preco}")
elif 21<= cod_carga <= 30:
    preco = peso * 250
    print(f"O preço da carga é: {preco}")
elif 31 <= cod_carga <= 40:
    preco = peso * 340
    print(f"O preço da carga é: {preco}")
#Valor do imposto
taxas = [0.35, 0.25, 0.15, 0.05, 0.0]

valor_imposto = preco * taxas[cod_origem - 1]
print(f"O valor do imposto da carga é: {valor_imposto}")

#Valor total

valor_total = preco + valor_imposto
print(f"O valor total da carga é: {valor_total}")