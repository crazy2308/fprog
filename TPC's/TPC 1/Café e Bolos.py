def main():
    preco_cafe = 2.50
    custo_por_kg = 0.86
    custo_fixo = 1.50
    iva = 0.23
    quilos = eval(input("Quantos quilos de café deseja encomendar? "))
    custo_cafe = quilos * preco_cafe
    custo_envio = (quilos * custo_por_kg) + custo_fixo
    subtotal = custo_cafe + custo_envio
    iva = subtotal * iva
    total = subtotal + iva

    print("--------- Fatura ----------")
    print("Quantidade de café:", quilos, "kg")
    print("Preço do café:" , custo_cafe, "€")
    print("Custo de envio:", custo_envio, "€")
    print("Subtotal:", subtotal, " €")
    print("IVA (23%):" , total, "€")
    print("Total a pagar:", total, "€")
    print("----------------------------")

main()

