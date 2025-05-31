def main():
    print()
    print("Este programa calcula a eficiência energética em termos de consumo de combustível de um automóvel que evetua vários trajetos.")
    print()

    with open("Odometro.txt", "r") as file:
        odometro_inicial = float(file.readline().strip())

        odometro_anterior = odometro_inicial
        distancia_total = 0
        combustivel_total = 0
        trajetos = 0

        for line in file:
            odometro_final, combustivel = map(float, line.split())

            distancia = odometro_final - odometro_anterior
            eficiencia = combustivel / distancia * 100

            print(f"Eficiência do Trajeto {trajetos + 1}: {eficiencia:.2f} litros/100 Km")

            odometro_anterior = odometro_final
            distancia_total += distancia
            combustivel_total += combustivel
            trajetos += 1

        eficiencia_total = combustivel_total / distancia_total * 100

        print(f"Eficiência energética média: {eficiencia_total:.2f} litros/100 Km")

main()