# informação de um laudo laboratotial

numero_laudo = "LAB-2024-00312"         #str - texto
nome_cliente = "Empresa Verde Ltda"     #str - texto
quantidade_amostras = 5                 # int - numero inteiro
resultado_ph = 6.8                      #float - numero decimal
laudo_aprovado = True                   #bool - verdadeiro ou falso

# imprimindo as informações
print("Laudo:", numero_laudo)
print("Cliente:", nome_cliente)
print("Amostras:", quantidade_amostras)
print("pH:", resultado_ph)
print("Aprovada:", laudo_aprovado)

print("****verificando os Tipos*******")
print(type(numero_laudo))
print(type(quantidade_amostras))
print(type(resultado_ph))
print(type(laudo_aprovado))
print("*******final*******")