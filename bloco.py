class Bloco:
    def __init__(self, matriz_referencia):
        self.matriz_referencia = matriz_referencia
        self.coordenadas = [0, 0, 0, 0, 0, 0, 0, 0]
        #self.coordenadas = [1, 8, 2, 8, 3, 8, 4, 8]
class BlocoI(Bloco):
    
    def gerarBloco(self):
        """
        essa função gera um bloco nas coordenadas específicas da tela
        """
        if(self.coordenadas == [0, 0, 0, 0, 0, 0, 0, 0]):               #se self.coordenadas = array de zeros, entao a peça ainda nao existe. Dessa forma, eu atualizo
            i = 0                                                       #suas coordenadas para a posição inicial
            midLinha = int ((len(self.matriz_referencia[0])-1)/2)
            while(i < len(self.coordenadas)):                           
                self.coordenadas[i] = 1        
                i = i + 2  
            i = 1 
            j = 0
            while(i < len(self.coordenadas)):                           
                self.coordenadas[i] = midLinha + j         
                i = i + 2  
                j = j + 1

        self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1]] = "*"
        self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3]] = "*"
        self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5]] = "*"
        self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7]] = "*"

    def apagaBloco(self):
        """
        essa função apaga um bloco nas coordenadas específicas da tela
        """
        self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1]] = " "
        self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3]] = " "
        self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5]] = " "
        self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7]] = " "
      
    def rotacionar_esquerda(self):
        print("rotacionando para esquerda")
        pass


    def rotacionar_direita(self):
        print("irotacionando para diereita")
        pass
    
    def ir_baixo(self):

        if(not(self.coordenadas[0] == self.coordenadas[2]) and self.matriz_referencia[self.coordenadas[6] + 1][self.coordenadas[7]] != " "):   
            self.coordenadas = [0, 0, 0, 0, 0, 0, 0, 0]                                          #se ele está em pé e a linha de baixo da última linha do bloco não
            return False                                                                         #está vazia, então não podemos mexer                   
        
        elif(self.coordenadas[0] == self.coordenadas[2] and (self.matriz_referencia[self.coordenadas[0] + 1][self.coordenadas[1]] != " " or   

        self.matriz_referencia[self.coordenadas[2] + 1][self.coordenadas[3]] != " " or           #se o bloco está deitado e, pelo menos uma posição abaixo de qualquer                
        self.matriz_referencia[self.coordenadas[4] + 1][self.coordenadas[5]] != " " or           #elemento da linha não está vazio, então não dá para mexer
        self.matriz_referencia[self.coordenadas[6] + 1][self.coordenadas[7]] != " ")):
            self.coordenadas = [0, 0, 0, 0, 0, 0, 0, 0]
            return False
        
        self.apagaBloco()
        i = 0
        while(i < len(self.coordenadas)):                           #atualizo as coordenadas para a linha de baixo
            self.coordenadas[i] = self.coordenadas[i] + 1           
            i = i + 2  
        self.gerarBloco()

        return True 

    def ir_esquerda(self):
        if(not(self.coordenadas[0] == self.coordenadas[2]) and (self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] - 1] != " " or  
        self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3] - 1] != " " or          #se ele está em pé e, pelo menos uma posição à esquerda de qualquer             
        self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5] - 1] != " " or          #elemento da linha não está vazio, então não dá para mexer
        self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] - 1] != " ")):
            return False

        elif(self.coordenadas[0] == self.coordenadas[2] and self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] - 1] != " "):                                         
            return False                                                                        #se está deitado e a posição ao lado do elemento mais à esquerda não
                                                                                                #está vazia, então não dá para mexer
        
        self.apagaBloco()
        i = 1
        while(i < len(self.coordenadas)):                           #atualizo as coordenadas para a coluna do lado
            self.coordenadas[i] = self.coordenadas[i] - 1           
            i = i + 2  
        self.gerarBloco()

    def ir_direita(self):
        if(not(self.coordenadas[0] == self.coordenadas[2]) and (self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] + 1] != " " or  
        self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3] - 1] != " " or          #se ele está em pé e, pelo menos uma posição à esquerda de qualquer             
        self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5] - 1] != " " or          #elemento da linha não está vazio, então não dá para mexer
        self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] - 1] != " ")):
            return False

        elif(self.coordenadas[0] == self.coordenadas[2] and self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] + 1] != " "):                                         
            return False                                                                        #se está deitado e a posição ao lado do elemento mais à direita não
                                                                                                #está vazia, então não dá para mexer
        
        self.apagaBloco()
        i = 1
        while(i < len(self.coordenadas)):                           #atualizo as coordenadas para a coluna do lado
            self.coordenadas[i] = self.coordenadas[i] + 1           
            i = i + 2  
        self.gerarBloco()





 