# Validação de laudo baseada em parâmetros reais pH
# Padrão Conama 357/2005- águas classe 2: pH entre 6,0 e 9,0

numero_laudo = "LAB-2025-00314"
resultado_ph = 9.8
limite_minimo = 6.0
limite_maximo = 9.0

#condicional principal

if resultado_ph < limite_minimo:
    status = "Reprovado!!!"
    motivo = f"pH: {resultado_ph} abaixo do limite minimo({limite_minimo})"
elif resultado_ph > limite_maximo:
    status = "Reprovado!!!"
    motivo = f"pH: {resultado_ph} acima do Limite maximo({limite_maximo})"
else:
    status = "Aprovado"
    motivo = f"pH: {resultado_ph} dentro dos parâmetros legais"



print("********************Exibição do Resultado********************")
print(f"Laudo: {numero_laudo}")
print(f"Resultado: {status}")
print(f"Motivo: {motivo}")
print("************************************************************")


