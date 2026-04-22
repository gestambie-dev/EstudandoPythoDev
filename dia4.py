# Funções em Python
# Funções de validação de laudos

def validar_ph(pH, limite_minino = 6.0, limite_maximo = 9.0):
    if pH < limite_minino:
        return "REPROVADO", f"ph {pH} abaixo do limite minimo({limite_minino})"
    elif pH > limite_maximo:
        return "REPROVADO", f"pH {pH} acima do limite máximo ({limite_maximo})"
    else:
        return "APROVADO", f"pH {pH} dentro dos parâmetros legais"
    

def validar_turbidez(turbidez, limite=100):
    if turbidez > limite:
        return "REPROVADO", f"Turbidez {turbidez} NTU acima do limite ({limite})"
    else:
        return "APROVADO", f"Turbidez {turbidez} NTU dentro dos parâmetros"

def validar_coliformes(presenca):
    if presenca:
        return "REPROVADO", "Coliformes totais: PRESENTE" 
    else:
        return "APROVADO", "Coliformes totais: AUSENTE" 

def validar_laudo(numero, pH, turbidez, coliformes):
    status_pH, motivo_pH = validar_ph(pH)
    status_turbidez, motivo_turbidez = validar_turbidez(turbidez)
    status_coliformes, motivo_coliformes = validar_coliformes(coliformes)

    if status_pH == "APROVADO" and status_turbidez == "APROVADO" and status_coliformes == "APROVADO":
        status_geral = "APROVADO"
    else:
        status_geral = "REPROVADO"

    print(f"\nLaudo: {numero}")
    print(f" pH               | {status_pH} | {motivo_pH}")
    print(f" Turbidez         | {status_turbidez} |{motivo_turbidez}")
    print(f" Coliformes       | {status_coliformes} | {motivo_coliformes}")
    print(f" Status Geral     | {status_geral}")

    return status_geral        

# Testando com os laudos que você já conhece
laudos = [
    {"numero": "LAB-2026-00310", "pH": 7.2, "Turbidez": 80,  "Coliformes": False},
    {"numero": "LAB-2026-00311", "pH": 5.1, "Turbidez": 45,  "Coliformes": False},
    {"numero": "LAB-2026-00312", "pH": 9.4, "Turbidez": 120, "Coliformes": True},
    {"numero": "LAB-2026-00313", "pH": 6.8, "Turbidez": 60,  "Coliformes": False},
    {"numero": "LAB-2026-00314", "pH": 8.1, "Turbidez": 95,  "Coliformes": False},
]

aprovados = 0
reprovados = 0

print("=========================ANALISE DE LAUDOS========================")

for laudo in laudos:
    resultado = validar_laudo(
        laudo["numero"],
        laudo["pH"],
        laudo["Turbidez"],
        laudo["Coliformes"]

    )
    if resultado == "APROVADO":
        aprovados += 1
    else:
        reprovados += 1

total = len(laudos)
print("===================================================================")
print(f"Total analisados : {total}")
print(f"Total aprovados : {aprovados}")
print(f"Total reprovados: {reprovados}")
print(f"Taxa de aprovação : {aprovados/total*100:.2f}%")
print("===================================================================")
