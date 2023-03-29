import cv2
imagem = cv2.imread('ponte.jpg')
for y in range(0, imagem.shape[0], 1): #percorre as linhas
    for x in range(0, imagem.shape[1], 1): #percorre as colunas
        imagem[y, x] = (0,(x*y)%256,0)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
