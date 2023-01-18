import cv2
import numpy as np

def empty(a):
    pass

def main():
    
    cap = cv2.VideoCapture(1)

    cv2.namedWindow("HSV")
    cv2.resizeWindow("HSV", 600, 400)

    cv2.createTrackbar("Threshold1", "HSV", 100, 255, empty)
    cv2.createTrackbar("Threshold2", "HSV", 0, 255, empty)

    while True:
        ret, frame = cap.read()
        imgctr = frame.copy()

        #Sizing the image
        frame = cv2.resize(frame, (800,500))
        imgctr = cv2.resize(imgctr, (800,500))

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #Blurring the image for easier tracking
        blurred = cv2.GaussianBlur(frame,(11,11),0)

        #converting the image to grayscale so we can find contours
        grayscale = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

        #Thresholds for getting contours
        threshold1 = cv2.getTrackbarPos("Threshold1", "HSV")
        threshold2 = cv2.getTrackbarPos("Threshold2", "HSV")

        #Brigten and make image more prevalent
        canny = cv2.Canny(grayscale, threshold1, threshold2)
        kernel = np.ones((5,5))
        imgDil = cv2.dilate(canny, kernel, iterations=1)

        #Finding the contours
        contours, hier = cv2.findContours(imgDil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        #Go through each contour and only deal with ones with a large area to remove noise
        for cnt in contours: 
            area = cv2.contourArea(cnt)
            if area > 5000:
                #Drawing the contour
                cv2.drawContours(imgctr, cnt, -1, (255,0,0), 3)
                
                #Get the permiter
                peri = cv2.arcLength(cnt, True)
                
                #Estimate the position of the corners
                corners = cv2.approxPolyDP(cnt, 0.02*peri, True)
                
                #Create a rectange around the contour
                x, y, w, h = cv2.boundingRect(corners)

                #Adding the rectangle to the screen
                cv2.rectangle(imgctr, (x, y), (x+w, y+h), (0,0,255), 5)

                #Adding text to the rectangle
                cv2.putText(imgctr, "Points: " + str(len(corners)),
                (x+w+20, y+h+20), cv2.FONT_HERSHEY_COMPLEX, .7, (0,255,0), 2)
        
        #Quit if q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        #show the view of the camera
        cv2.imshow("frame", frame)
        cv2.imshow("Gray", imgctr)

    cap.release()
    cv2.destroyAllWindows()
    return 0

if __name__ == "__main__":
    main()
