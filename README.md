# Virtual_Painter

Virtual Painter is an interactive Python application that allows users to draw on a virtual canvas using hand gestures. The application uses OpenCV, MediaPipe, and Tkinter to detect hand gestures and create drawings in real-time. The project integrates a virtual painting experience with a simple graphical user interface (GUI) for saving and loading drawings.

## Features

- **Hand Gesture Detection**: Detects hand movements and gestures to draw on a virtual canvas.
- **Dynamic Brush Control**: Adjusts brush color and size based on gestures.
- **Save and Load Drawings**: Save your artwork as a PNG file and reload it for editing.
- **Real-Time Interaction**: Combines video feed with a canvas to provide a seamless drawing experience.

## How It Works

1. The application captures video feed using OpenCV and detects hand landmarks using MediaPipe Hands.
2. The distance between the thumb tip and index finger tip is calculated to detect a pinch gesture.
3. When the pinch gesture is detected, the brush color and size change dynamically.
4. The user can draw on the canvas by moving their hand, and the drawing is updated in real-time.
5. The GUI provides buttons to save the current drawing or load a previously saved canvas.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy
- Tkinter (included with Python on most platforms)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nazifmhd/Virtual_Painter.git
   cd Virtual_Painter
   ```
2. Install the required Python packages:
   ```bash
   pip install opencv-python mediapipe numpy
   ```

## Usage

1. Run the application:
   ```bash
   python Virtual_Painter.py
   ```
2. A video feed will open, and the GUI will display buttons for saving and loading drawings.
3. Use your index finger to draw on the canvas.
4. Pinch your thumb and index finger together to change the brush color and size dynamically.
5. Click **Save Drawing** to save your artwork as a PNG file.
6. Click **Load Drawing** to load a previously saved PNG file.

## Key Bindings

- **q**: Exit the application.

## File Structure

- `Virtual_Painter.py`: Main Python script containing the application logic.
- `README.md`: Documentation file for the project.

## Example Gestures

- **Default Drawing**: Use your index finger to draw. The default color is red, and the brush size is 5.
- **Dynamic Brush**: Pinch your thumb and index finger (distance < 50) to change the brush color to green and increase the brush size to 10.

## Screenshots

![Virtual Painter Interface](path/to/screenshot.png)  
*A screenshot of the application showing real-time drawing.*

## Troubleshooting

- Ensure your webcam is properly connected and accessible.
- If the application does not detect hand gestures, ensure there is sufficient lighting and the hand is visible in the frame.
- If `cv2.imshow` displays a blank window, check your OpenCV installation.

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [MediaPipe](https://google.github.io/mediapipe/) for hand tracking.
- [OpenCV](https://opencv.org/) for video processing.

---

Enjoy creating art with your hands using Virtual Painter! If you encounter any issues or have suggestions, feel free to open an issue or contact me.
