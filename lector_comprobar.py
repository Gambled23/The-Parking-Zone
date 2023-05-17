# import the opencv library
import cv2
import time
from leer_ticket import desocuparCajon
from tkinter import messagebox

id_cámaras = ['B1','B2','B3','B4']

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
        if data == id_cámaras[0]:
            messagebox.showinfo('Cajon correcto', f'El ticket presentado es para el cajon {data}')
        else:
            messagebox.showerror('Cajon incorrecto', f'El ticket presentado es para el cajon {data} pero se presentó en {id_cámaras[0]}')
            print(f'')
        time.sleep(3)
        
        
    # Display the resulting frame
    cv2.imshow(f'The Parking Zone - Cajon {id_cámaras[0]}', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()