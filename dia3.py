# Dia 3 loops

#Lista de Laudos com seus respectivos pH's

laudos = [
    {"Numero": "LAB-2026-00310","pH": 7.2},
    {"Numero": "LAB-2026-00311","pH": 5.1},
    {"Numero": "LAB-2026-00312","pH": 9.4},
    {"Numero": "LAB-2026-00313","pH": 6.8},
    {"Numero": "LAB-2026-00314","pH": 8.1},

]
limite_minimo = 6.0
limite_maximo = 9.0

aprovados = 0
reprovados = 0

print("============ANALISE DE LAUDOS===============")
for laudo in laudos:
    numero = laudo["Numero"]
    pH = laudo["pH"]

    if pH < limite_minimo or pH > limite_maximo:
        reprovados += 1
        status = "REPROVADO"
    else:
        aprovados += 1
        status = "APROVADO"
    print(f"{numero} | pH: {pH} | {status}")

taxa_aprovacao = aprovados/reprovados*100
print("=============================================")
total = len(laudos)
print(f"Total de laudos analisado: {total}")
print(f"total aprovados {aprovados}")
print(f"Total reprovados: {reprovados}")
print(f"Taxa de Aprovação: {aprovados}/{reprovados}*100")
print("=============================================")


