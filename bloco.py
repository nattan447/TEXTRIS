class Bloco:
    def __init__(self, matriz_referencia):
        self.matriz_referencia = matriz_referencia
        self.estado_bloco = "lying"
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
        
        self.__linha_inicial = self.coordenadas[0]
        self.__linha_final = self.coordenadas[6]
        self.__coluna_inicial = self.coordenadas[1]
        self.__coluna_final = self.coordenadas[7]
      
    def rotacionar_esquerda(self):
        print("rotacionando para esquerda")
        pass


    def rotacionar_direita(self):
        print("irotacionando para diereita")
        pass
    
    def ir_baixo(self):
        """
        move peca para baixo e retorna true , se nao for possivel retorna false
        """
        if self.estado_bloco=="lying":
            for i in range(self.__coluna_inicial,self.__coluna_final+1): #verifico se tem como ir para baixo
                if self.matriz_referencia[self.__linha_inicial+1][i]!=" ":return False
            for i in range(self.__coluna_inicial,self.__coluna_final+1): #movo a peca para bnaixo
                self.matriz_referencia[self.__linha_inicial][i]=" "
                self.matriz_referencia[self.__linha_inicial+1][i]="*"
        else:
            if self.matriz_referencia[self.__linha_final][self.__coluna_inicial]!=" ": return False #verifico se tem como ir para baixo
            for l in range(self.__linha_inicial,self.__linha_final+2):
                j = " "
                guarda = self.matriz_referencia[i][self.__coluna_inicial]
                self.matriz_referencia[i][self.__coluna_inicial]= j #movo a peca para bnaixo
                j = guarda
        for i in range(0,len(self.coordenadas),2): #atualizo as cordenadas
            self.coordenadas[i]+=1
        return True
      




        # if(self.coordenadas[0] + 1 == self.coordenadas[2] and self.coordenadas[6] + 1 != " "):   #se ele está em pé e a linha de baixo da última linha do bloco não 
        #     return False                                                                         #está vazia, não dá pra mexer

        # elif(not(self.coordenadas[0] + 1 == self.coordenadas[2]) and (self.matriz_referencia[self.coordenadas[0] + 1][self.coordenadas[1]] != " " or  
        # self.matriz_referencia[self.coordenadas[2] + 1][self.coordenadas[3]] != " " or           #se o bloco está deitado e, pelo menos uma posição abaixo de qualquer                
        # self.matriz_referencia[self.coordenadas[4] + 1][self.coordenadas[5]] != " " or           #elemento da linha não está vazio, então não dá para mexer
        # self.matriz_referencia[self.coordenadas[6] + 1][self.coordenadas[7]] != " ")):
        #     return False

        # self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1]] = " "      #limpo as posições onde a peça estava anteriormente
        # self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3]] = " "
        # self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5]] = " "
        # self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7]] = " "

        # i = 0
        # while(i < len(self.coordenadas)):                           #atualizo as coordenadas para a linha de baixo
        #     self.coordenadas[i] = self.coordenadas[i] + 1           
        #     i = i + 2  

        # self.matriz_referencia[self.coordenadas[0]][self.coordenadas[1]] = "*"      #coloco a peça na sua nova posição
        # self.matriz_referencia[self.coordenadas[2]][self.coordenadas[3]] = "*"
        # self.matriz_referencia[self.coordenadas[4]][self.coordenadas[5]] = "*"
        # self.matriz_referencia[self.coordenadas[6]][self.coordenadas[7]] = "*"

        return True 

    def ir_esquerda(self):
        print("Indo para a esquerda")
        pass
    def ir_direita(self):
        print("Indo para a direita")
        pass




 