from PIL import Image
import numpy as np

# convertendo imagem para grayscale
image = Image.open("tuc.jpg").convert("L")

# transformando imagem em uma matrix 2D pelo numpy (isso porque estamos usando uma imagem em escala de cinza)
gray_matrix = np.array(image)

# criando uma imagem a partir da matriz
gray_image_from_matrix = Image.fromarray(gray_matrix.astype(np.uint8))

gray_image_from_matrix.save("tuc_gray_from_matrix.jpg")
print("Imagem em grayscale feita: tuc_gray_from_matrix.jpg")
