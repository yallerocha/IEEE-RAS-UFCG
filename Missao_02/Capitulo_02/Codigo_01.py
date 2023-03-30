#importação do OpenCV
import cv2
#leitura da imagem
imagem = cv2.imread('ponte.jpg')
#atribuição dos valores dos canais RGB
(b, g, r) = imagem[0, 0]
#vizualização dos valores
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)