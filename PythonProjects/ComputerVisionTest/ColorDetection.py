import cv2
import numpy as np

def empty(a):
    pass

def main():

    #Formatted as 
    upper = (85, 145, 210)
    lower = (65, 125, 185)
    
    print(cv2.__version__)
    cap = cv2.VideoCapture(1)

    cv2.namedWindow("HSV")
    cv2.resizeWindow("HSV", 600, 400)

    cv2.createTrackbar("HUE MIN", "HSV", 0, 179, empty)
    cv2.createTrackbar("HUE MAX", "HSV", 179, 179, empty)
    cv2.createTrackbar("SAT MIN", "HSV", 0, 255, empty)
    cv2.createTrackbar("SAT MAX", "HSV", 255, 255, empty)
    cv2.createTrackbar("VALUE MIN", "HSV", 0, 255, empty)
    cv2.createTrackbar("VALUE MAX", "HSV", 255, 255, empty)

    while True:
        ret, frame = cap.read()

        hMin = cv2.getTrackbarPos("HUE MIN", "HSV")
        hMax = cv2.getTrackbarPos("HUE MAX", "HSV")
        sMin = cv2.getTrackbarPos("SAT MIN", "HSV")
        sMax = cv2.getTrackbarPos("SAT MAX", "HSV")
        vMin = cv2.getTrackbarPos("VALUE MIN", "HSV")
        vMax = cv2.getTrackbarPos("VALUE MAX", "HSV")

        frame = cv2.resize(frame, (800,500))
        blurred = cv2.GaussianBlur(frame,(11,11),0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        lower = (hMin, sMin, vMin)
        upper = (hMax, sMax, vMax)
        mask = cv2.inRange(hsv, lower, upper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask,None, iterations =2)
        
        #allows for showing the mask in color
        result = cv2.bitwise_and(frame, frame, mask=mask)


        #Quit if q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        #show the hsv view of the camera
        #cv2.imshow("csv", hsv)

        #show the masked view of the camera
        cv2.imshow("mask", mask)

        #show the masked result with color
        cv2.imshow("Result", result)

    cap.release()
    cv2.destroyAllWindows()
    return 0

if __name__ == "__main__":
    main()
