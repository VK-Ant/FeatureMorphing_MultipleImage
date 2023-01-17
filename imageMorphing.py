import cv2

image1 = cv2.imread('3.jpg')
image1 = cv2.resize(image1,(225,225))
cv2.imwrite("Image1.png",image1)
image2 = cv2.imread('1.jpg')
image2 = cv2.resize(image2,(225,225))
cv2.imwrite("Image2.png",image1)
image3 = cv2.imread('5.jpg')
image3 = cv2.resize(image3,(225,225))
cv2.imwrite("Image3.png",image3)


#imgAdd = cv2.addWeighted(image1,0.7,image2,0.3,0)
#cv2.imwrite("Morphed1.png", imgAdd)

slides = [["Image1.png","Image2.png"],
        ["Image1.png","Image3.png"]]

for src, dst in slides:
    imagesrc = cv2.imread(src)
    imagesrc = cv2.resize(imagesrc,(255,255))
    imagedst = cv2.imread(dst)
    imagedst = cv2.resize(imagedst,(255,255))

    for i in range(100):
        percentage = float(i/100)
        print(percentage)
        imgAdd = cv2.addweighted(imagesrc,1- percentage, imagedst,percentage,0)
        cv2.imshow("Morphed",imgAdd);
        cv2.waitKey(100)


cv2.waitKey(0)
cv2.destroyAllWindows()