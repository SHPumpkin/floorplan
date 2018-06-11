import cv2

def morphological(image, threshold = 10.682, openingSize = 5, closingSize = 50):
    image_copy = image.copy()
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (openingSize, openingSize))
    dilated = cv2.dilate(image_copy, element)
    #cv2.imshow("dilate", dilated)
    #cv2.waitKey(0)
    #cv2.threshold(image_copy, threshold)
    eroded = cv2.erode(dilated, element)

    element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (closingSize, closingSize))
    eroded = cv2.erode(eroded, element2)
    dilated = cv2.dilate(eroded, element2)

    #cv2.imwrite("afterMorphological.png", dilated)
    #cv2.waitKey(0)
    return dilated






