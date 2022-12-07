import cv2 as cv
class Image(object):
    def __init__(self, URL):
        self.URL = URL
        self.img = cv.imread(self.URL)

    def show_image(self):
        # Output img with window name as 'image'
        cv.imshow('image', self.img)
        # Maintain output window utill
        # user presses a key
        cv.waitKey(0)
    def resize_image(self, h, w):

        self.img = cv.resize(self.img, (h,w), interpolation = cv.INTER_AREA)

image1 = Image('../Maquette/interface1.png')
image1.show_image()




 

        