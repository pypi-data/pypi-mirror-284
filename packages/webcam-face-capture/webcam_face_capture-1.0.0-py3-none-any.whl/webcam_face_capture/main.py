import cv2
import os

def webcam_face_capture(folder_name):
    """
    Captures grayscale face images from a webcam and saves them in the specified folder.

    Args:
    - folder_name (str): Name of the folder where images will be saved.

    Returns:
    - None

    This function initializes the webcam, detects faces using a pre-trained Haar Cascade classifier,
    and saves grayscale images of detected faces to the specified folder. It displays real-time
    feedback on the webcam feed, including the number of images saved and detection status.

    If no faces are detected, it displays a red rectangle and a 'No Face Detected' message.
    Detected faces are outlined with a blue rectangle on the webcam feed. Grayscale face images
    without any border markings are saved with names formatted as 'image_<number>.jpg' inside the
    specified folder.

    Press 'q' to quit the capture or when the maximum number of images (default: 500) is reached.

    Example usage:
    ```python
    folder_name = "captured_faces"
    webcam_face_capture(folder_name)
    ```
    """
    def create_folder_if_not_exists(folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

    def capture_and_save_faces(folder_name, max_images=500):
        # Create the folder if it doesn't exist
        create_folder_if_not_exists(folder_name)
        
        # Initialize webcam
        cap = cv2.VideoCapture(0)  # 0 is the default camera
        
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return
        
        # Load face detection model (pre-trained Haar Cascade)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        image_count = 0

        # Read and display an image from the webcam
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print("Error: Failed to capture image from webcam.")
                break
            
            # Convert frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
            
            if len(faces) > 0:
                # Draw green rectangle around the face if detected
                cv2.rectangle(frame, (10, 10), (100, 40), (0, 255, 0), -1)
                cv2.putText(frame, f"Images saved: {image_count}/{max_images}", (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
            else:
                # Draw red rectangle and text if no face detected
                cv2.rectangle(frame, (10, 10), (100, 40), (0, 0, 255), -1)
                cv2.putText(frame, "No Face Detected", (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
            
            # Process each detected face
            for (x, y, w, h) in faces:
                # Draw rectangle around the face on the original frame
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                # Crop the face region from the original frame
                face_region = frame[y:y+h, x:x+w]
                
                # Convert the cropped face region to grayscale
                gray_face = cv2.cvtColor(face_region, cv2.COLOR_BGR2GRAY)
                
                # Save the grayscale face image without any border markings
                if image_count < max_images:
                    image_count += 1
                    image_name = f"{folder_name}/image_{image_count}.jpg"
                    cv2.imwrite(image_name, gray_face)
                    # print(f"Saved: {image_name}")
            
            # Display the original frame with face detection and text
            cv2.imshow('Webcam', frame)
            
            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q') or image_count >= max_images:
                break
        
        # Release the webcam and close all windows
        cap.release()
        cv2.destroyAllWindows()
    capture_and_save_faces(folder_name)


