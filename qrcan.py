# -*- credit: sky9262 -*-


import cv2
import sys
import os
from pyzbar import pyzbar

try:
    inpt = sys.argv[1]
except:
    print("Please provide me either a qr code image or directory path of many qr code images :-)")
    print("\nFor image: qrscan filename.jpg")
    print("For directory: qrcan ./path/to/directory/")
    sys.exit(1)

def loadImg(inpt):
    tmp = []
    images = []
    if os.path.isdir(inpt):
        for filename in os.listdir(inpt):
            img = os.path.join(inpt,filename)
            if img is not None:
                tmp.append(img)
    else:
         tmp.append(inpt)   
    for img in sorted(tmp,key=len):
        images.append(img)          
    return images
    
    
files = loadImg(inpt)

print("\nQR code data is:\n")

for _file in files:
    img = cv2.imread(_file)
    print(((pyzbar.decode(img))[0].data).decode())
print("\n")    

