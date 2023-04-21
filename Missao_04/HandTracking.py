import cv2
import mediapipe as mp

def main():
    handTracking = HandTracking()
    handTracking.start(0)

class HandTracking:
    
    #Funcao que inicia o tracking das maos:   
    def start(self, cam):
        #Variavel que guarda o endereco da camera a ser utilizada:
        video = cv2.VideoCapture(cam)
        #Variavel que guarda a solution hands do MediaPipe, que possibilita trabalhar com o tracking de maos:
        hands = mp.solutions.hands
        #Configura a solution para detectar no maximo duas maos:
        Hands = hands.Hands(max_num_hands = 2)
        #Variavel que guarda a solution responsavel pela representação visual dos resultados do tracking:
        mpDraw = mp.solutions.drawing_utils

        while True:
            #Leitura do frame do video:
            success, frame = video.read()
            #Conversao do frame de BGR para RGB, para que possa ser processado:
            frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            #Variavel que guarda os resultados do processamento do frame:
            results = Hands.process(frameRGB)
            #Variavel que guarda os landmarks de cada mao processada:
            handsLandmarks = results.multi_hand_landmarks
            
            #Verifica se houve processamento de maos no frame, caso não, o loop segue normalmente:
            if handsLandmarks != None:
                #Variavel que guarda o numero total de dedos abertos nas maos:
                totalOpenFingers = 0
                #Laço que itera sobre os Landmarks (Objetos) de cada mao:
                for Landmarks in handsLandmarks:
                    #Variavel que gurda as coordenadas globais de cada ponto de tracking da mao:
                    worldKeyPoints = self.__worldKeyPoints(frame, Landmarks.landmark)
                    
                    #Verifica se a mao esta para cima, para garantir o funcionamento correto do codigo:
                    if self.__handUp(worldKeyPoints) == True:
                        #Desenha os pontos e as conexoes entre os pontos de tracking no frame:
                        mpDraw.draw_landmarks(frame, Landmarks, hands.HAND_CONNECTIONS)
                        #Atribuicao da quantidade de dedos abertos na mao analisada:
                        totalOpenFingers += self.__fingersOpen(worldKeyPoints)
                        
                #Adiciona um display no frame que mostra o numero total de dedos abertos:           
                self.__digitalDisplay(frame, totalOpenFingers)
            
            #Vizualização do frame com as informações adicionadas:
            cv2.imshow('Frame', frame)
            cv2.waitKey(1)
    
    #       
    def __worldKeyPoints(self, frame, landmark):
        height, width, _  = frame.shape
        worldKeyPoints = []
        
        for cord in landmark:
            x, y = int(cord.x * width), int(cord.y * height)
            worldKeyPoints.append((x, y))
        
        return worldKeyPoints

    def __handUp(self, keyPoints):
        if keyPoints[0][1] < keyPoints[2][1]:
            return False
        elif keyPoints[1][1] < keyPoints[17][1]:
            return False
        else:
            return True

    def __fingersOpen(self, keyPoints):
        fingersOpen = 0
        
        fingersTips = [8, 12, 16, 20]     
        for tip in fingersTips:
            if keyPoints[tip][1] < keyPoints[tip-2][1]:
                fingersOpen += 1
        
        if keyPoints[4][0] < keyPoints[17][0]:
            if keyPoints[4][0] < keyPoints[3][0]:
                fingersOpen += 1
        elif keyPoints[4][0] > keyPoints[3][0]:
            fingersOpen += 1
                
        return fingersOpen
    
    def __digitalDisplay(self, frame, totalOpenFingers):
        cv2.rectangle(frame, (0, 0), (220, 120), (0, 200, 0), -1)
        cv2.putText(frame, str(totalOpenFingers), (20, 100), cv2.FONT_HERSHEY_DUPLEX, 4, (255, 255, 255), 5)

if __name__ == "__main__":
    main()