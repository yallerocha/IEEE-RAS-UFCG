import cv2
import mediapipe as mp

class HandNumbers:
        
    def start(self, camIndex):
        video = cv2.VideoCapture(camIndex)

        hands = mp.solutions.hands
        Hands = hands.Hands(max_num_hands=2)
        mpDwaw = mp.solutions.drawing_utils

        while True:
            success, frame = video.read()
            frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            results = Hands.process(frameRGB)
            height, width, _  = frame.shape
            handsLandmarks = results.multi_hand_landmarks 

            if handsLandmarks:
                raisedFingers = 0
                for Landmarks in handsLandmarks:
                    keyPoints = []
                    for cord in Landmarks.landmark:
                        world_x, world_y = int(cord.x * width), int(cord.y * height)
                        keyPoints.append((world_x, world_y))
                    
                    if self.__handUp(keyPoints):
                        mpDwaw.draw_landmarks(frame, Landmarks, hands.HAND_CONNECTIONS)
                        
                        fingersTips = [8, 12, 16, 20]         
                        for tip in fingersTips:
                            if self.__fingerUp(keyPoints,tip):
                                raisedFingers += 1
                    
                        if keyPoints[4][0] < keyPoints[17][0]:
                            if keyPoints[4][0] < keyPoints[3][0]:
                                raisedFingers += 1
                        else:
                            if keyPoints[4][0] > keyPoints[3][0]:
                                raisedFingers += 1

                cv2.rectangle(frame, (80, 10), (300, 110), (255, 255, 255), -1)
                cv2.putText(frame, str(raisedFingers), (100, 100), 
                            cv2.FONT_HERSHEY_DUPLEX, 4, (0, 0, 255), 5)

            cv2.imshow('Frame', frame)
            cv2.waitKey(1)

    def __handUp(self, keyPoints):
            if keyPoints[0][1] < keyPoints[2][1]:
                return False
            elif keyPoints[1][1] < keyPoints[17][1]:
                return False
            else:
                return True

    def __fingerUp(self, keyPoints, tip):
        if keyPoints[tip][1] < keyPoints[tip-2][1]:
            return True
        else:
            return False
        
a = HandNumbers()
a.start(0)

