# Louay Khalil

import time
import cv2

if __name__ == '__main__':
    ############################################################################
    # Connect to video Source
    cam = cv2.VideoCapture("http://username:password@192.168.1.4/video/mjpg.cgi")
    cam.open("http://username:password@192.168.1.4/video/mjpg.cgi")

    # Print on console information about camera connection
    if cam.isOpened():
        print("Camera connection established.")
    else:
        print("Failed to connect to the camera .")
        exit(-1)

    ############################################################################
    while (True):
        # Get the video stream
        ret, frame = cam.read()
        # Show a frame with the image
        cv2.imshow('frame', frame)
        # Save image to file
        cv2.imwrite(filename='saved_img.jpg', img=frame)
        # Try to catch an exception and print the exception
        try:
            image = cv2.imread('saved_img.jpg', 1)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=3,
                minSize=(30, 30)
            )
            print("Found {0} Faces!".format(len(faces)))
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            status = cv2.imwrite('faces_detected.jpg', image)
            print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
        except Exception as e: print(e)
        # Delay of 50 seconds in the while-loop
        time.sleep(50)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # End of While-loop
    ############################################################################

############################################################################
# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()
############################################################################
############################################################################
############################################################################
# print( "X: ",x, "y: ",y, "w: ",w, "h: ", h)
# w = w*1.25
# h = w*1.25