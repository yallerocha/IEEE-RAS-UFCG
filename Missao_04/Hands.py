import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

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
            mpDwaw.draw_landmarks(frame, Landmarks, hands.HAND_CONNECTIONS)
            
            keyPoints = []
            for cord in Landmarks.landmark:
                cx, cy = int(cord.x * width), int(cord.y * height)
                keyPoints.append((cx, cy)) 
                        
            fingersTips = [8, 12, 16, 20]  
            for tip in fingersTips:
                if keyPoints[tip][1] < keyPoints[tip - 2][1]:
                    raisedFingers += 1
            
            if keyPoints[4][0] < keyPoints[17][0]:
                if keyPoints[4][0] < keyPoints[2][0]:
                    raisedFingers += 1
            else:
                if keyPoints[4][0] > keyPoints[2][0]:
                    raisedFingers += 1

        cv2.rectangle(frame, (80, 10), (300, 110), (255, 0, 0), -1)
        cv2.putText(frame, str(raisedFingers), (100, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5)

    cv2.imshow('Frame', frame)
    cv2.waitKey(1)
