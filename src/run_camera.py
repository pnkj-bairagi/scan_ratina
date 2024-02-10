import cv2

def run_camera():
    # Open the default camera (usually camera index 0)
    cap = cv2.VideoCapture(0)
    print(cap)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Read and display video frames
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the frame
        print(frame)
        cv2.imshow('Camera', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_camera()
