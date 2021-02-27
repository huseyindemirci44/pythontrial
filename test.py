import cv2
import numpy as np
import math 
from PIL import Image 
from PIL import ImageFilter

import random
import matplotlib.pyplot as plt

distance = 64 ; 
numberofimages = 10;


def dist(a,b):
    c = [];
    m,n = np.array(a).shape
    for i in range(0,m):
        t = math.sqrt((a[i][0]-b[0])*(a[i][0]-b[0]) + (a[i][1]-b[1])*(a[i][1]-b[1]));
        c.append(t);
    c = np.array(c) ;
    n = np.min(c);
    return n
    

Image1= Image.open('Image_972_background.jpg') ;
Image1 = Image1.convert('RGB')


imb1 = Image.open('blue1.jpg') ;
imb2 = Image.open('blue2.jpg') ;
imb3 = Image.open('blue3.jpg') ;
imb4 = Image.open('blue4.jpg') ;
imb5 = Image.open('blue5.jpg') ;
imb6 = Image.open('blue6.jpg') ;
imb7 = Image.open('blue7.jpg') ;
imb8 = Image.open('blue8.jpg') ;
imb9 = Image.open('blue9.jpg') ;
imb10 = Image.open('blue10.jpg') ;
imr1 = Image.open('red1.jpg') ;
imr2 = Image.open('red2.jpg') ;
imr3 = Image.open('red3.jpg') ;
imr4 = Image.open('red4.jpg') ;
imr5 = Image.open('red5.jpg') ;
imr6 = Image.open('red6.jpg') ;
imr7 = Image.open('red7.jpg') ;
imr8 = Image.open('red8.jpg') ;
imr9 = Image.open('red9.jpg') ;
imr10 = Image.open('red10.jpg') ;
img1 = Image.open('gr1.jpg') ;
img2 = Image.open('gr2.jpg') ;
img3 = Image.open('gr3.jpg') ;
img4 = Image.open('gr4.jpg') ;
img5 = Image.open('gr5.jpg') ;
img6 = Image.open('gr6.jpg') ;
img7 = Image.open('gr7.jpg') ;
img8 = Image.open('gr8.jpg') ;
img9 = Image.open('gr9.jpg') ;
img10 = Image.open('gr10.jpg') ;


x,y = Image1.size;


for j in range(0,numberofimages):
    print('Generating ', j, '-th image');

    allxy = []
    posx = random.randrange(20,x-20);
    posy = random.randrange(20,y-20);    
    allxy.append([posx,posy]);
            
    it = Image1.copy();

    for i in range(0,150):

        posx = random.randrange(20,x-20);
        posy = random.randrange(20,y-20); 
        b = [posx,posy];
 
        if dist(allxy,b)> distance:
            allxy.append([posx,posy]);
        
        m,n = np.array(allxy).shape
        
       
    for i in range(0,m):
        r1 = random.randrange(1,4);
        r2 = random.randrange(1,11);
#        print(r1,r2)
 
        if (r1 == 1 ) & (r2 == 1 ):      
            it.paste(imb1, (allxy[i][0], allxy[i][1])) 
        if (r1 == 1 ) & (r2 == 2 ):    
            it.paste(imb2, (allxy[i][0], allxy[i][1])) 
        if (r1 == 1 )& (r2 == 3) :    
            it.paste(imb3, (allxy[i][0], allxy[i][1])) 
        if (r1 == 1 )& (r2 == 4) :    
            it.paste(imb4, (allxy[i][0], allxy[i][1])) 
        if (r1 == 1 )& (r2 == 5 ):    
            it.paste(imb5, (allxy[i][0], allxy[i][1])) 
        if (r1 == 1 )& (r2 == 6 ):    
            it.paste(imb6, (allxy[i][0], allxy[i][1]))
        if (r1 == 1 )& (r2 == 7 ):    
            it.paste(imb7, (allxy[i][0], allxy[i][1])) 
        if (r1 == 1) & (r2 == 8) :    
            it.paste(imb8, (allxy[i][0], allxy[i][1])) 
        if (r1 == 1 )& (r2 == 9) :    
            it.paste(imb9, (allxy[i][0], allxy[i][1])) 
        if (r1 == 1 )& (r2 == 10 ):    
            it.paste(imb10, (allxy[i][0], allxy[i][1]))
        if (r1 == 1 ) & (r2 == 1 ):   
            it.paste(imr1, (allxy[i][0], allxy[i][1])) 
        if (r1 == 2 ) & (r2 == 2) :    
            it.paste(imr2, (allxy[i][0], allxy[i][1])) 
        if (r1 == 2 ) & (r2 == 3) :    
            it.paste(imr3, (allxy[i][0], allxy[i][1])) 
        if (r1 == 2 ) & (r2 == 4) :    
            it.paste(imr4, (allxy[i][0], allxy[i][1])) 
        if (r1 == 2) & (r2 == 5) :    
            it.paste(imr5, (allxy[i][0], allxy[i][1])) 
        if (r1 == 2) & (r2 == 6 ):    
            it.paste(imr6, (allxy[i][0], allxy[i][1]))
        if (r1 == 2) & (r2 == 7) :    
            it.paste(imr7, (allxy[i][0], allxy[i][1])) 
        if (r1 == 2) & (r2 == 8) :    
            it.paste(imr8, (allxy[i][0], allxy[i][1])) 
        if (r1 == 2) & (r2 == 9) :    
            it.paste(imr9, (allxy[i][0], allxy[i][1])) 
        if (r1 == 2) & (r2 == 10) :    
            it.paste(imr10, (allxy[i][0], allxy[i][1]))   
        if (r1 == 3) & (r2 == 1) :    
            it.paste(img1, (allxy[i][0], allxy[i][1])) 
        if (r1 == 3 )& (r2 == 2 ):    
            it.paste(img2, (allxy[i][0], allxy[i][1])) 
        if (r1 == 3) & (r2 == 3 ):    
            it.paste(img3, (allxy[i][0], allxy[i][1])) 
        if (r1 == 3) & (r2 == 4 ):    
            it.paste(img4, (allxy[i][0], allxy[i][1])) 
        if (r1 == 3) & (r2 == 5 ):    
            it.paste(img5, (allxy[i][0], allxy[i][1])) 
        if (r1 == 3 )& (r2 == 6 ):    
            it.paste(img6, (allxy[i][0], allxy[i][1]))
        if (r1 == 3 )& (r2 == 7 ):    
            it.paste(img7, (allxy[i][0], allxy[i][1])) 
        if (r1 == 3 )& (r2 == 8 ):    
            it.paste(img8, (allxy[i][0], allxy[i][1])) 
        if (r1 == 3 )& (r2 == 9 ):    
            it.paste(img9, (allxy[i][0], allxy[i][1])) 
        if (r1 == 3 )& (r2 == 10 ):    
            it.paste(img10, (allxy[i][0], allxy[i][1]))   
                
                
    it = it.filter(ImageFilter.BoxBlur(3))
                
    it.save("colortag"+str(j)+'.jpg', quality=95) 
                
                
    


#Image1.show()
     

