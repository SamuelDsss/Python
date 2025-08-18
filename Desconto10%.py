print("Desconto de 10% em Compras acima de R$ 100")
tu = float(input("Digite o valor da Compra: "))
if tu > 100 :
    tu = tu - (tu * 0.10)
    print(tu)
else :
    print("Não tera desconto ")
