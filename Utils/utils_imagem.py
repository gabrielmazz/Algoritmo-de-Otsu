import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

#leitura da imagem
def leitura_Imagem(nome):
    imagem = mpimg.imread(nome)
    return imagem

# Realiza a plotagem das imagens com o matplotlib
def plotagem_imagem(Imagem_Original, Imagem_Binaria):
    
    # Cria uma figura com dois subplots lado a lado
    fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(20, 30))
    
    # Exibe a imagem original no primeiro subplot
    ax1.imshow(Imagem_Original, cmap='gray')
    
    # Exibe a imagem binária no segundo subplot
    ax2.imshow(Imagem_Binaria, cmap='Greys')
    
    # Mostra a figura com os subplots
    plt.show()
    
def salvar_imagem(Imagem_Binaria, nome):
    plt.imsave(nome, Imagem_Binaria, cmap='Greys')