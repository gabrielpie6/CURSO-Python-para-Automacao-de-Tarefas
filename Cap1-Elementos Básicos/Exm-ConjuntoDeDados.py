departamentos = ["Financeiro", "Marketing", "RH", "Jurídico"]
print(f"ORIGINAL: {departamentos}")
departamentos.sort()
print(f"ORDENADO: {departamentos}")

departamentos.append("Contabilidade")
print(f"COM INSERÇÃO: {departamentos}")

copia = departamentos.copy()

print(f'ÍNDICE: {departamentos.index("Marketing")}')

departamentos.pop(0)
print(f'ÍNDICE: {departamentos.index("Marketing")}')
print(f"COM REMOÇÃO: {departamentos}")