# import the opencv library
import cv2
import time
import leer_ticket

# define a video capture object
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = cv2.QRCodeDetector()
while True:
    # Capture the video frame by frame
    ret, frame = vid.read()
    data, bbox, straight_qrcode = detector.detectAndDecode(frame)
    global previousData
    previousData = data
    if len(data) > 0:
        print(data)
        time.sleep(5)
        
        
    # Display the resulting frame
    cv2.imshow('frame', frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()