# Validação de laudo baseada em parâmetros reais pH
# Padrão Conama 357/2005- águas classe 2: pH entre 6,0 e 9,0

numero_laudo = "LAB-2025-00314"
resultado_ph = 9.8
limite_minimo = 6.0
limite_maximo = 9.0

resultado_turbidez = 120
limite_turbidez = 100

resultado_coliformes = False

#condicional principal

if resultado_ph < limite_minimo:
    status = "REPROVADO!!!"
    motivo = f"pH: {resultado_ph} abaixo do limite minimo({limite_minimo})"
elif resultado_ph > limite_maximo:
    status = "REPROVADO!!!"
    motivo = f"pH: {resultado_ph} acima do Limite maximo({limite_maximo})"
else:
    status = "APROVADO"
    motivo = f"pH: {resultado_ph} dentro dos parâmetros legais"

# Avaliando o Parametro de Turbidez
if resultado_turbidez > limite_turbidez:
    status_turbidez = "REPROVADO!!!"
    motivo_turbidez = f"Turbidez Total: {resultado_turbidez} acima do limite({limite_turbidez})"
else:
    status_turbidez = "APROVADO"
    motivo_turbidez = f"Turbidez Total: {resultado_turbidez} dentro dos padrões legais"    
    
# Avaliando o Parametro Coliformes Totais
if resultado_coliformes:  
    status_coliformes = "REPROVADO!!!"
    motivo_coliformes = f"Coliformes Totais: PRESENTE"
else:
    status_coliformes = "APROVADO"
    motivo_coliformes = f"Coliformes Totais: AUSENTE"    

# AVALIAÇÃO GERAL DO LAUDO

if status == "APROVADO" and status_turbidez == "APROVADO" and status_coliformes == "APROVADO":
    status_geral = "APROVADO"
    motivo_geral = "Laudo Aprovado em todos os Parâmetros"
else:
    status_geral = "REPROVADO!!!"
    motivo_geral = "Devido a não conformidade em UM ou MAIS parâmetros"    
    
print("********************Exibição do Resultado********************")
print(f"Laudo: {numero_laudo}")
print(f"Resultado: {status}")
print(f"Motivo: {motivo}")
print(f"Status Turbidez: {status_turbidez}")
print(f"Motivo Turbidez: {motivo_turbidez}") 
print(f"Status Coliformes: {status_coliformes}")
print(f"Motivo Coliformes: {motivo_coliformes}")
print("************************************************************")
print(f"Status Geral: {status_geral}")
print(f"Motivo Geral: {motivo_geral}")  
print("************************************************************")


