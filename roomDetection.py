import cv2
import numpy as np

def inverse_color(image):
    height,width = image.shape
    img2 = image.copy()

    for i in range(height):
        for j in range(width):
            img2[i,j] = (255-image[i,j])
    return img2

def roomDetection(image):
    img = image.copy()
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # height, width = thresh.shape
    # thresh2 = thresh.copy()
    # for i in range(height):
    #     for j in range(width):
    #         thresh2[i, j] = (255-thresh2[i, j])

    image2, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #print("contour2");
    res = thresh
    #for cnt in contours:
    rooms = []
    counter = 0
    for i in contours:
        rooms.append(i)
        counter += 1
        # if counter > 4:
        #     break
    mask = np.zeros(thresh.shape).astype(thresh.dtype)
    mask = inverse_color(mask)
    # cv2.imshow("rooms", mask)
    # cv2.waitKey(0)
    cv2.fillPoly(mask, rooms, (0, 255, 0))
    #res = cv2.bitwise_or(res, mask)
    #print(cnt)
    #cv2.imshow("rooms", mask)
    #cv2.imwrite("rooms.png", mask)
    #cv2.waitKey(0)
    return len(contours)