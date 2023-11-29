import cv2 as cv
import numpy as np

class findpic:
    def __init__(self, main_img, temp_img):
        self.mainimg = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.tempimg = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        
    def find(self):
        result = cv.matchTemplate(self.mainimg,self.tempimg,cv.TM_CCOEFF_NORMED)
        min,max,minloc,maxloc = cv.minMaxLoc(result)
        
        acc = 0.7
        
        location = np.where(result >= acc)
        location = list(zip(*location[::-1]))
        # print(type(location))
        # print(location)
        if location:
            height = self.tempimg.shape[0]
            width = self.tempimg.shape[1]
            # print(height)
            # print(width)
            rectangle = []
            
            for l in location:
                rect = [int(l[0]),int(l[1]),width,height]
                rectangle.append(rect)
                rectangle.append(rect)
            print(rectangle)

            rex,weights = cv.groupRectangles(rectangle,groupThreshold=1,eps=0.5)
            exit
            
            if len(rex):
                for (x,y,w,h) in rex :
                    print(x,y,w,h)
                    topleft = (x,y)
                    bottomright = (x+w,y+h)
                    cv.rectangle(self.mainimg,topleft,bottomright,color=(255,0,255),thickness=2, lineType=cv.LINE_AA)
                    
                
                
                
                                
            cv.imshow('result',self.mainimg)
            cv.waitKey(0)
            cv.destroyAllWindows()
            exit
        
find = findpic('image/game2.jpg','image/coin.jpg')
find.find()


