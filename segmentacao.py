import numpy as np

def otsu(imagem):
    
    # Verifica se a imagem é colorida e converte para escala de cinza
    if len(imagem.shape) > 2:
        imagem = imagem[:, :, 0]  # Usa apenas o primeiro canal (vermelho) para escala de cinza
    
    # Obtém as dimensões da imagem
    altura, largura = imagem.shape
    
    # Cria a imagem binária de retorno com o mesmo tamanho da imagem original
    imagemRetorno = np.zeros((altura, largura))
    
    # Calcula o histograma da imagem
    hist, _ = np.histogram(imagem, bins=256, range=(0, 256))
    
    # Normaliza o histograma para obter as probabilidades
    prob = hist / hist.sum()
    
    # Inicializa variáveis para o cálculo do limiar ótimo
    limiar_otimo = 0
    variancia_max = 0
    
    # Itera sobre todos os possíveis limiares
    for k in range(1, 255):
        
        # Probabilidade acumulada da classe 1
        probAcumulada = np.sum(prob[:k])
        
        # Média acumulada da classe 1
        if probAcumulada > 0:
            medAcumulada = np.sum(np.arange(k) * prob[:k]) / probAcumulada
        else:
            medAcumulada = 0
        
        # Média global da imagem
        mediaGlobal = np.mean(imagem)
        
        # Calcula a variância entre as classes
        q = probAcumulada * (1 - probAcumulada)
        if q == 0:  # Evita divisão por zero
            continue
        
        variancia = ((mediaGlobal * probAcumulada - medAcumulada) ** 2) / q
        
        # Atualiza o limiar ótimo se a variância for maior
        if variancia > variancia_max:
            variancia_max = variancia
            limiar_otimo = k
    
    # Cria a imagem binária com base no limiar ótimo
    for x in range(altura):
        for y in range(largura):
            if imagem[x, y] > limiar_otimo:
                imagemRetorno[x, y] = 0
            else:
                imagemRetorno[x, y] = 1
    
    return imagemRetorno