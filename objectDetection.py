import cv2

def doorDetection(image, scaleFactor = 1.121, minNeighbors = 1):
    doorCascade = cv2.CascadeClassifier("cascade_600_1500.xml")
    image2 = image.copy()
    #print(str(scaleFactor) + " " + str(image2.depth()))
    doors = doorCascade.detectMultiScale(image2, scaleFactor, minNeighbors)
    # print(doors)
    # print(len(doors))
    for(x, y, w, h) in doors:
        cv2.rectangle(image2, (x,y), (x+w, y+h), (0, 255, 0), 2)
    #cv2.imshow("doors", image2)
    #cv2.imwrite("doors.png", image2)
    #cv2.waitKey(0)
    return doors