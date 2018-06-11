import cv2
def internalWallClosing(image, doors, openingSize = 15, closingSize = 50):
    image2 = image.copy()
    for (x, y, w, h) in doors:
        element = cv2.getStructuringElement(cv2.MORPH_RECT, (openingSize, openingSize))
        dilated = cv2.dilate(image2, element)
        eroded = cv2.erode(dilated, element)

        element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (closingSize, closingSize))
        eroded = cv2.erode(eroded, element2)
        image2 = cv2.dilate(eroded, element2)

        #cv2.imshow("closing doors...", image2)
        #cv2.waitKey(0)
        #cv2.rectangle(image2, (x - 10, y - 10), (x + w, y + h), (0, 0, 0), -1)

    #cv2.imshow("closing internal wall", image2)
    #cv2.imwrite("internalClosing.png", image2)
    #cv2.waitKey(0)
    return image2
