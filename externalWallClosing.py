import cv2
import morphologicalTransformation
def convexWallClosing(image):
    img = image.copy()
    ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
    # height, width = thresh.shape
    # thresh2 = thresh.copy()
    # for i in range(height):
    #     for j in range(width):
    #         thresh2[i, j] = (255-thresh2[i, j])

    image2, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print("contour");
    # print(len(contours))
    for cnt in contours:
        hull = cv2.convexHull(cnt)
        cv2.drawContours(thresh, [cnt], -1, (0, 255, 0), 20)
        cv2.drawContours(thresh, [hull], -1, (0, 0, 255), 20)
    #cv2.imshow("hull1", thresh)
    #cv2.imwrite("convexhull.png", thresh)
    #cv2.waitKey(0)
    # res = morphologicalTransformation.morphological(thresh, openingSize = 5, closingSize = 5)
    # cv2.imshow("hull2", res)
    # cv2.imwrite("convexhullMorphl1.png", res)
    # cv2.waitKey(0)
    return thresh