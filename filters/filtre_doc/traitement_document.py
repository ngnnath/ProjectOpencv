import os, sys
import cv2
import numpy as np
# Get absolute path of current file
abs_path = os.path.abspath(os.path.dirname(__file__))

# Get image path from option
nom_img = sys.argv[1]

if os.path.isfile(nom_img) == False:
    sys.exit("Exit : file not found")
    
#chargement du fichier
img = cv2.imread(nom_img)

#fonction de seuillage // valeur de seuil 250
reval, threshold = cv2.threshold(img,250,255,cv2.THRESH_BINARY)
grayscaled =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
reval, threshold2 = cv2.threshold(grayscaled,112,255,cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)


cv2.imwrite(abs_path+"/resultat.png", gaus)
