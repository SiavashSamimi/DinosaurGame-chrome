from PIL import ImageGrab
import cv2
import numpy as np
from pynput import keyboard

font = cv2.FONT_HERSHEY_SIMPLEX
kb = keyboard.Controller()

while True:
    #grab the screen
    screen = np.array(ImageGrab.grab(bbox=(0,0,1300,300))) 
    
    #resize the screen.Depending on the size of your screen, you need to change the following values....(screen[w,h])
    frame = screen[142:300,380:985]
    
    #convert color the frame to gray
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #make two bounding box.one for the background color and the other for the obstacles
    large_scale = np.sum(frame[90:133, 140:160] / 255.0)# for the obstacles
    tiny_scale = np.sum(frame[5:10,5:10] / 255.0) # for the background color
    
    #if the background color is white
    if tiny_scale == 25: 
    
        #if there is an obstacle within the bounding box
        if large_scale/860.0 < 1:
        
            #jump
            kb.press(keyboard.Key.up)
            
    #if the background color is black        
    else:
    
        #if there is an obstacle within the bounding box
        if large_scale > 0:
        
            #jump
            kb.press(keyboard.Key.up)


    cv2.imshow('Window', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break 
