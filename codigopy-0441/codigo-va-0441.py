# Ramirez Azul NC 0441
# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os 
# ruta de la imagen
ruta_imagen = os.path.join(
    "img-original-0441",
    "lexus.jpg"
)

img = cv2.imread(ruta_imagen)
# Imagen
# Vamos a crear nuestra matriz principal
lexus = cv2.imread(ruta_imagen)
# print(lexus) muestra las matrices de la imagen
# convertit BGR a RGB  color rojo COLOR_BGR2RGB
lexus = cv2.cvtColor(lexus, cv2.COLOR_BGR2RGB)
# cv2.imshow(" lexus original 0441", lexus)
cv2.imshow("lexus color 0441", lexus)
cv2.waitKey(0) # tiempo de espera
cv2.destroyAllWindows() # destruye todas las ventanas en memoria

