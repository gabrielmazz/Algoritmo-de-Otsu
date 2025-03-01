import matplotlib.pyplot as plt
import argparse

import utils
import filters
import bordas
import segmentacao

import Utils.utils_imagem as ut_img

# Variáveis para passagem de argumentos via terminal
parser = argparse.ArgumentParser()

# Argumento para salvar a imagem na pasta de resultados
SAVE = parser.add_argument('--save', action='store_true', help='Salvar a imagem na pasta de resultados')


def main(imagem, tipo, filtro, m, n):
    
    # Leitura da imagem
    Imagem_Original = ut_img.leitura_Imagem('./imagens/{}.jpg'.format(imagem))    

    # Binarização da imagem com o método de Otsu
    Imagem_Binaria = segmentacao.otsu(Imagem_Original) 
    
    # ImgFiltrada = bordas.Derivative(Imagem_Original,tipo, filtro,m,n)
    
    # limiar = 0.1*np.mean(ImgFiltrada)
    # Imagem_Binaria = utils.Threshold(ImgFiltrada,limiar)   

    ##--> OUTRO METODO DE BINARIZACAO
    # Imagem_Binaria = bordas.Canny(Imagem_Original,m,n) 


    # Realiza a plotagem das imagens
    ut_img.plotagem_imagem(Imagem_Original,Imagem_Binaria)
    
    # Salva a imagem na pasta de resultados
    if SAVE:
        ut_img.salvar_imagem(Imagem_Binaria, './resultados/{}_{}_{}_{}x{}.png'.format(tipo,imagem,filtro,m,n))

if __name__ == '__main__':
    
    main('imagem2','otsu','Gaussian', 0.3, 0.7)