import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# Try different camera indices if needed
cap = cv2.VideoCapture(0)  # Try default camera first
# If unsuccessful, try listing available cameras using OS-specific tools and replace the index here (e.g., cap = cv2.VideoCapture(1)) 

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame")
            break

        # Instructions displayed on the frame before capturing
        cv2.putText(frame, 'Ready? Press "Q" to start capturing', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        # Wait for 'q' key press to start capturing
        if cv2.waitKey(1) & 0xFF == ord('q'):
            while counter < dataset_size:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Unable to capture frame")
                    break

                cv2.imshow('frame', frame)
                cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
                counter += 1

                # Exit inner loop on 'q' press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

cap.release()
cv2.destroyAllWindows()