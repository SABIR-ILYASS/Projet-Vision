import cv2
class Image(object):
    def __init__(self, URL):
        self.URL = URL



    def read_image(self):
        # Read RGB image
        img = cv2.imread(self.URL)
        # Output img with window name as 'image'
        cv2.imshow('image', img)
        # Maintain output window utill
        # user presses a key
        cv2.waitKey(0) 

image1 = Image('C:/Users/SUPER ELectro/Desktop/Projet-Vision\Maquette/interface1.png')
image1.read_image()



 

        