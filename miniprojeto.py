#Mini Projeto do DIA 6

laudos =[
    {"numero": "LAB-2025-00325", "pH": 6.5, "Turbidez":75, "Coliformes": True},
    {"numero": "LAB-2025-00326", "pH": 7.5, "Turbidez":80, "Coliformes": False},
    {"numero": "LAB-2025-00327", "pH": 8.5, "Turbidez":101, "Coliformes": True},
    {"numero": "LAB-2025-00328", "pH": 9.5, "Turbidez":120, "Coliformes": False},
    {"numero": "LAB-2025-00329", "pH": 4.2, "Turbidez":125, "Coliformes": True},
    {"numero": "LAB-2025-00330", "pH": 6.5, "Turbidez":75, "Coliformes": True}, 
]

#limites
pH_limite_minimo = 6.5
pH_limite_maximo = 8.5
turbidez_limite_maximo = 100

#Função de validação pH
def validar_ph(pH,pH_limite_minimo, pH_limite_maximo):
    if pH < pH_limite_minimo:
        return "Reprovado", f"O pH está abaixo do limite permitido {pH_limite_minimo}."
    elif pH > pH_limite_maximo:
        return "Reprovado", f"O pH está acima do limite permitido {pH_limite_maximo}."
    else:
        return "Aprovado", f"O pH está dentro do limite permitido."
 
#Função de validação turbidez
def validar_turbidez(turbidez,turbidez_limite_maximo):
    if turbidez > turbidez_limite_maximo:
        return "Reprovado", f"A turbidez está acima do limite permitido{turbidez_limite_maximo}."
    else:
        return "Aprovado", f"A turbidez está dentro do limite permitido."   

#Função de validação coliformes 
def validar_coliformes(presenca):
    if presenca == True:
        return "Reprovado", f"A presença de coliformes totais indica contaminação."
    else:
        return "Aprovado", f"A presença de coliformes totais indica ausência de contaminação."    

#Função de avaliação geral dos laudos
def avaliar_laudos(numero, pH, turbidez, coliformes):
    status_ph, motivo_ph = validar_ph(pH, pH_limite_minimo,pH_limite_maximo)
    status_turbidez, motivo_turbidez = validar_turbidez(turbidez,turbidez_limite_maximo)
    status_coliformes, motivo_coliformes = validar_coliformes(coliformes) 

    #Retorna o status geral dos laudos
    if status_ph == "Reprovado" or status_turbidez == "Reprovado" or status_coliformes == "Reprovado":
        status_geral = "Reprovado"
    else:
        status_geral = "Aprovado"

    print(f"\nLaudos: {numero}")
    print(f"PH: {pH} {status_ph} {motivo_ph}")
    print(f"Turbidez: {turbidez} {status_turbidez} {motivo_turbidez}")
    print(f"Coliformes: {coliformes} {status_coliformes} {motivo_coliformes}")

    return status_geral


aprovados = 0
reprovados = 0

#Imprime todos os laudos
for laudo in laudos: 
    resultado = avaliar_laudos(
        laudo['pH'],
        laudo['Turbidez'],
        laudo['Coliformes'],
    )
    if resultado == "Aprovado":
        aprovados += 1
    else:
        reprovados += 1

#Imprime o total de laudos aprovados e reprovados

total = len(laudos)

def resumo_executivo(total,aprovados,reprovados):
    print("===============================================================")
    print(f"Total de laudos: {total}")
    print(f"Laudos Aprovados: {aprovados}")
    print(f"Laudos Reprovados: {reprovados}")
    print(f"Porcentagem de Aprovados: {aprovados/total*100:.2f}%")
    print(f"Porcentagem de Reprovados: {reprovados/total*100:.2f}%")
    print("===============================================================")

resumo_executivo(total,aprovados,reprovados)   

