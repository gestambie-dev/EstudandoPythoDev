
def calcular_taxa(aprovados, total):
    if total == 0:
        return 0.0
    return aprovados / total *100

def classificar_risco(taxa_aprovação):
    if taxa_aprovação >= 80:
        return "Baixo", "Maioria dos psrâmetros dentro do padrão"
    elif taxa_aprovação >= 50:
        return "Médio", "Ateção - parte dos laudos fora do padrão"
    else:
        return "Alto", "Situação critica - maioria reprovada"
    
def gerar_resumo(total, aprovados, reprovados):
    taxa = calcular_taxa(aprovados, total)
    risco, descricao = classificar_risco(taxa)

    print("=" * 50)
    print(f"  RESUMO EXECUTIVO")
    print("=" * 50)
    print(f"  Total analisados : {total}")
    print(f"  Aprovados        : {aprovados}")
    print(f"  Reprovados       : {reprovados}")
    print(f"  Taxa de aprovação: {taxa:.1f}%")
    print(f"  Nível de risco   : {risco}")
    print(f"  Situação         : {descricao}")
    print("=" * 50)    

    return taxa, risco

# simulando resultados de um lote de laudos

total = 10
aprovados = 4
reprovados = 6

taxa_final, risco_final = gerar_resumo(total, aprovados, reprovados)

# usando os valores retornados para uma decisão
if risco_final == "Alto":
    print("\nAção nescessária: notificar responsável técnico")