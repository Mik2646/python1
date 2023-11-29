import cv2 as cv
import numpy as np

class findpic:
    def __init__(self, main_img, temp_img):
        self.mainimg = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.tempimg = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        
    def find(self, debug=False, accuracy=0.9, _text="odject" ):
        result = cv.matchTemplate(self.mainimg,self.tempimg,cv.TM_CCOEFF_NORMED)
        min,max,minloc,maxloc = cv.minMaxLoc(result)
        
        acc = accuracy
            
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
            point = []
            
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
                    centerX =int(w/2)+ x
                    centerY = int(h/2)+ y
                    point.append((centerX,centerY))
                    # print(x)
                    # print(x)
                    font = cv.FONT_HERSHEY_SIMPLEX
                    position = (topleft[0]+0, topleft[1])
                    fontsize = 0.5
                    color = (200, 200, 0)
                    
                    if debug :
                        
                        cv.drawMarker(self.mainimg,(centerX,centerY),color=(255,0,235),thickness=2, markerSize=25,markerType=cv.MARKER_CROSS)
                        cv.rectangle(self.mainimg,topleft,bottomright,color=(255,0,255),thickness=2, lineType=cv.LINE_8)
                        cv.putText(self.mainimg, _text, position, font, fontsize, color, thickness=2)
            else:
                print(" ไม่เจอรูปภาพ ") 
                
            if debug:  
                print(f'เจอรูปภาพทั้งหมด = {len(rex)} รูป')  
                # print(point)                   
                cv.imshow('result',self.mainimg)
                cv.waitKey(0)
                cv.destroyAllWindows()
            return point
        
# find = findpic('image/game2.jpg','image/coin.jpg')
# find.find(debug=True, _text="coin")


