import matplotlib
matplotlib.use('Agg')  # Usa backend sem interface gráfica
import matplotlib.pyplot as plt

def gerar_grafico():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    plt.plot(x, y, marker='o')
    plt.title('Gráfico Simples')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.savefig('grafico.png')
    print("Gráfico gerado com sucesso: grafico.png")

if __name__ == "__main__":
    gerar_grafico()
