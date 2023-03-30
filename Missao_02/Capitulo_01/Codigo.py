#importação do OpenCV
import cv2
#leitura da imagem
imagem = cv2.imread('Entrada.jpg')
#vizualização das informações
print('Largura em pixels: ', end='')
print(imagem.shape[1]) 
print('Altura em pixels: ', end='')
print(imagem.shape[0]) 
print('Qtde de canais: ', end='')
print(imagem.shape[2])
#vizualização da imagem
cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0)
# Salva a imagem
cv2.imwrite("saida.jpg", imagem)