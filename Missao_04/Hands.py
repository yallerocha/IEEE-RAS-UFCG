import cv2
import mediapipe as mp

def main():
    handNumbers = HandNumbers()
    handNumbers.start(0)

class HandNumbers:
        
    def start(self, cam):
        video = cv2.VideoCapture(cam)

        hands = mp.solutions.hands
        Hands = hands.Hands(max_num_hands = 2)
        mpDraw = mp.solutions.drawing_utils

        while True:
            success, frame = video.read()
            frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            results = Hands.process(frameRGB)
            handsLandmarks = results.multi_hand_landmarks

            if handsLandmarks != None:
                totalOpenFingers = 0
                
                for Landmarks in handsLandmarks:
                    worldKeyPoints = self.__worldKeyPoints(frame, Landmarks.landmark)
                    
                    if self.__handUp(worldKeyPoints) == True:
                        mpDraw.draw_landmarks(frame, Landmarks, hands.HAND_CONNECTIONS)
                        totalOpenFingers += self.__fingersOpen(worldKeyPoints)
                            
                self.__digitalDisplay(frame, totalOpenFingers)

            cv2.imshow('Frame', frame)
            cv2.waitKey(1)
            
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