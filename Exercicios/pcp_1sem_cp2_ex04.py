# Definição de funções
def calculo_horas(salario, horasextras):
    valor_unitario_extra = salario * 0.015
    return valor_unitario_extra * horasextras

def calculo_faltas(salario, faltas):
    valor_unitario_falta = salario * 0.020
    return valor_unitario_falta * faltas

def calculo_bonus(cargo, recebeu_bonus):
    if recebeu_bonus.lower() != 's':
        return 0.0

    if cargo == 1:
        return 1000.0
    elif cargo == 2:
        return 500.0
    elif cargo == 3:
        return 300.0
    elif cargo == 4:
        return 100.0
    else:
        return 0.0


# Coleta de dados
nome = input("Digite o nome do funcionário: ")
cargo = int(input("Digite o cargo do funcionário (1 a 4): "))
salario = float(input("Digite o salário do funcionário: "))
horasextras = float(input("Digite a quantidade de horas extras trabalhadas: "))
faltas = int(input("Digite a quantidade de faltas do funcionário: "))
recebeu_bonus = input("Digite (s/n) se o funcionário recebeu bônus: ")

# Cálculo dos valores através das funções
valorBonus = calculo_bonus(cargo, recebeu_bonus)
valorHorasExtras = calculo_horas(salario, horasextras)
descontoFaltas = calculo_faltas(salario, faltas)

# Calculos finais
acrescimos = valorHorasExtras + valorBonus
salarioBruto = salario + acrescimos
salarioFinal = salarioBruto - descontoFaltas

# Resultados organizados
print(f"\nDemonstrativo de pagamento de {nome}")
print(f"\nO salário bruto é de: {salarioBruto}")
print(f"O total de acréscimos é de: {acrescimos}")
print(f"O total de descontos é de: {descontoFaltas}")
print(f"O salário final é de: {salarioFinal}")

