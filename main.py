import matplotlib.pyplot as plt
import argparse
import Segmentation.segmentacao as segmentacao
from rich.console import Console
from rich.progress import Progress
import Utils.utils_imagem as ut_img
import Utils.utils_code as ut_code
import numpy as np
import time
import Utils.library_checker as lib_checker

# Variáveis para passagem de argumentos via terminal
parser = argparse.ArgumentParser()

# Argumento para salvar a imagem na pasta de resultados
SAVE = parser.add_argument('--save', action='store_true', help='Salvar a imagem na pasta de resultados')
INFO = parser.add_argument('--info', action='store_true', help='Exibir o tempo de execução')
URL_IMAGE = parser.add_argument('--url', type=str, help='URL da imagem para usar no algoritmo')

def metodo_otsu(imagem_escolhida, tipo, args):
    
    # Inicializa a variável de tempo
    tempo_inicio = time.time()
    
    with Progress() as progress:
        
        # Adiciona uma tarefa barra de progresso
        task = progress.add_task("[cyan]Processando...", total=3)
        
        # Leitura da imagem
        progress.update(task, advance=1, description='[cyan]Lendo a imagem...')
        Imagem_Original = ut_img.leitura_Imagem('./imagens/{}'.format(imagem_escolhida))    

        time.sleep(1)

        # Binarização da imagem com o método de Otsu
        progress.update(task, advance=1, description='[cyan]Aplicando o método de Otsu...')
        Imagem_Binaria = segmentacao.otsu(Imagem_Original) 

        time.sleep(1)
        
        # Calcula o tempo de execução
        tempo_execucao = time.time() - tempo_inicio - 2

        # Realiza a plotagem das imagens
        progress.update(task, advance=1, description='[cyan]Plotando as imagens...')
        ut_img.plotagem_imagem(Imagem_Original, Imagem_Binaria)
    
    time.sleep(1)
    ut_code.clear_terminal()
    
    # Deleta a imagem baixada
    if args.url:
        ut_img.deletar_imagem(imagem_escolhida)
        
    # Exibe o tempo de execução
    if args.info:
        ut_code.print_infos_table(tempo_execucao, tipo, imagem_escolhida)
        
    # Salva a imagem na pasta de resultados
    if args.save:
        ut_img.salvar_imagem(Imagem_Binaria, './Resultados/{}_{}'.format(imagem_escolhida, tipo))
    

if __name__ == '__main__':
    
    # Verifica se o usuário passou uma URL de imagem
    args = parser.parse_args()
    
    # Verifica se todas as bibliotecas estão instaladas
    lib_checker.check_library()
    
    # Funções triviais
    ut_code.clear_terminal()
    ut_code.print_title()
    
    
    # Baixa a imagem da URL
    if args.url:
        ut_img.download_imagem(args)
    
    # Inicializa a console
    console = Console()
    
    # Lista as imagens disponíveis na pasta
    imagens_disponiveis = ut_img.lista_imagens_pasta('./imagens', console)
    
    # Escolhe uma imagem para aplicar o método de Otsu
    imagem_escolhida = ut_img.escolher_imagens(imagens_disponiveis, console)
    
    metodo_otsu(imagem_escolhida ,'otsu', args)