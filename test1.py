# Import required packages 
import cv2 
import glob
import pytesseract 
from shutil import copy
from shutil import move
import os

# Mention the installed location of Tesseract-OCR in your system 
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

'''
for i_file in glob.glob("C:/Users/nxa18346/Documents/OCR/B/*.jpg"):
    # Read image from which text needs to be extracted 
    img = cv2.imread(i_file) 
    #print("Image:")
    #print(file)
    #print(img)
    # Preprocessing the image starts 

    # Convert the image to gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # Performing OTSU threshold 
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 

    # Specify structure shape and kernel size. 
    # Kernel size increases or decreases the area 
    # of the rectangle to be detected. 
    # A smaller value like (10, 10) will detect 
    # each word instead of a sentence. 
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 

    # Appplying dilation on the threshold image 
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 

    # Finding contours 
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                    cv2.CHAIN_APPROX_NONE) 

    # Creating a copy of image 
    im2 = img.copy() 

    # A text file is created and flushed 
    file = open("%s.txt" %i_file, "w+") 
    file.write("") 
    file.close() 

    # Looping through the identified contours 
    # Then rectangular part is cropped and passed on 
    # to pytesseract for extracting text from it 
    # Extracted text is then written into the text file 
    for cnt in contours: 
        x, y, w, h = cv2.boundingRect(cnt) 
        
        # Drawing a rectangle on copied image 
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        
        # Cropping the text block for giving input to OCR 
        cropped = im2[y:y + h, x:x + w] 
        
        # Open the file in append mode 
        file = open("%s.txt" %i_file, "a") 
        
        # Apply OCR on the cropped image 
        text = pytesseract.image_to_string(cropped) 
        
        # Appending the text into file 
        file.write(text) 
        file.write("\n") 
        
        # Close the file 
        file.close 

# Copy image to new folder if particular text matched
'''
text_to_search = ['1991','1992','1993','1994','1995','Rajkot']
if not os.path.exists('Sorted_B'):
    os.makedirs('Sorted_B')
for t_file in glob.glob("C:/Users/nxa18346/Documents/OCR/B/*.txt"):
    c_file = os.path.splitext(t_file)[0]
    #print(c_file)
    with open(t_file) as f:
        for t in text_to_search:
            if t in f.read() and os.path.exists(c_file):
                move(c_file, 'Sorted_B')


