# -*- credit: sky9262 -*-


import cv2
import sys
import os

try:
    inpt = sys.argv[1]
except:
    print("Please provide me either a qr code image or directory path of many qr code images :-)")
    print("\nFor image: qrscan filename.jpg")
    print("For directory: qrcan ./path/to/directory/")
    sys.exit(1)

def loadImg(inpt):
    images = []
    if os.path.isdir(inpt):
        for filename in os.listdir(inpt):
            img = os.path.join(inpt,filename)
            if img is not None:
                images.append(img)
    else:
         images.append(inpt)        
    return images
    
    
files = loadImg(inpt)

print("\nQR code data is:\n")

for _file in files:
    img = cv2.imread(_file)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    if bbox is not None:
        print(data,end="")
print("\n")    

