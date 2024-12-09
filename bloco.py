class Bloco:
    def __init__(self, matriz_referencia):
        self.matriz_referencia = matriz_referencia
        self.coordenadas = []

class BlocoI(Bloco):
    
    def gerarBloco(self):
        """
        essa função gera um bloco na parte inicial da tela
        """
        #metade da linha
        midLinha = int ((len(self.matriz_referencia[0])-1)/2)
    
        # nosssas linha do jogo comeca no indice 1
        self.matriz_referencia[1][midLinha] = "*"
        self.coordenadas.append(1)
        self.coordenadas.append(midLinha)

        self.matriz_referencia[1][midLinha + 1] = "*"
        self.coordenadas.append(1)
        self.coordenadas.append(midLinha+1)

        self.matriz_referencia[1][midLinha + 2] = "*"
        self.coordenadas.append(1)
        self.coordenadas.append(midLinha+2)

        self.matriz_referencia[1][midLinha + 3] = "*"
        self.coordenadas.append(1)
        self.coordenadas.append(midLinha+3)
      
    def rotacionar_esquerda(self):
        print("rotacionando para esquerda")
        pass


    def rotacionar_direita(self):
        print("irotacionando para diereita")
        pass
    
    def ir_baixo(self):


        if(self.coordenadas[0] + 1 == self.coordenadas[2] and self.coordenadas[6] + 1 != " "):   #se ele está em pé e a linha de baixo da última linha do bloco não 
            return False                                                                         #está vazia, não dá pra mexer

        elif(not(self.coordenadas[0] + 1 == self.coordenadas[2]) and (self.matriz_referencia[self.coordenadas[0] + 1][self.coordenadas[1]] != " " or  
        self.matriz_referencia[self.coordenadas[2] + 1][self.coordenadas[3]] != " " or           #se o bloco está deitado e, pelo menos uma posição abaixo de qualquer                
        self.matriz_referencia[self.coordenadas[4] + 1][self.coordenadas[5]] != " " or           #elemento da linha não está vazio, então não dá para mexer
        self.matriz_referencia[self.coordenadas[6] + 1][self.coordenadas[7]] != " ")):
            return False

        self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1]] = " "      #limpo as posições onde a peça estava anteriormente
        self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3]] = " "
        self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5]] = " "
        self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7]] = " "

        i = 0
        while(i < len(self.coordenadas)):                           #atualizo as coordenadas para a linha de baixo
            self.coordenadas[i] = self.coordenadas[i] + 1           
            i = i + 2  

        self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1]] = "*"      #coloco a peça na sua nova posição
        self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3]] = "*"
        self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5]] = "*"
        self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7]] = "*"

        return True 

    def ir_esquerda(self):
        print("Indo para a esquerda")
        pass
    def ir_direita(self):
        print("Indo para a direita")
        pass




 