import cv2
import numpy as np
from scipy.spatial.distance import cosine

# Initialize an empty array to store retinal scans
retina_scans = []

def preprocess_retina(image):
    # Placeholder preprocessing function
    # You should implement actual preprocessing steps here
    # Example: Convert image to grayscale and resize
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray, (100, 100))
    return resized_image

def store_retina(scan):
    # Preprocess the retinal scan
    preprocessed_scan = preprocess_retina(scan)
    print(preprocessed_scan)
    # Add the preprocessed scan to the array
    retina_scans.append(preprocessed_scan)

def normalize_vector(vector):
    # Normalize the vector to have unit length
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm

def match_retina(current_scan):
    # Preprocess the current retinal scan
    preprocessed_current_scan = preprocess_retina(current_scan)

    # Normalize the preprocessed current scan
    preprocessed_current_scan = normalize_vector(preprocessed_current_scan.flatten())

    # Compute similarity scores between the current scan and stored scans
    scores = []
    for stored_scan in retina_scans:
        # Preprocess and normalize the stored scan
        preprocessed_stored_scan = normalize_vector(stored_scan.flatten())

        # Compute cosine similarity between preprocessed scans
        similarity_score = cosine(preprocessed_current_scan, preprocessed_stored_scan)
        scores.append(similarity_score)

    # Determine the best match based on the lowest similarity score
    min_score = min(scores)
    print("Min Score:", min_score)  # Debugging purposes
    if min_score < 0.1:  # Adjust the threshold value as needed
        return True
    else:
        return False

def scan_retina_from_video(video_source=0):
    # Open the video capture device (0 for default webcam)
    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    scanning = False

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the frame
        cv2.imshow('Retina Scan', frame)

        key = cv2.waitKey(1) & 0xFF

        # Press 's' to start scanning
        if key == ord('s'):
            print("Scanning retina...")
            scanning = True

        # Press 'm' to match the current scan with stored scans
        elif key == ord('m'):
            if len(retina_scans) == 0:
                print("No stored retinal scans for matching.")
            else:
                matched = match_retina(frame)
                if matched:
                    print("Retina matched.")
                else:
                    print("Retina not matched.")

        # Press 'q' to exit the loop
        elif key == ord('q'):
            break

        # If scanning, store the frame and turn off the camera
        if scanning:
            store_retina(frame)
            # cap.release()
            # cv2.destroyAllWindows()
            print("Retina scan stored.")
            # break
            scanning = False

if __name__ == "__main__":
    # Specify the video source (0 for default webcam)
    scan_retina_from_video()
