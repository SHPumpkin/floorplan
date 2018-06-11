import cv2
import objectDetection
import morphologicalTransformation
import externalWallClosing
import internalWallClosing
import roomDetection
import random
from PIL import Image
import pytesseract

image = cv2.imread("real1.jpg")

result = {}
file = open("realTest1.txt", "w")
test2 = pytesseract.image_to_boxes(Image.open('real1.jpg'), lang='eng')
print(test2)
text=pytesseract.image_to_string(Image.open('real1.jpg'), lang='eng')
print(text)
for i in range(1, 100000):
    img = image.copy()
    print(i)
    rand1 = random.uniform(1, 100)
    rand2 = random.randint(1, 10)
    doors = objectDetection.doorDetection(img, scaleFactor=rand1, minNeighbors=rand2)

    rand3 = random.randint(1, 50)
    rand4 = random.randint(rand3, 100)
    res2 = morphologicalTransformation.morphological(img, openingSize=rand3, closingSize=rand4)


    res3 = externalWallClosing.convexWallClosing(res2)

    rand5 = random.randint(1,50)
    rand6 = random.randint(rand5, 100)
    res4 = internalWallClosing.internalWallClosing(res3, doors, openingSize=rand5, closingSize=rand6)

    res5 = roomDetection.roomDetection(res4)
    if res5 > 4:
        cv2.imshow("4rooms2", res4)
        cv2.imwrite("4rooms2"+str(i)+".jpg", res4)
        cv2.waitKey(0)
        #print(str(rand1) + " " + str(rand2) + " " + str(rand3) + " " + str(rand4) + " " + str(rand5) + " " + str(rand6))
    if (res5, len(doors)) in result.keys():
        result[(res5, len(doors))] += 1
    else:
        result[(res5, len(doors))] = 1
    print("Total Rooms:" + str(res5))
    print("Total Doors:" + str(len(doors)))
    file = open("resultfileTextRec21.txt", "w")
    file.write(str(i)+"\n")
    file.write(str(sorted(result.items(), key=lambda d: d[1])))
    file.close()
