import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image

image = Image.new('RGB',(100,100))

def brezenham_alg(start_x, start_y, end_x, end_y):
    if(start_x < end_x):
        x = start_x
        y = start_y
        last_x = end_x
        last_y = end_y
    else:
        x = end_x
        y = end_y
        last_x = start_x
        last_y = start_y

    if(x==last_x):
        y = min(start_y, end_y)
        last_y = max(start_y, end_y)

    dx = last_x - x
    dy = last_y - y

    if dx == 0:
        while y <= last_y:
            y+=1
        return

    tan = dy/dx

    incrN  = -2*dx
    incrNE = 2*(dy-dx)
    incrE  = 2*dy
    incrSE = 2*(dy+dx)
    incrS  = 2*dx

    d,low_incre, high_incre = 0,0,0
    """
    dy>1 : N - NE (y)
    0<dy<1 : NE - E (x)
    0>dy>-1 : E - SE (x)
    dy<-1 : SE - S (y)
    """

    if tan >1:
        high_incre = incrN
        low_incre  = incrNE
        d = dy-2*dx

    elif tan >0:
        high_incre = incrNE
        low_incre  = incrE
        d = 2*dy-dx

    elif tan >-1:
        high_incre = incrE
        low_incre  = incrSE
        d = 2*dy+dx

    else:
        high_incre = incrSE
        low_incre  = incrS
        d = dy+2*dx

    while x != last_x or (y != last_y if (tan>1 or tan<-1) else False):
        if d<= 0 :
            d+= low_incre
            if(tan>1):
                x+= 1
                y+= 1
                image.putpixel((x,y),(0,0,255)) #синий
            elif(tan<-1):
                y-=1
                image.putpixel((x,y),(255,160,122)) #светло оранжевый
            else:
                y+= 0 if tan>0 else -1
                x+= 1
                image.putpixel((x,y),(255, 165, 0)) #оранжевый
        else :
            d+= high_incre
            if(tan>1):
                y+=1
                image.putpixel((x,y),(128, 0, 128)) #фиолетовый
            elif(tan<-1):
                y-=1
                x+=1
                image.putpixel((x,y),(255,255,255)) #белый
    plt.imshow(image)
#фиолетово-синий
brezenham_alg(5,-50,30,40)
