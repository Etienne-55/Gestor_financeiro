salario = float(input("Informe o valor do seu salário: "))

valor_alimento = salario *0.30

valor_lazer = salario *0.20

valor_economia = salario *0.10

valor_uber = salario *0.35

valor_outros = salario *0.05

print(f"recomendação de gastos para salário de valor: {salario}\n ")

print(f"Alimentação:{valor_alimento}")
print(f"Locomoção:{valor_uber}")
print(f"Lazer:{valor_lazer}")
print(f"Economia:{valor_economia}")
print(f"Outros:{valor_outros}")