#Mini Projeto

laudos =[
    {"Numero": "LAB-2025-00325", "pH": 6.5, "Turbidez":75, "Coliformes Totais": True},
    {"Numero": "LAB-2025-00326", "pH": 7.5, "Turbidez":80, "Coliformes Totais": False},
    {"Numero": "LAB-2025-00327", "pH": 8.5, "Turbidez":101, "Coliformes Totais": True},
    {"Numero": "LAB-2025-00328", "pH": 9.5, "Turbidez":120, "Coliformes Totais": False},
    {"Numero": "LAB-2025-00329", "pH": 4.2, "Turbidez":125, "Coliformes Totais": True},
    {"Numero": "LAB-2025-00330", "pH": 6.5, "Turbidez":75, "Coliformes Totais": True}, 
]

print(len(laudos))

#limites
pH_limite_minimo = 6.5
pH_limite_maximo = 8.5

turbidez_limite_maximo = 100

#Função de validação pH
def validar_parametro_ph(pH,pH_limite_minimo, pH_limite_maximo):
    if pH > pH_limite_minimo:
        return "Reprovado", f"O pH do laudo {laudo.Numero} está acima do limite permitido{pH_limite_minimo}."
    elif ph < pH_limite_maximo:
        return "Reprovado", f"O pH do laudo {laudo.Numero} está abaixo do limite permitido{pH_limite_maximo}."
    else:
        return "Aprovado", f"O pH do laudo {laudo.Numero} está dentro do limite permitido."

#Função de validação turbidez
def validar_parametro_turbidez(turbidez,turbidez_limite_maximo):
    if turbidez > turbidez_limite_maximo:
        return "Reprovado", f"A turbidez do laudo {laudo.Numero} está acima do limite permitido{turbidez_limite_maximo}."
    else:
        return "Aprovado", f"A turbidez do laudo {laudo.Numero} está dentro do limite permitido."   

#Função de validação coliformes
def validar_parametro_coliformes(presenca):
    if presenca == True:
        return "Reprovado", f"A presença de coliformes totais indica contaminação."
    else:
        return "Aprovado", f"A presença de coliformes totais indica ausência de contaminação."    
