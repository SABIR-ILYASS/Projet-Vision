import time
import cv2 as cv

class Video(object):
    def __init__(self, URL, number):
        self.URL = URL
        self.fps = number

    def stop_video(self):
        if cv.waitKey(25) & 0xFF == ord(' '):
            return True
        return False

    def read_video(self):
        cap = cv.VideoCapture(self.URL)
        # Check if camera opened successfully
        if (cap.isOpened() == False):
            print("Error opening video stream or file")

        # start time
        start = time.time()

        # Read until video is completed
        count = 0
        wait = 0
        while (cap.isOpened()):

            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret:
                if wait % self.fps == 0:
                    cv.imwrite("C:/Users/sabir/Desktop/Projet-Vision/frames/frame%d.jpg" % count, frame)
                    count += 1

                # Display the resulting frame
                cv.imshow('Frame', frame)

                # Press Q on keyboard to  exit
                if self.stop_video():
                    break

            # Break the loop
            else:
                break
            wait += 1

        # When everything done, release the video capture object
        cap.release()

        # Closes all the frames
        cv.destroyAllWindows()



video1 = Video('C:/Users/sabir/Desktop/Projet-Vision/Data/video1.mp4', 100)
video1.read_video()

