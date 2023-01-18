import cv2
import numpy as np

def empty(a):
    pass

def main():
    
    cap = cv2.VideoCapture(1)
    
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
 
    while True:
        ret, frame = cap.read()


        #Sizing the image
        frame = cv2.resize(frame, (800,500))

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # try to detect faces in the webcam
        faces = faceCascade.detectMultiScale(rgb, scaleFactor=1.3, minNeighbors=5)

        # for each faces found
        for (x, y, w, h) in faces:
        # Draw a rectangle around the face
            color = (0, 255, 255) # in BGR
            stroke = 5
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, stroke)
            cv2.putText(frame, "Face Detected", (x+w+20, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
        
        #Quit if q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        #show the view of the camera
        cv2.imshow("frame", frame)

    cap.release()
    cv2.destroyAllWindows()
    return 0

if __name__ == "__main__":
    main()
