
# Valores de faturamento mensal por estado
sp_total = 67836.43
rj_total = 36678.66
mg_total = 29229.88
es_total = 27165.48
total_outros = 19849.53

# Ganho total no mes
total_mensal = sp_total + rj_total + mg_total + es_total + total_outros

#calculo de cada estado
sp = (sp_total / total_mensal) * 100
rj = (rj_total / total_mensal) * 100
mg = (mg_total / total_mensal) * 100
es = (es_total / total_mensal) * 100
outros = (total_outros / total_mensal) * 100

print("Resultado:\n")
print("SP:", sp, "%")
print("RJ:", rj, "%")
print("MG:", mg, "%")
print("ES:", es, "%")
print("Outros:", outros, "%")


