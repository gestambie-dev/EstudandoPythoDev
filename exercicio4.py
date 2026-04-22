# Funções em Python
# Funções de validação de laudos

"""Exercício do dia
Adicione uma nova função chamada `gerar_resumo_executivo()` que recebe o total, 
aprovados e reprovados e imprime o bloco final de resumo. 
O objetivo é tirar essa lógica do corpo principal e colocar numa função.
O corpo principal do programa deve ficar limpo — apenas o loop e a chamada da função de resumo."""


laudos = ["aprovados", "reprovados", "aprovados", "reprovados"]

aprovados = 0
reprovados = 0

for laudo in laudos:
    
    if laudo == "aprovados":
        aprovados += 1
    else:
        reprovados += 1

total = len(laudos)

def resumo_executivo(total, aprovado, reprovado):      
    print("==============================================")
    print(f"Total analisado   : {total}")
    print(f"Total aprovados   : {aprovado}")
    print(f"Total reprovados  : {reprovado}")
    print(f"Taxa de aprovação: {aprovado/total*100:.2f}%")
    print("==============================================")


resumo_executivo(total, aprovados, reprovados)