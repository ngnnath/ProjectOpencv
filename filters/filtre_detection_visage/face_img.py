import os
import sys
import click
import cv2
import PIL
from PIL import Image
from shutil import copy

# Get absolute path of current file
abs_path = os.path.abspath(os.path.dirname(__file__))

# Get image path from option
nom_img = sys.argv[1]

print(nom_img)
DEFAULT_CASCADE_FOLDER = abs_path+'/'+'classifiers'
DEFAULT_FRONTAL_FACE_CLASSIFIER = abs_path+'/'+'classifiers'+'/'+'haarcascade_frontalface_default.xml'
DEFAULT_EYE_CLASSIFIER = abs_path+'/'+'classifiers'+'/'+'haarcascade_eyes.xml'


face_cascade=DEFAULT_FRONTAL_FACE_CLASSIFIER
eyes_cascade=DEFAULT_EYE_CLASSIFIER

# Define cascade classifiers
face_cascade = cv2.CascadeClassifier(face_cascade)
eye_cascade = cv2.CascadeClassifier(eyes_cascade)

	
nom_filtre="troll"

filtre = cv2.imread(nom_filtre+".png")
image_modif = cv2.imread(nom_img)
cv2.imwrite(abs_path+"/resultat.png", image_modif)
filtre_fond = cv2.imread(nom_filtre+"_fond.png")
frame= image_modif	

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces_data = face_cascade.detectMultiScale(gray, 1.2, 5)

i=0
# Draw a rectangle around the faces
for (x, y, w, h) in faces_data:
    i=i+1
    filtre = cv2.imread(nom_filtre+".png")
    image_modif = cv2.imread(abs_path+"/resultat.png")
    filtre_fond = cv2.imread(nom_filtre+"_fond.png")
    frame= image_modif	

    height, width, channels = image_modif.shape
		#create masks
    fond_noir = Image.new('RGB',(width,height),(0,0,0))
    fond_noir.save(abs_path+"/fond_noir.png", "PNG")
    fond_transparent = Image.new('RGBA', (width,height), (0,0,0,0))
    fond_transparent.save(abs_path+"/fond_transparent.png", "PNG")

		# resize the images
    basewidth = w

    img_to_resize = Image.open(abs_path+"/"+nom_filtre+'.png')
    wpercent = (basewidth / float(img_to_resize.size[0]))
    hsize = int((float(img_to_resize.size[1]) * float(wpercent)))
    img_resized = img_to_resize.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img_resized.save(abs_path+'/resized_'+nom_filtre+'.png')

    img_to_resize = Image.open(abs_path+"/"+nom_filtre+'_fond.png')
    img_resized = img_to_resize.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img_resized.save(abs_path+'/resized_'+nom_filtre+'_fond.png')

	#adapted the mask to the images
    fond_noir = cv2.imread(abs_path+'/fond_noir.png',cv2.IMREAD_COLOR)
    filtre_fond = cv2.imread(abs_path+'/resized_'+nom_filtre+'_fond.png',cv2.IMREAD_COLOR)
    fond_transparent = cv2.imread(abs_path+'/fond_transparent.png', cv2.IMREAD_UNCHANGED)
    filtre = cv2.imread(abs_path+'/resized_'+nom_filtre+'.png',cv2.IMREAD_UNCHANGED)

    height1, width1, channels2 = filtre_fond.shape
  
    array_filtre_fond = filtre_fond[0:height1,0:width1]
		
    fond_noir[y:y+width1,x:x+height1]  = array_filtre_fond

    array_filtre = filtre[0:height1,0:width1]
    fond_transparent[y:y+width1,x:x+height1]  = array_filtre

    cv2.imwrite( "fond_noir.png", fond_noir)
    cv2.imwrite( "fond_transparent.png", fond_transparent)

    filtre_fond = cv2.imread("fond_noir.png")
    filtre = cv2.imread("fond_transparent.png")

		# Convert uint8 to float
    filtre = filtre.astype(float)
    image_modif = image_modif.astype(float)
		 
		# Normalize the filtre_fond mask to keep intensity between 0 and 1
    filtre_fond = filtre_fond.astype(float)/255
		 
		# Multiply the filtre with the filtre_fond matte
    filtre = cv2.multiply(filtre_fond, filtre)
		 
		# Multiply the image_modif with ( 1 - filtre_fond )
    image_modif = cv2.multiply(1.0 - filtre_fond, image_modif)
		 
		# Add the masked filtre and image_modif.
    outImage = cv2.add(filtre, image_modif)
		 

    cv2.imwrite(  abs_path+"/resultat.png", outImage)
