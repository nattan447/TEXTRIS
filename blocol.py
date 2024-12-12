from bloco import Bloco


class BlocoL(Bloco):
    
    def gerarBloco(self):
        """
        essa função gera um bloco nas coordenadas específicas da tela
        """
        if(self.coordenadas == [0, 0, 0, 0, 0, 0, 0, 0]):               #se self.coordenadas = array de zeros, entao a peça ainda nao existe. Dessa forma, eu atualizo
            i = 1                                                       #suas coordenadas para a posição inicial
            midLinha = int ((len(self.matriz_referencia[0])-1)/2)
            while(i < len(self.coordenadas) - 1):                           
                self.coordenadas[i] = midLinha        
                i = i + 2  
            self.coordenadas[7] = midLinha + 1
            i = 0 
            j = 0
            while(i < len(self.coordenadas) - 1):                           
                self.coordenadas[i] = 1 + j         
                i = i + 2  
                j = j + 1
            self.coordenadas[6] = 3

        self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1]] = "#"
        self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3]] = "#"
        self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5]] = "#"
        self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7]] = "#"

    def apagaBloco(self):
        """
        essa função apaga um bloco nas coordenadas específicas da tela
        """
        self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1]] = " "
        self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3]] = " "
        self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5]] = " "
        self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7]] = " "
      
    def rotacionar_esquerda(self):
        if(self.coordenadas[5] + 1 == self.coordenadas[3]):     #Caso em que a peça está deitada para a direita
            if(self.coordenadas[0] - 2 <= 0):       #Verifico se é possível girar a peça
                return False
            elif(self.matriz_referencia[self.coordenadas[0] - 2][self.coordenadas[1] - 2] != " " or self.matriz_referencia[self.coordenadas[2] - 1][self.coordenadas[3] - 1] != " "):
                return False
            else:                                           #Atualizo as coordenadas e gero um novo bloco
                self.apagaBloco()
                i = 2
                j = 0
                while(i >= 1):
                    self.coordenadas[j] = self.coordenadas[j] - i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] - i
                    j = j + 2
                    i = i - 1
                self.coordenadas[6] = self.coordenadas[6] - 1
                self.coordenadas[7] = self.coordenadas[7] + 1
                self.gerarBloco()
                return True

        elif(self.coordenadas[4] - 1 == self.coordenadas[2]):   #Caso em que a peça está em pé
            if(self.coordenadas[1] - 2 <= 0):    #Verifico se é possível girar a peça
                return False
            elif(self.matriz_referencia[self.coordenadas[0] + 2][self.coordenadas[1] - 2] != " " or self.matriz_referencia[self.coordenadas[2] + 1][self.coordenadas[3] - 1] != " "):
                return False
            else:                                           #Atualizo as coordenadas e gero um novo bloco
                self.apagaBloco()
                i = 2
                j = 0
                while(i >= 1):
                    self.coordenadas[j] = self.coordenadas[j] + i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] - i
                    j = j + 2
                    i = i - 1
                self.coordenadas[6] = self.coordenadas[6] - 1
                self.coordenadas[7] = self.coordenadas[7] - 1
                self.gerarBloco()
                return True

        elif(self.coordenadas[5] - 1 == self.coordenadas[3]):  #Caso em que a peça está deitada para a esquerda
            if(self.coordenadas[0] + 2 >= len(self.matriz_referencia) - 1): #Verifico se é possível girar a peça
                return False
            elif(self.matriz_referencia[self.coordenadas[0] + 2][self.coordenadas[1] + 2] != " " or self.matriz_referencia[self.coordenadas[2] + 1][self.coordenadas[3] + 1] != " "):
                return False
            else:                                           #Atualizo as coordenadas e gero um novo bloco
                self.apagaBloco()
                i = 2
                j = 0
                while(i >= 1):
                    self.coordenadas[j] = self.coordenadas[j] + i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] + i
                    j = j + 2
                    i = i - 1
                self.coordenadas[6] = self.coordenadas[6] + 1
                self.coordenadas[7] = self.coordenadas[7] - 1
                self.gerarBloco()
                return True

        elif(self.coordenadas[4] + 1 == self.coordenadas[2]):   #Caso em que a peça está de cabeça para baixo
            if(self.coordenadas[1] + 2 >= len(self.matriz_referencia[0]) - 1): #Verifico se é possível girar a peça
                return False
            elif(self.matriz_referencia[self.coordenadas[0] - 2][self.coordenadas[1] + 2] != " " or self.matriz_referencia[self.coordenadas[2] - 1][self.coordenadas[3] + 1] != " "):
                return False
            else:
                self.apagaBloco()
                i = 2
                j = 0
                while(i >= 1):
                    self.coordenadas[j] = self.coordenadas[j] - i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] + i
                    j = j + 2
                    i = i - 1
                self.coordenadas[6] = self.coordenadas[6] + 1
                self.coordenadas[7] = self.coordenadas[7] + 1
                self.gerarBloco()
                return True

    def rotacionar_direita(self):
        if(self.coordenadas[5] + 1 == self.coordenadas[3]):     #Caso em que a peça está deitada para a direita
            if(self.coordenadas[0] + 2 >= len(self.matriz_referencia) - 1 or self.coordenadas[7] - 1 <= 0):       #Verifico se é possível girar a peça
                return False
            elif(self.matriz_referencia[self.coordenadas[0] + 2][self.coordenadas[1] - 2] != " " or self.matriz_referencia[self.coordenadas[6] - 1][self.coordenadas[7] - 1] != " "):
                return False
            else:                                           #Atualizo as coordenadas e gero um novo bloco
                self.apagaBloco()
                i = 2
                j = 0
                while(i >= 1):
                    self.coordenadas[j] = self.coordenadas[j] + i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] - i
                    j = j + 2
                    i = i - 1
                self.coordenadas[6] = self.coordenadas[6] - 1
                self.coordenadas[7] = self.coordenadas[7] - 1
                self.gerarBloco()
                return True

        elif(self.coordenadas[4] - 1 == self.coordenadas[2]):   #Caso em que a peça está em pé
            if(self.coordenadas[1] + 2 >= len(self.matriz_referencia[0]) - 1) or self.coordenadas[6] + 1 >= len(self.matriz_referencia) - 1:    #Verifico se é possível girar a peça
                return False
            elif(self.matriz_referencia[self.coordenadas[0] + 2][self.coordenadas[1] + 2] != " " or self.matriz_referencia[self.coordenadas[6] + 1][self.coordenadas[7] - 1] != " "):
                return False
            else:                                           #Atualizo as coordenadas e gero um novo bloco
                self.apagaBloco()
                i = 2
                j = 0
                while(i >= 1):
                    self.coordenadas[j] = self.coordenadas[j] + i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] + i
                    j = j + 2
                    i = i - 1
                self.coordenadas[6] = self.coordenadas[6] + 1
                self.coordenadas[7] = self.coordenadas[7] - 1
                self.gerarBloco()
                return True

        elif(self.coordenadas[5] - 1 == self.coordenadas[3]):  #Caso em que a peça está deitada para a esquerda
            if(self.coordenadas[0] - 2 <= 0 or self.coordenadas[7] + 1 >= len(self.matriz_referencia[0]) - 1): #Verifico se é possível girar a peça
                return False
            elif(self.matriz_referencia[self.coordenadas[0] - 2][self.coordenadas[1] + 2] != " " or self.matriz_referencia[self.coordenadas[6] + 1][self.coordenadas[7] + 1] != " "):
                return False
            else:                                           #Atualizo as coordenadas e gero um novo bloco
                self.apagaBloco()
                i = 2
                j = 0
                while(i >= 1):
                    self.coordenadas[j] = self.coordenadas[j] - i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] + i
                    j = j + 2
                    i = i - 1
                self.coordenadas[6] = self.coordenadas[6] + 1
                self.coordenadas[7] = self.coordenadas[7] + 1
                self.gerarBloco()
                return True

        elif(self.coordenadas[4] + 1 == self.coordenadas[2]):   #Caso em que a peça está de cabeça para baixo
            if(self.coordenadas[1] - 2 <= 0 or self.coordenadas[6] - 1 <= 0): #Verifico se é possível girar a peça
                return False
            elif(self.matriz_referencia[self.coordenadas[0] - 2][self.coordenadas[1] - 2] != " " or self.matriz_referencia[self.coordenadas[6] - 1][self.coordenadas[7] + 1] != " "):
                return False
            else:
                self.apagaBloco()
                i = 2
                j = 0
                while(i >= 1):
                    self.coordenadas[j] = self.coordenadas[j] - i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] - i
                    j = j + 2
                    i = i - 1
                self.coordenadas[6] = self.coordenadas[6] - 1
                self.coordenadas[7] = self.coordenadas[7] + 1
                self.gerarBloco()
                return True

    def ir_baixo(self):

        if(self.coordenadas[5] - 1 == self.coordenadas[7]):
            if(self.matriz_referencia[self.coordenadas[0] + 1][self.coordenadas[1]] != " " or self.matriz_referencia[self.coordenadas[6] + 1][self.coordenadas[7]] != " "):   
                self.coordenadas = [0, 0, 0, 0, 0, 0, 0, 0]                                          #se ele está de ponta cabeça e a linha de baixo da última linha dos
                return False                                                                         #blocos não está vazia, então não podemos mexer  

        elif(self.coordenadas[5] + 1 == self.coordenadas[7]):
            if(self.matriz_referencia[self.coordenadas[4] + 1][self.coordenadas[5]] != " " or self.matriz_referencia[self.coordenadas[6] + 1][self.coordenadas[7]] != " "):   
                self.coordenadas = [0, 0, 0, 0, 0, 0, 0, 0]                                          #se ele está em pé e a linha de baixo da última linha dos
                return False                                                                         #blocos não está vazia, então não podemos mexer  
                 
        
        elif(self.coordenadas[4] - 1 == self.coordenadas[6]):                         #Caso em que está deitado para esquerda e nao podemos mover para baixo
            if(self.matriz_referencia[self.coordenadas[0] + 1][self.coordenadas[1]] != " " or self.matriz_referencia[self.coordenadas[2] + 1][self.coordenadas[3]] != " " or self.matriz_referencia[self.coordenadas[4] + 1][self.coordenadas[5]] != " "):
                self.coordenadas = [0, 0, 0, 0, 0, 0, 0, 0]
                return False
            
        elif(self.coordenadas[4] + 1 == self.coordenadas[6]):                         #Caso em que está deitado para direita e nao podemos mover para baixo
            if(self.matriz_referencia[self.coordenadas[0] + 1][self.coordenadas[1]] != " " or self.matriz_referencia[self.coordenadas[2] + 1][self.coordenadas[3]] != " " or self.matriz_referencia[self.coordenadas[6] + 1][self.coordenadas[7]] != " "):
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
        if(self.coordenadas[5] - 1 == self.coordenadas[7]):                           #Caso em que está de ponta cabeça e nao podemos mover para esquerda
            if(self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] - 1] != " " or self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3] - 1] != " " or self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] - 1] != " "):   
                return False                           
                                                                                         

        elif(self.coordenadas[5] + 1 == self.coordenadas[7]):                         #Caso em que está em pé e nao podemos mover para esquerda  
            if(self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] - 1] != " " or self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3] - 1] != " " or self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5] - 1] != " "):   
                return False                                        
                                                                                       
        
        elif(self.coordenadas[4] - 1 == self.coordenadas[6]):                         #Caso em que está deitado para esquerda e nao podemos mover para esquerda
            if(self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] - 1] != " " or self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] - 1] != " "):
                return False 
                
            
        elif(self.coordenadas[4] + 1 == self.coordenadas[6]):                         #Caso em que está deitado para direita e nao podemos mover para esquerda
            if(self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5] - 1] != " " or self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] - 1] != " "):
                return False 
                                                                                                                                                                             
        self.apagaBloco()
        i = 1
        while(i < len(self.coordenadas)):                           #atualizo as coordenadas para a coluna do lado
            self.coordenadas[i] = self.coordenadas[i] - 1           
            i = i + 2  
        self.gerarBloco()

    def ir_direita(self):
        if(self.coordenadas[5] - 1 == self.coordenadas[7]):                           #Caso em que está de ponta cabeça e nao podemos mover para direita
            if(self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] + 1] != " " or self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3] + 1] != " " or self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5] + 1] != " "):   
                return False                           
                                                                                         

        elif(self.coordenadas[5] + 1 == self.coordenadas[7]):                         #Caso em que está em pé e nao podemos mover para direita  
            if(self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] + 1] != " " or self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3] + 1] != " " or self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] + 1] != " "):   
                return False                                        
                                                                                       
        
        elif(self.coordenadas[4] - 1 == self.coordenadas[6]):                         #Caso em que está deitado para esquerda e nao podemos mover para direita
            if(self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5] + 1] != " " or self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] + 1] != " "):
                return False 
                
            
        elif(self.coordenadas[4] + 1 == self.coordenadas[6]):                         #Caso em que está deitado para direita e nao podemos mover para direita
            if(self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] + 1] != " " or self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] + 1] != " "):
                return False
                                                                                                    
        self.apagaBloco()
        i = 1
        while(i < len(self.coordenadas)):                           #atualizo as coordenadas para a coluna do lado
            self.coordenadas[i] = self.coordenadas[i] + 1           
            i = i + 2  
        self.gerarBloco()