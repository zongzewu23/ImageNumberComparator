import math
import sys
import keyboard
from PIL import ImageGrab
import pyautogui
import cv2
import pytesseract
import time  

pytesseract.pytesseract.tesseract_cmd = r'F:\xycalc\TESS-OCR\tesseract.exe'

while True:
    if keyboard.is_pressed('space'):
        print('done')
        sys.exit()

    
    result = ["", ""]

    
    ImageGrab.grab(bbox=(100, 300, 230, 450)).save('num1.png') 
    ImageGrab.grab(bbox=(280, 300, 400, 450)).save('num2.png') 

    
    img1 = cv2.imread('num1.png')
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    _, thresh1 = cv2.threshold(img1, 150, 255, cv2.THRESH_BINARY)
    num1_str = pytesseract.image_to_string(thresh1, config='--psm 7').strip()

    
    img2 = cv2.imread('num2.png')
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    _, thresh2 = cv2.threshold(img2, 150, 255, cv2.THRESH_BINARY)
    num2_str = pytesseract.image_to_string(thresh2, config='--psm 7').strip()

    
    result = [num1_str, num2_str]
    print(f"print result: {result}")

    try:
        
        result[0] = result[0].replace('O', '0').replace('{', '1').replace('A', '4').strip()
        result[1] = result[1].replace('O', '0').replace('{', '1').replace('A', '4').strip()

        
        
        num1 = math.floor(float(result[0]))
        num2 = math.floor(float(result[1]))

        
        pyautogui.moveTo(277, 700, duration=0.05)

        if num1 > num2:
            pyautogui.mouseDown()
            pyautogui.move(50, 50, duration=0.2)
            pyautogui.move(-50, 50, duration=0.05)
            pyautogui.mouseUp()
            print(f'{num1}  >  {num2}')
        elif num1 == num2:
            pyautogui.mouseDown()
            pyautogui.move(100, 0, duration=0.2)
            pyautogui.mouseUp()
            print(f'{num1}  =  {num2}')
        else:
            pyautogui.mouseDown()
            pyautogui.move(-50, 50, duration=0.2)
            pyautogui.move(50, 50, duration=0.05)
            pyautogui.mouseUp()
            print(f'{num1}  <  {num2}')
        
        #set delay to ensure the last compare result won't affect next compare
        time.sleep(0.25)
    
    except IndexError as e:
        print('Too much string, man')
    except ValueError as e:
        print('Not even an integer, bro')
