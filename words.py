import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time
def srch(text,key) :
	if len(text)<len(key) :
		return False
	if text.find(key) != -1 :
		return True
	else :
		return False
def find_word_in_image() :
	print('Enter the image path : ')
	img=input()
	print('Enter the word to search : ')
	key=input()
	pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
	img = cv2.imread(img)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	print('Checking...')
	pytesseract.image_to_pdf_or_hocr(img,extension='pdf')
	boxes = pytesseract.image_to_data(img)
	f=0
	for a,b in enumerate(boxes.splitlines()):
			 if a!=0:
				 b = b.split()
				 if len(b)==12 and srch(b[11].lower(),key.lower()):
					 x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
					 cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
					 cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)
					 f=1
	if f==0 :
		print('Word not found')
	else : 
		print('Word found !')
	size=(1000,800)
	cv2.imshow('img', cv2.resize(img,size))
	cv2.waitKey(0)
def get_text_in_image() :
	print(pytesseract.image_to_string(img))
while(True) :
	print("1. Find a word in an image")
	print("2. Get all the text in an image")
	print("3. Exit")
	print("Select a number : ",end='')
	n=int(input())
	if n==1 :
		find_word_in_image()
	elif n==2 :
		get_text_in_image()
	elif n==3 :
		exit(0)
