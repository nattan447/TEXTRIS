from blocos.bloco import Bloco

##
# \brief Esta classe implementa um bloco do tipo I
class BlocoI(Bloco):
    ##
    # \brief gera uma peça nas coordenadas atuais. Caso elas sejam 0, gera uma peça na posição inicial do jogo
    # \return True caso conseguiu gerar a peça, ou False caso não conseguiu
    def gerarBloco(self):
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

        if(self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1]] != " " or
        self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3]] != " " or
        self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5]] != " " or
        self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7]] != " "):
            return False

        self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1]] = "*"
        self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3]] = "*"
        self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5]] = "*"
        self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7]] = "*"
        return True

    ##
    # \brief apaga a peça que está nas coordenadas atuais
    # \return nenhum
    def apagaBloco(self):
        self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1]] = " "
        self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3]] = " "
        self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5]] = " "
        self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7]] = " "

    ##
    # \brief rotaciona a peça atual para a esquerda
    # \return True caso conseguiu rotacionar a peça, ou False caso não conseguiu  
    def rotacionar_esquerda(self):
        if(self.coordenadas[1] + 1 == self.coordenadas[3]):     #Caso em que a peça está deitada para a direita
            if(self.coordenadas[2] - 1 <= 0 or self.coordenadas[4] - 2 <= 0 or self.coordenadas[6] - 3 <= 0):       #Verifico se, após girar, a peça não sairá da tela
                return False
            elif(self.matriz_referencia[self.coordenadas[2] - 1][self.coordenadas[3] - 1] != " " or self.matriz_referencia[self.coordenadas[4] - 2][self.coordenadas[5] - 2] != " " or self.matriz_referencia[self.coordenadas[6] - 3][self.coordenadas[7] - 3] != " "):
                return False                                    #Verifico se está livre o espaço para a peça
            else:                                           
                self.apagaBloco()                           
                i = 1
                j = 2
                while(i < 4):                                               #Atualizo as coordenadas e gero um novo bloco
                    self.coordenadas[j] = self.coordenadas[j] - i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] - i
                    j = j + 2
                    i = i + 1
                self.gerarBloco()
                return True

        elif(self.coordenadas[0] - 1 == self.coordenadas[2]):   #Caso em que a peça está em pé
            if(self.coordenadas[3] - 1 <= 0 or self.coordenadas[5] - 2 <= 0 or self.coordenadas[7] - 3 <= 0):       #Verifico se, após girar, a peça não sairá da tela
                return False
            elif(self.matriz_referencia[self.coordenadas[2] + 1][self.coordenadas[3] - 1] != " " or self.matriz_referencia[self.coordenadas[4] + 2][self.coordenadas[5] - 2] != " " or self.matriz_referencia[self.coordenadas[6] + 3][self.coordenadas[7] - 3] != " "):
                return False                                                #Verifico se está livre o espaço para a peça
            else:                                           
                self.apagaBloco()
                i = 1
                j = 2
                while(i < 4):                                               #Atualizo as coordenadas e gero um novo bloco
                    self.coordenadas[j] = self.coordenadas[j] + i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] - i
                    i = i + 1
                    j = j + 2
                self.gerarBloco()
                return True

        elif(self.coordenadas[1] - 1 == self.coordenadas[3]):  #Caso em que a peça está deitada para a esquerda
            if(self.coordenadas[2] + 1 >= len(self.matriz_referencia) - 1 or self.coordenadas[4] + 2 >= len(self.matriz_referencia) - 1 or self.coordenadas[6] + 3 >= len(self.matriz_referencia) - 1): #Verifico se, após girar, a peça não sairá da tela
                return False
            elif(self.matriz_referencia[self.coordenadas[2] + 1][self.coordenadas[3] + 1] != " " or self.matriz_referencia[self.coordenadas[4] + 2][self.coordenadas[5] + 2] != " " or self.matriz_referencia[self.coordenadas[6] + 3][self.coordenadas[7] + 3] != " "):
                return False                                                #Verifico se está livre o espaço para a peça
            else:                                           
                self.apagaBloco()
                i = 1
                j = 2
                while(i < 4):                                               #Atualizo as coordenadas e gero um novo bloco
                    self.coordenadas[j] = self.coordenadas[j] + i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] + i
                    j = j + 2
                    i = i + 1
                self.gerarBloco()
                return True

        elif(self.coordenadas[0] + 1 == self.coordenadas[2]):   #Caso em que a peça está de cabeça para baixo
            if(self.coordenadas[3] + 1 >= len(self.matriz_referencia[0])-1 or self.coordenadas[5] + 2 >= len(self.matriz_referencia[0] )-1 or self.coordenadas[7] + 3 >= len(self.matriz_referencia[0]))-1: #Verifico se, após girar, a peça não sairá da tela
                return False
            elif(self.matriz_referencia[self.coordenadas[2] - 1][self.coordenadas[3] + 1] != " " or self.matriz_referencia[self.coordenadas[4] - 2][self.coordenadas[5] + 2] != " " or self.matriz_referencia[self.coordenadas[6] - 3][self.coordenadas[7] + 3] != " "):
                return False                                                #Verifico se está livre o espaço para a peça
            else:
                self.apagaBloco()
                i = 1
                j = 2
                while(i < 4):                                               #Atualizo as coordenadas e gero um novo bloco
                    self.coordenadas[j] = self.coordenadas[j] - i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] + i
                    i = i + 1
                    j = j + 2
                self.gerarBloco()
                return True

    ##
    # \brief rotaciona a peça atual para a direita
    # \return True caso conseguiu rotacionar a peça, ou False caso não conseguiu 
    def rotacionar_direita(self):
        if(self.coordenadas[1] + 1 == self.coordenadas[3]):     #Caso em que a peça está deitada para a direita
            if(self.coordenadas[2] + 1 >= len(self.matriz_referencia) - 1 or self.coordenadas[4] + 2 >= len(self.matriz_referencia) - 1 or self.coordenadas[6] + 3 >= len(self.matriz_referencia) - 1):       #Verifico se, após girar, a peça não sairá da tela
                return False
            elif(self.matriz_referencia[self.coordenadas[2] + 1][self.coordenadas[3] - 1] != " " or self.matriz_referencia[self.coordenadas[4] + 2][self.coordenadas[5] - 2] != " " or self.matriz_referencia[self.coordenadas[6] + 3][self.coordenadas[7] - 3] != " "):
                return False
            else:                                           #Atualizo as coordenadas e gero um novo bloco
                self.apagaBloco()
                i = 1
                j = 2
                while(i < 4):
                    self.coordenadas[j] = self.coordenadas[j] + i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] - i
                    j = j + 2
                    i = i + 1
                self.gerarBloco()
                return True

        elif(self.coordenadas[0] - 1 == self.coordenadas[2]):   #Caso em que a peça está em pé
            if(self.coordenadas[3] + 1 >= len(self.matriz_referencia[0]) - 1 or self.coordenadas[5] + 2 >= len(self.matriz_referencia[0]) - 1 or self.coordenadas[7] + 3 >= len(self.matriz_referencia[0]) - 1):       #Verifico se, após girar, a peça não sairá da tela
                return False
            elif(self.matriz_referencia[self.coordenadas[2] + 1][self.coordenadas[3] + 1] != " " or self.matriz_referencia[self.coordenadas[4] + 2][self.coordenadas[5] + 2] != " " or self.matriz_referencia[self.coordenadas[6] + 3][self.coordenadas[7] + 3] != " "):
                return False
            else:                                           #Atualizo as coordenadas e gero um novo bloco
                self.apagaBloco()
                i = 1
                j = 2
                while(i < 4):
                    self.coordenadas[j] = self.coordenadas[j] + i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] + i
                    i = i + 1
                    j = j + 2
                self.gerarBloco()
                return True

        elif(self.coordenadas[1] - 1 == self.coordenadas[3]):  #Caso em que a peça está deitada para a esquerda
            if(self.coordenadas[2] - 1 <= 0 or self.coordenadas[4] - 2 <= 0 or self.coordenadas[6] - 3 <= 0): #Verifico se, após girar, a peça não sairá da tela
                return False
            elif(self.matriz_referencia[self.coordenadas[2] - 1][self.coordenadas[3] + 1] != " " or self.matriz_referencia[self.coordenadas[4] - 2][self.coordenadas[5] + 2] != " " or self.matriz_referencia[self.coordenadas[6] - 3][self.coordenadas[7] + 3] != " "):
                return False
            else:                                           #Atualizo as coordenadas e gero um novo bloco
                self.apagaBloco()
                i = 1
                j = 2
                while(i < 4):
                    self.coordenadas[j] = self.coordenadas[j] - i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] + i
                    j = j + 2
                    i = i + 1
                self.gerarBloco()
                return True

        elif(self.coordenadas[0] + 1 == self.coordenadas[2]):   #Caso em que a peça está de cabeça para baixo
            if(self.coordenadas[3] - 1 <= 0 or self.coordenadas[5] - 2 <= 0 or self.coordenadas[7] - 3 <= 0): #Verifico se, após girar, a peça não sairá da tela
                return False
            elif(self.matriz_referencia[self.coordenadas[2] - 1][self.coordenadas[3] - 1] != " " or self.matriz_referencia[self.coordenadas[4] - 2][self.coordenadas[5] - 2] != " " or self.matriz_referencia[self.coordenadas[6] - 3][self.coordenadas[7] - 3] != " "):
                return False
            else:
                self.apagaBloco()
                i = 1
                j = 2
                while(i < 4):
                    self.coordenadas[j] = self.coordenadas[j] - i
                    self.coordenadas[j + 1] = self.coordenadas[j + 1] - i
                    i = i + 1
                    j = j + 2
                self.gerarBloco()
                return True

    ##
    # \brief move a peça atual para baixo
    # \return True caso conseguiu mover a peça, ou False caso não conseguiu 
    def ir_baixo(self):
        if(self.coordenadas[0] + 1 == self.coordenadas[2]):
            if(self.matriz_referencia[self.coordenadas[6] + 1][self.coordenadas[7]] != " "):   
                self.coordenadas = [0, 0, 0, 0, 0, 0, 0, 0]                                          #se ele está de ponta cabeça e a linha de baixo da última linha do
                return False                                                                         #bloco não está vazia, então não podemos mexer  

        elif(self.coordenadas[0] - 1 == self.coordenadas[2]):
            if(self.matriz_referencia[self.coordenadas[0] + 1][self.coordenadas[1]] != " "):   
                self.coordenadas = [0, 0, 0, 0, 0, 0, 0, 0]                                          #se ele está em pé e a linha de baixo da última linha do
                return False                                                                         #bloco não está vazia, então não podemos mexer  
                 
        
        elif(self.coordenadas[0] == self.coordenadas[2]):
            if((self.matriz_referencia[self.coordenadas[0] + 1][self.coordenadas[1]] != " " or  
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

    ##
    # \brief move a peça atual para esquerda
    # \return True caso conseguiu mover a peça, ou False caso não conseguiu 
    def ir_esquerda(self):
        if(not(self.coordenadas[0] == self.coordenadas[2])):
            if((self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] - 1] != " " or  
            self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3] - 1] != " " or          #se ele está em pé e, pelo menos uma posição à esquerda de qualquer             
            self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5] - 1] != " " or          #elemento da linha não está vazio, então não dá para mexer
            self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] - 1] != " ")):
                return False

        elif(self.coordenadas[1] + 1 == self.coordenadas[3]):
            if(self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] - 1] != " "):       #se está deitado para direita e a posição ao lado do elemento mais à                                   
                return False                                                                       #esquerda não está vazia, então não dá para mexer
            
        elif(self.coordenadas[1] - 1 == self.coordenadas[3]):
            if(self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] - 1] != " "):       #se está deitado para esquerda e a posição ao lado do elemento mais à                                   
                return False                                                                       #esquerda não está vazia, então não dá para mexer

                                                                                                     
        
        self.apagaBloco()
        i = 1
        while(i < len(self.coordenadas)):                           #atualizo as coordenadas para a coluna do lado
            self.coordenadas[i] = self.coordenadas[i] - 1           
            i = i + 2  
        self.gerarBloco()

    ##
    # \brief move a peça atual para direita
    # \return True caso conseguiu mover a peça, ou False caso não conseguiu 
    def ir_direita(self):
        if(not(self.coordenadas[0] == self.coordenadas[2])):
            if((self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] + 1] != " " or  
            self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3] + 1] != " " or          #se ele está em pé e, pelo menos uma posição à esquerda de qualquer             
            self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5] + 1] != " " or          #elemento da linha não está vazio, então não dá para mexer
            self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] + 1] != " ")):
                return False

        elif(self.coordenadas[1] + 1 == self.coordenadas[3]):  
            if(self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7] + 1] != " "):      #se está deitado para direita e a posição ao lado do elemento mais à                                  
                return False                                                                      #direita não está vazia, então não dá para mexer
            
        elif(self.coordenadas[1] - 1 == self.coordenadas[3]):  
            if(self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1] + 1] != " "):      #se está deitado para esquerda e a posição ao lado do elemento mais à                                  
                return False                                                                      #direita não está vazia, então não dá para mexer
                                                                                                    
        self.apagaBloco()
        i = 1
        while(i < len(self.coordenadas)):                           #atualizo as coordenadas para a coluna do lado
            self.coordenadas[i] = self.coordenadas[i] + 1           
            i = i + 2  
        self.gerarBloco()



        
