# Informações de um laudo laboratorial

numero_laudo = "LAB-2025-00313"     # str - texto
nome_cliente = "Posto Lauro Ltda"  # str - texto
quantidade_amostra = 5              # int - numero inteiro
resultado_ph = 6.8                  # float - numero decimal
laudo_aprovado = True               # bool - verdadeiro ou falso




#imprimindo as informações
print("Imprimindo as informações do cliente")
print("Laudo:", numero_laudo)
print("Cliente:", nome_cliente)
print("Amostra:", quantidade_amostra)
print("pH:", resultado_ph)

if laudo_aprovado:
    print("Laudo Aprovado")
else: 
    print("Laudo Não aprovado.. Verificar")

# verificando a tipagem
print("--VERIFICANDO A TIPAGEM--")        
print("Numero do laudo, Type:", type(numero_laudo))
print("Quantidade de Amostras, Type:", type(quantidade_amostra))
print("Resultado pH, Type:", type(resultado_ph))
print("Laudo Aprovado, Type:", type(laudo_aprovado))
