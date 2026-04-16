# Coleta de dados
cp1 = float(input("Digite a nota do Checkpoint 1: "))
cp2 = float(input("Digite a nota do Checkpoint 2: "))
cp3 = float(input("Digite a nota do Checkpoint 3: "))
sp1 = float(input("Digite a nota da Sprint 1: "))
sp2 = float(input("Digite a nota da Sprint 2: "))
gs = float(input("Digite a nota da Global Solution: "))

# Identificação de menor média
if cp1 <= cp2 and cp1 <= cp3:
    menor_cp = cp1
elif cp2 <= cp1 and cp2 <= cp3:
    menor_cp = cp2
else:
    menor_cp = cp3

# Soma das duas maiores notas checkpoint
soma_cps = (cp1 + cp2 + cp3) - menor_cp

# Calculo de media
media = ((soma_cps + sp1 + sp2) / 4) * 0.4 + gs * 0.6

# Calculo de media com peso
mediaPeso = media * 0.4

print(f"A média sem peso é: {media:.2f}")
print(f"A média com peso é: {mediaPeso:.2f}")