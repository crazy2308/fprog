def QuadradoElementos(numeros):
    return [x ** 2 for x in numeros]

def SomatorioLista(numeros):
    return sum(numeros)

def ConverteEmNumeros(ListaCaracteres):
    return [float(x.strip()) for x in ListaCaracteres]

def main():
    nome_ficheiro = input("Nome do ficheiro com os números: ")

    try:
        with open(nome_ficheiro, 'r') as f:
            linhas = f.readlines()

        numeros = ConverteEmNumeros(linhas)
        quadrados = QuadradoElementos(numeros)
        soma = SomatorioLista(quadrados)

        print(f"Soma dos quadrados: {soma}")
    except FileNotFoundError:
        print("Ficheiro não encontrado.")
    except ValueError:
        print("Erro ao converter os dados. Verifique o conteúdo do ficheiro.")

if __name__ == "__main__":
    main()
