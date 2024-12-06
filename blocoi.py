from bloco import Bloco


class BlocoI(Bloco):
    
    def gerarBloco(self):
        #metade da linha
        midLinha = int ((len(self.matriz_referencia[0])-1)/2)
    
        # nosssas linha do jogo comeca no indice 1
        self.matriz_referencia[1][midLinha] = "*"
        self.matriz_referencia[2][midLinha] = "*"
        self.matriz_referencia[3][midLinha] = "*"
        self.matriz_referencia[4][midLinha] = "*"

        