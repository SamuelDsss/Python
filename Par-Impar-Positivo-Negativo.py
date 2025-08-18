positivo = 0
negativo = 0
impares = 0
pares = 0

print("Descubra quantos numero são positivo, negativo, impar ou par?")
print("")
for i in range(5):
    nm = int(input("Digite um numero: "))
    if(nm >0):
        positivo = positivo + 1
    else:
        negativo = negativo + 1
    if(nm%2 == 0):
        impares = impares + 1
    else:
        pares = pares + 1 
        
print("")
print("Resultados")
print("")
print("positivo: ", positivo)
print("negativo: ", negativo)
print("impares:  ", impares)
print("pares:    ", pares)
