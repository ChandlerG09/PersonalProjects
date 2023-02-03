import cv2

# Initialize webcam
cap = cv2.VideoCapture(1)

# Read the first frame
ret, frame = cap.read()

# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Store the previous frame
prev_frame = gray

while True:
    # Read the next frame
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate the difference between the previous frame and the current frame
    diff = cv2.absdiff(prev_frame, gray)
    
    # Threshold the difference to create a binary mask
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    
    # Dilate the binary mask to fill in any holes
    dilated = cv2.dilate(thresh, None, iterations=3)
    
    # Find contours in the binary mask
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on the frame
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow("Motion Detection", frame)
    
    # Update the previous frame
    prev_frame = gray
    
    # Break the loop if the user presses the "q" key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
