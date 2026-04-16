def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= (renda * 20):
        return True
    else:
        return False


def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif 7 <= parcelas <= 12:
        return 0.08
    else:
        return 0.10


def calcular_parcela(valor, taxa, parcelas):
    numerador = taxa * (1 + taxa) ** parcelas
    denominador = (1 + taxa) ** parcelas - 1
    pmt = valor * (numerador / denominador)
    return pmt


def calcular_total(parcela, parcelas):
    return parcela * parcelas


def calcular_juros(total, valor):
    return total - valor

#Coleta de dados
nome = input("Nome do cliente: ")
cliente_idade = int(input("Idade: "))
cliente_renda = float(input("Renda mensal (R$): "))
valor_desejado = float(input("Valor desejado do empréstimo (R$): "))
n_parcelas = int(input("Número de parcelas (3 a 24): "))

#Validação do número de parcelas
if n_parcelas < 3 or n_parcelas > 24:
    print("\nErro: O número de parcelas deve ser entre 3 e 24.")
else:
    aprovado = pode_aprovar(cliente_idade, cliente_renda, valor_desejado)

#Resultados finais
    print(f"\nResultado para: {nome}")

    if aprovado:
        taxa_aplicada = definir_taxa(n_parcelas)
        valor_pmt = calcular_parcela(valor_desejado, taxa_aplicada, n_parcelas)
        valor_total = calcular_total(valor_pmt, n_parcelas)
        total_juros = calcular_juros(valor_total, valor_desejado)

        print("Status: Empréstimo aprovado")
        print(f"Valor Financiado: R$ {valor_desejado:,.2f}")
        print(f"Taxa de Juros: {taxa_aplicada * 100:.0f}% ao mês")
        print(f"Valor da Parcela: R$ {valor_pmt:,.2f}")
        print(f"Valor Total Pago: R$ {valor_total:,.2f}")
        print(f"Total de Juros Pagos: R$ {total_juros:,.2f}")
    else:
        print("\nStatus: Empréstimo negado")
        print("Motivo: O cliente não atende aos requisitos de idade ou margem de renda.")