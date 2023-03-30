#importação do OpenCV
import cv2
#leitura da imagem
imagem = cv2.imread('ponte.jpg')
#laços que percorrem as linhas e colunas
for y in range(0, imagem.shape[0], 1): 
    for x in range(0, imagem.shape[1], 1):
        #substituição dos valores dos canais do pixel
        imagem[y, x] = (0,(x*y)%256,0)
#vizualização da imagem modificada
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
