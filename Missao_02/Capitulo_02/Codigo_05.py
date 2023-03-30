#importação do OpenCV
import cv2
#leitura da imagem
imagem = cv2.imread('ponte.jpg')
#laços que percorrem as linhas e colunas
for y in range(0, imagem.shape[0], 10): 
    for x in range(0, imagem.shape[1], 10):
        #substituição dos valores dos canais do pixel
        imagem[y:y+5, x: x+5] = (0,255,255)
#vizualização da imagem modificada    
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)