##
# \brief Esta classe implementa um bloco genérico
class Bloco:
    ##
    # \brief Construtor. Apenas inicializa as coordenadas da peça como 0 e atribui uma matriz onde a peça será colocada
    def __init__(self, matriz_referencia):
        self.matriz_referencia = matriz_referencia
        self.coordenadas = [0, 0, 0, 0, 0, 0, 0, 0]



 