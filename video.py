import cv2 as cv

class Video(object):
    def __init__(self, URL):
        self.URL = URL
        # self.number_of_frame_per_second = number

    def stop_video(self):
        if cv.waitKey(25) & 0xFF == ord(' '):
            return True
        return False

    def read_video(self):
        cap = cv.VideoCapture(self.URL)
        # Check if camera opened successfully
        if (cap.isOpened() == False):
            print("Error opening video stream or file")

        # Read until video is completed
        while (cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:

                # Display the resulting frame
                cv.imshow('Frame', frame)

                # Press Q on keyboard to  exit
                if self.stop_video():
                    break

            # Break the loop
            else:
                break

        # When everything done, release the video capture object
        cap.release()

        # Closes all the frames
        cv.destroyAllWindows()


video1 = Video('C:/Users/sabir/Desktop/Projet-Vision/video1.mp4')
video1.read_video()

