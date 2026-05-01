#Mini Projeto do DIA 6

laudos =[
    {"numero": "LAB-2025-00325", "pH": 6.5, "Turbidez":75, "coliformes": True},
    {"numero": "LAB-2025-00326", "pH": 7.5, "Turbidez":80, "coliformes": False},
    {"numero": "LAB-2025-00327", "pH": 8.5, "Turbidez":101, "coliformes": True},
    {"numero": "LAB-2025-00328", "pH": 9.5, "Turbidez":120, "coliformes": False},
    {"numero": "LAB-2025-00329", "pH": 4.2, "Turbidez":125, "coliformes": True},
    {"numero": "LAB-2025-00330", "pH": 6.5, "Turbidez":75, "coliformes": True}, 
]

#limites
pH_limite_minimo = 6.5
pH_limite_maximo = 8.5
turbidez_limite_maximo = 100

#Função de validação pH
def validar_ph(pH,pH_limite_minimo, pH_limite_maximo):
    if pH < pH_limite_minimo:
        return "Reprovado", f" pH está abaixo do limite permitido {pH_limite_minimo}."
    elif pH > pH_limite_maximo:
        return "Reprovado", f" pH está acima do limite permitido {pH_limite_maximo}."
    else:
        return "Aprovado", f" pH está dentro do limite permitido."
 
#Função de validação turbidez
def validar_turbidez(turbidez,turbidez_limite_maximo):
    if turbidez > turbidez_limite_maximo:
        return "Reprovado", f" está acima do limite permitido{turbidez_limite_maximo}."
    else:
        return "Aprovado", f" está dentro do limite permitido."   

#Função de validação coliformes 
def validar_coliformes(presenca):
    if presenca:
        return "Reprovado", f"PRESENTE"
    else:
        return "Aprovado", f" AUSENTE"    

#Função de recomendação de ação
def recomendar_acao(risco):
    if risco == "Baixo":
        return "Manter rotina de monitoramento."
    elif risco == "Médio":
        return "Monitorar próximo lote com frequência dobrada"
    else:
        return "Interromper operação e acionar equipe de qualidade"

#Função de avaliação geral dos laudos
def avaliar_laudo(numero, pH, turbidez, coliformes):
    status_ph, motivo_ph = validar_ph(pH, pH_limite_minimo,pH_limite_maximo)
    status_turbidez, motivo_turbidez = validar_turbidez(turbidez,turbidez_limite_maximo)
    status_coliformes, motivo_coliformes = validar_coliformes(coliformes) 

    #Retorna o status geral dos laudos
    if status_ph == "Reprovado" or status_turbidez == "Reprovado" or status_coliformes == "Reprovado":
        status_geral = "Reprovado"
    else:
        status_geral = "Aprovado"


    print("\n" + "="*90)
    print(f"Laudos: {numero}")
    print(f"PH:         |{status_ph} | Ph {pH} {motivo_ph}"), #formatção de texto
    print(f"Turbidez:   |{status_turbidez} | Turbidez {turbidez} NTU{motivo_turbidez}") #formatção de texto
    print(f"Coliformes: |{status_coliformes}| Coliformes Totais: {motivo_coliformes}") #formatção de texto
    print(f"Status:      {status_geral}")
    print("="*90)

    return status_geral

# Função para gerar Resumo
def gerar_resumo(total,aprovados,reprovados):
    taxaprovacao = (aprovados /total)*100

    #define o risco
    if taxaprovacao == 100:
        risco = "Baixo"
        situacao = "Normal - Todos os laudos dentro do padrão"
    elif taxaprovacao >=60:
        risco = "Médio"
        situacao = "Atenção - Parte dos laudos fora do padrão"
    else: 
        risco = "Alto"
        situacao = "Crítico - Maioria dos laudos fora do padrão"

    acao = recomendar_acao(risco)

    print("\n" + "="*90)
    print(f"RESUMO EXECUTIVO")    
    print("="*90)
    print(f"Total de laudos  : {total}")
    print(f"Aprovados        : {aprovados}")
    print(f"Reprovados       : {reprovados}")
    print(f"Taxa de aprovação: {taxaprovacao:.1f}%")
    print(f"Risco geral      : {risco}")
    print(f"Situação         : {situacao}")
    print("="*90)
    print(f"Ação recomendada: {acao}")
    print("="*90)
   

aprovados = 0
reprovados = 0

#Imprime todos os laudos
for laudo in laudos: 
    resultado = avaliar_laudo(
        laudo['numero'],
        laudo['pH'],
        laudo['Turbidez'],
        laudo['coliformes'],
    )
    if resultado == "Aprovado":
        aprovados += 1
    else:
        reprovados += 1

# Gera o relatório final
gerar_resumo(len(laudos), aprovados, reprovados)