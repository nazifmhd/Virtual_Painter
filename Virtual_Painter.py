import cv2
import mediapipe as mp
import numpy as np
import math
import tkinter as tk
from tkinter import filedialog

# Function to calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to save the canvas
def save_canvas(canvas):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        cv2.imwrite(file_path, canvas)

# Function to load the canvas
def load_canvas():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        loaded_image = cv2.imread(file_path)
        return loaded_image
    return np.zeros((480, 640, 3), dtype="uint8")

# Initialize Mediapipe and canvas
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
canvas = np.zeros((480, 640, 3), dtype="uint8")

cap = cv2.VideoCapture(0)
prev_x, prev_y = 0, 0

# Default color and brush size
color = (255, 0, 0)  # Red
brush_size = 5

# Initialize Tkinter window
root = tk.Tk()
root.title("Virtual Painter")

# Add Save and Load buttons
save_button = tk.Button(root, text="Save Drawing", command=lambda: save_canvas(canvas))
save_button.pack()
load_button = tk.Button(root, text="Load Drawing", command=lambda: load_canvas())
load_button.pack()

# OpenCV loop with Tkinter integration
def start_painting():
    global canvas
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)
        
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                index_finger_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]  # Thumb tip
                h, w, _ = frame.shape
                cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
                thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
                
                # Calculate distance between thumb and index finger
                dist = distance(thumb_x, thumb_y, cx, cy)
                
                # Pinch gesture detected (threshold distance for pinch)
                if dist < 50:  # You can adjust this threshold based on your preference
                    color = (0, 255, 0)  # Change color to green
                    brush_size = 10  # Increase brush size
                else:
                    color = (255, 0, 0)  # Default color red
                    brush_size = 5  # Default brush size

                # If the previous points are not set yet, set them
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = cx, cy
                
                # Draw with selected color and brush size
                cv2.line(canvas, (prev_x, prev_y), (cx, cy), color, brush_size)
                prev_x, prev_y = cx, cy
                
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        else:
            prev_x, prev_y = 0, 0

        # Combine the canvas and the video frame
        combined = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
        cv2.imshow("Virtual Painter", combined)
        
        # Check for 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    root.quit()  # Quit Tkinter window when OpenCV window closes

# Start the painting thread
import threading
paint_thread = threading.Thread(target=start_painting)
paint_thread.start()

# Start Tkinter main loop
root.mainloop()
