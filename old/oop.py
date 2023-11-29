import cv2 as cv
import numpy as np

class Picture:
    def __init__(self,main_img,temp_img):
        self.main_img = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        
    def findpic(self):
        result = cv.matchTemplate(self.main_img,self.temp_img,cv.TM_CCOEFF_NORMED)
        min,max,minloc,maxloc = cv.minMaxLoc(result)
        print(max)
        print(maxloc)
        
        acc = 0.9
        
        if max >= acc:
            topleft = maxloc
            print(self.temp_img.shape)
            
            height = self.temp_img.shape[0]
            width = self.temp_img.shape[1]
            
            buttomright = (topleft[0]+width,topleft[1]+height)
            cv.rectangle(self.main_img,topleft,buttomright,color=(97,189,92),thickness=4,lineType= cv.LINE_4)
            
            font = cv.FONT_HERSHEY_SIMPLEX
            
            text = "GOJO"
            text_size = cv.getTextSize(text, font, 0.5, 4)[0]
            text_width, text_height = text_size

            text_x = (topleft[0] + buttomright[0] - text_width) // 2
            text_y = buttomright[1] + text_height + 10

            position = (text_x, text_y)
            fontsize = 0.7
            color = (200, 200, 0)
            cv.putText(self.main_img, text, position, font, fontsize, color, thickness=2)
            # font = cv.FONT_HERSHEY_SIMPLEX
            
            # position = (topleft[0],topleft[1])
            # fontsize = 0.5
            # color = (255,0,255)
            # cv.putText(self.main_img,"TEST_TEXT",position,font,fontsize,color,thickness=4)
            
            cv.imshow('result',self.main_img)
            cv.waitKey(0)
            cv.destroyAllWindows()