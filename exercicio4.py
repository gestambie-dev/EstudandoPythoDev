# Funções em Python
# Funções de validação de laudos

"""Exercício do dia
Adicione uma nova função chamada `gerar_resumo_executivo()` que recebe o total, 
aprovados e reprovados e imprime o bloco final de resumo. 
O objetivo é tirar essa lógica do corpo principal e colocar numa função.
O corpo principal do programa deve ficar limpo — apenas o loop e a chamada da função de resumo."""

# 1º Lista de laudos
laudos = ["aprovados", "reprovados", "aprovados", "reprovados"]

# 2º Inicialização das variáveis
aprovados = 0 
reprovados = 0

# 3º Laço for 
for laudo in laudos:
    
    if laudo == "aprovados":
        aprovados += 1
    else:
        reprovados += 1

# 4º Contagem dos itens da lista
total = len(laudos)

# Função 
def resumo_executivo(total, aprovado, reprovado):      
    print("==============================================")
    print(f"Total analisado   : {total}")
    print(f"Total aprovados   : {aprovado}")
    print(f"Total reprovados  : {reprovado}")
    print(f"Taxa de aprovação: {aprovado/total*100:.2f}%")
    print("==============================================")


resumo_executivo(total, aprovados, reprovados)