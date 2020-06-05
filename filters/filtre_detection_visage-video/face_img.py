import os
import sys
import click
import time
import cv2
import PIL
from PIL import Image

# Get absolute path of current file
abs_path = os.path.abspath(os.path.dirname(__file__))

DEFAULT_CASCADE_FOLDER = abs_path+'/'+'classifiers'
DEFAULT_FRONTAL_FACE_CLASSIFIER = abs_path+'/'+'classifiers'+'/'+'haarcascade_frontalface_default.xml'
DEFAULT_EYE_CLASSIFIER = abs_path+'/'+'classifiers'+'/'+'haarcascade_eyes.xml'

face_cascade=DEFAULT_FRONTAL_FACE_CLASSIFIER
eyes_cascade=DEFAULT_EYE_CLASSIFIER

# Define cascade classifiers
face_cascade = cv2.CascadeClassifier(face_cascade)
eye_cascade = cv2.CascadeClassifier(eyes_cascade)

video_capture = cv2.VideoCapture(0)

while (video_capture.isOpened()):

	# Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_data = face_cascade.detectMultiScale(gray, 1.2, 5)
    	
    nom_filtre="troll"
    nom_img="frame"
	
    filtre = cv2.imread(nom_filtre+".png")
    image_modif = frame
    filtre_fond = cv2.imread(nom_filtre+"_fond.png")	
	
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_data = face_cascade.detectMultiScale(gray, 1.2, 5)
	# Draw a rectangle around the faces
    for (x, y, w, h) in faces_data:

        filtre = cv2.imread(nom_filtre+".png")
        image_modif = frame
        filtre_fond = cv2.imread(nom_filtre+"_fond.png")
		#cv2.rectangle(img=frame,pt1=(x, y),pt2=(x + w, y + h),color=(255, 0, 0),thickness=2)
		#cv2.line(frame,(x,y),(x,y+h),(255,255,255),5)

			 
        height, width, channels = image_modif.shape

			#create masks
        fond_noir = Image.new('RGB',(width,height),(0,0,0))
        fond_noir.save(abs_path+"/fond_noir.png", "PNG")

        fond_transparent = Image.new('RGBA', (width,height), (0,0,0,0))
        fond_transparent.save(abs_path+"/fond_transparent.png", "PNG")
			# resize the images
        basewidth = w

        img_to_resize = Image.open(abs_path+'/'+nom_filtre+'.png')
        wpercent = (basewidth / float(img_to_resize.size[0]))
        hsize = int((float(img_to_resize.size[1]) * float(wpercent)))
        img_resized = img_to_resize.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img_resized.save(abs_path+'/'+'resized_'+nom_filtre+'.png')

        img_to_resize = Image.open(abs_path+'/'+nom_filtre+'_fond.png')
        img_resized = img_to_resize.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img_resized.save(abs_path+'/'+'resized_'+nom_filtre+'_fond.png')

			#adapted the mask to the images
        fond_noir = cv2.imread(abs_path+'/'+'fond_noir.png',cv2.IMREAD_COLOR)
        filtre_fond = cv2.imread(abs_path+'/'+'resized_'+nom_filtre+'_fond.png',cv2.IMREAD_COLOR)
        fond_transparent = cv2.imread(abs_path+'/'+'fond_transparent.png', cv2.IMREAD_UNCHANGED)
        filtre = cv2.imread(abs_path+'/'+'resized_'+nom_filtre+'.png',cv2.IMREAD_UNCHANGED)
        height1, width1, channels2 = filtre_fond.shape
        array_filtre_fond = filtre_fond[0:height1,0:width1]
			

        fond_noir[y:y+width1,x:x+height1]  = array_filtre_fond

        array_filtre = filtre[0:height1,0:width1]
        fond_transparent[y:y+width1,x:x+height1]  = array_filtre

        cv2.imwrite(abs_path+'/'+ "fond_noir.png", fond_noir)
        cv2.imwrite(abs_path+'/'+ "fond_transparent.png", fond_transparent)

        filtre_fond = cv2.imread(abs_path+'/'+"fond_noir.png")
        filtre = cv2.imread(abs_path+'/'+"fond_transparent.png")

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
			#cv2.imshow("outImg", outImage/255)
		
        frame = outImage/255

	# Display the resulting frame
	cv2.imshow('Face Detection using a webcam ', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
		
    time.sleep(1)
    image_modif = frame
	
video_capture.release()
cv2.destroyAllWindows()
