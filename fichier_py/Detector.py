from Image import Image
import cv2
import imutils
class Detector:
    def __init__(self, image):
        self.image = image

    def detector(self):
        # Initializing the HOG person detector
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        # Resizing the Image
        self.image = imutils.resize(self.image, width=min(400, self.image.shape[1]))

        # Detecting all the regions in the
        # Image that has a pedestrians inside it
        (regions, _) = hog.detectMultiScale(self.image, winStride=(4, 4),padding=(4, 4),scale=1.05)

        # Drawing the regions in the Image
        for (x, y, w, h) in regions:
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    def show_image(self):
        cv2.imshow("Image", self.image)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

path = "C:/Users/sabir/Desktop/Projet-Vision/frames/frame8.jpg"
img = Image(path)
detect = Detector(img.get_image())
detect.detector()
detect.show_image()

