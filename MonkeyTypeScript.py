from random import random
from threading import Timer
from time import sleep
from PIL import ImageGrab, ImageEnhance, ImageFilter, Image
import pytesseract, keyboard, os

def write_string(text):
    
    for x in text:
        keyboard.write(x)
        sleep(random() * 0.3)
    return     


while True:  
        if keyboard.is_pressed(keyboard.KEY_DOWN):
            img = ImageGrab.grabclipboard()
            img.save('temp.png')
            pytesseract.pytesseract.tesseract_cmd = r"C:\Users\X\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
            text = pytesseract.image_to_string(Image.open('temp.png'))
            os.remove('temp.png')
            write_string(text)
            print(text)
        if keyboard.is_pressed(keyboard.KEY_UP):
            break