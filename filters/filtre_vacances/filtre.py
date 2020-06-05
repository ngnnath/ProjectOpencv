import os, sys

import cv2
#import cv
import PIL
from PIL import Image

# Get absolute path of current dir
abs_path = os.path.abspath(os.path.dirname(__file__))

# Get image path from option
nom_img = sys.argv[1]

if os.path.isfile(nom_img) == False:
    sys.exit("Exit : file not found")

# Read the images
nom_filtre="vacances"
#nom_img=abs_path+"/retouche"

filtre = cv2.imread(nom_filtre+".png")
image_modif = cv2.imread(nom_img)
#image_modif = cv2.imread(nom_img+".png")
filtre_fond = cv2.imread(nom_filtre+"_fond.png")

 
height, width, channels = image_modif.shape
#create masks
fond_noir = Image.new('RGB',(width,height),(0,0,0))
fond_noir.save(abs_path+"/fond_noir.png", "PNG")

fond_transparent = Image.new('RGBA', (width,height), (0,0,0,0))
fond_transparent.save(abs_path+"/fond_transparent.png", "PNG")

# resize the images
# resize the images
basewidth = width/3

img_to_resize = Image.open(abs_path+'/'+nom_filtre+'.png')
wpercent = (basewidth / float(img_to_resize.size[0]))
hsize = int((float(img_to_resize.size[1]) * float(wpercent)))
img_resized = img_to_resize.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img_resized.save(abs_path+'/resized_'+nom_filtre+'.png')

img_to_resize = Image.open(abs_path+'/'+nom_filtre+'_fond.png')
img_resized = img_to_resize.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img_resized.save(abs_path+'/resized_'+nom_filtre+'_fond.png')

#adapted the mask to the images
fond_noir = cv2.imread(abs_path+'/fond_noir.png',cv2.IMREAD_COLOR)
filtre_fond = cv2.imread(abs_path+'/resized_'+nom_filtre+'_fond.png',cv2.IMREAD_COLOR)
fond_transparent = cv2.imread(abs_path+'/fond_transparent.png', cv2.IMREAD_UNCHANGED)
filtre = cv2.imread(abs_path+'/resized_'+nom_filtre+'.png',cv2.IMREAD_UNCHANGED)

height1, width1, channels2 = filtre_fond.shape
array_filtre_fond = filtre_fond[0:height1,0:width1]
x=height-height1
y=width-width1
fond_noir[x:x+height1,y:y+width1]  = array_filtre_fond

array_filtre = filtre[0:height1,0:width1]
fond_transparent[x:x+height1,y:y+width1]  = array_filtre

cv2.imwrite(abs_path+"/fond_noir.png", fond_noir)
cv2.imwrite(abs_path+"/fond_transparent.png", fond_transparent)

filtre_fond = cv2.imread(abs_path+"/fond_noir.png")
filtre = cv2.imread(abs_path+"/fond_transparent.png")

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
 
# Display image
cv2.imwrite(abs_path+"/resultat.png", outImage)

#print(os.path.join(abs_path,"resultat.png"))

 
