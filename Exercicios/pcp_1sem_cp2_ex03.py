notas1 = input("Digite os três notas do checkpoint (0 a 10): ").split()
notas2 = input("Digite as duas notas das sprints (0 a 10): ").split()
nota_gs = float(input("Digite a nota da grobal solution (0 a 10): "))

notas_cp = [float(x) for x in notas1]
notas_sprint = [float(x) for x in notas2]

a, b, c = sorted(notas_cp, reverse=False)
d, e = sorted(notas_sprint)

media_semestre = ((b + c + d + e) / 4) * 0.4 + nota_gs * 0.6

print(f"Media do semestre: {media_semestre:.2f}")
