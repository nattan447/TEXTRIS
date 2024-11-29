class Bloco:
    def __init__(self,cordenas):
        self.__cordenadas = cordenas
    
    def gerarBloco(self,matriT):
        ##metade da linha
        midLinha = int ((len(matriT[0])-1)/2)
        print(midLinha)
        #nosssas linha do jogo comeca no indice 1
        matriT[1][midLinha] = "*"
        matriT[2][midLinha] = "*"
        matriT[3][midLinha] = "*"
        matriT[4][midLinha] = "*"




 