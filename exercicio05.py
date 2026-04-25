def calcular_taxa(aprovados, total):
    if total == 0:
        return 0
    return (aprovados / total) * 100

def classificar_risco(taxa_aprovação):
    if taxa_aprovação >= 80:
        return "Baixo", "Maioria dos parâmetros dentro do padrão"
    elif taxa_aprovação >= 50:
        return "Médio", "Atenção - parte dos laudos fora do padrão"
    else:
        return "Alto", "Situação critica - maioria reprovadda"

def gerar_resumo(total, aprovados, reprovados):
    taxa = calcular_taxa(aprovados, total)
    risco, descricao = classificar_risco(taxa)

    print("="*60)
    print(f" Resumo Executivo")
    print("="*60)
    print(f" Total analisadas: {total}")
    print(f" Aprovadas: {aprovados}")
    print(f" Reprovadas: {reprovados}")
    print(f" Taxa de aprovação: {taxa:.2f}%")
    print(f" Nível de Risco: {risco}")
    print(f" Situação: {descricao}")
    print("="*60)
    
    return taxa, risco

def recomendar_acao(risco):    
    if risco == "Alto":
        return "Alto","Suspender operação e acionar o laboratorio para reanalise"
    elif risco == "Médio":
        return "Medio","Monitorar o proximo lote com frequencia dobrada."
    else:
        return "Baixo", "Manter protocolo padrão de monitoramento."    
   
# Simulando resultados de um lote de laudos
# 
total = 10
aprovados = 4
reprovados = 6

taxa_final, risco_final = gerar_resumo(total, aprovados, reprovados)

#if risco_final == "Alto":
#    print("\nAção nescessaria : Notificar responsável tecnico.")

acao_necessaria = recomendar_acao(risco_final)
print(f"Ação Necessaria: {acao_necessaria}")


