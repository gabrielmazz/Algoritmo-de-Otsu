import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from rich.console import Console
from rich.prompt import Prompt
import os
from PIL import Image
from io import BytesIO
import requests

# Leitura da imagem
def leitura_Imagem(nome):
    
    # Lê a imagem
    imagem = mpimg.imread(nome)
    
    # Retorna a imagem
    return imagem

# Realiza a plotagem das imagens com o matplotlib
def plotagem_imagem(Imagem_Original, Imagem_Binaria):
    
    # Cria uma figura com dois subplots lado a lado
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    
    # Exibe a imagem original no primeiro subplot
    axs[0].imshow(Imagem_Original, cmap='gray')
    axs[0].set_title('Imagem Original')
    
    # Exibe a imagem binária no segundo subplot
    axs[1].imshow(Imagem_Binaria, cmap='gray')
    axs[1].set_title('Imagem com Método de Otsu')
    
    # Remove os eixos dos subplots
    for ax in axs.flat:
        ax.set(xticks=[], yticks=[])
    
    # Mostra a figura com os subplots
    plt.show()
    
def salvar_imagem(Imagem_Binaria, nome):
    
    # Adicione uma extensão válida ao nome do arquivo
    if not nome.endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp')):
        nome += '.png'  # Ou qualquer outro formato desejado
        
    plt.imsave(nome, Imagem_Binaria, cmap='Greys')
    
def lista_imagens_pasta(pasta, console):
    # Lista as imagens disponíveis na pasta
    imagens = [f for f in os.listdir(pasta)]
    
    # Printa as imagens
    for i, imagem in enumerate(imagens):
        
        # Extrai o nome da imagem a sua extensão
        nome, extensao = os.path.splitext(imagem)
        
        if nome == "IMAGEM_BAIXADA_URL":  # Verifica se é a imagem_baixada
            console.print(f'{i+1}. [bold green]{nome}{extensao}[/bold green]')  # Imprime em verde
        else:
            console.print(f'{i+1}. {nome}{extensao}')  # Imprime normalmente
        
    return imagens

def escolher_imagens(imagens, console):
    
    # Escolhe uma imagem para aplicar o método de Otsu
    while True:
        escolha = int(Prompt.ask('Escolha uma imagem para aplicar o método de [bold purple]Otsu[/bold purple]', console=console))
        
        if escolha > 0 and escolha <= len(imagens):
            return imagens[escolha-1]
        else:
            console.print('Escolha inválida. Tente novamente.')

def download_imagem(args):
    
    # Baixa a imagem da URL
    response = requests.get(args.url)
    
    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        # Lê a imagem
        Imagem = Image.open(BytesIO(response.content))
        
        # Define o nome da imagem
        nome_imagem = "IMAGEM_BAIXADA_URL"  # Nome fixo
        extensao = args.url.split('.')[-1]  # Extrai a extensão da URL (ex: jpg, png, etc.)
        
        # Salva a imagem com o novo nome
        Imagem.save(f'./imagens/{nome_imagem}.{extensao}')
        
    else:
        console.print('Erro ao baixar a imagem. Tente novamente.')

def deletar_imagem(nome):
    
    # Deleta a imagem
    os.remove('./imagens/{}'.format(nome))