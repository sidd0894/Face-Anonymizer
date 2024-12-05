# Face Anonymizer with OpenCV and MediaPipe

This project demonstrates how to detect faces in real-time from a webcam feed and blur them using OpenCV and MediaPipe. It leverages the MediaPipe Face Detection model to identify faces in a frame, and then applies a blur effect to those areas. Optionally, it can also draw bounding boxes around detected faces.


## Requirements

To run the project, you'll need to install the following Python libraries:

- `mediapipe`: For face detection.
- `opencv-python`: For image processing and webcam access.

You can install the dependencies using pip:

```bash
pip install mediapipe opencv-python
```

Alternatively, you can install all required dependencies from the `requirements.txt` file by running:

```bash
pip install -r requirements.txt
```

## Functions

### `blur_faces(frame, ksize: int, draw_bbox: bool=False)`

This function detects faces in a given frame and applies a blur effect on the face regions.

**Parameters:**
- `frame` (numpy.ndarray): The image frame from the webcam or video source.
- `ksize` (int): The size of the kernel used for the blur effect.
- `draw_bbox` (bool, optional): If set to `True`, it will draw a bounding box around the detected face. Defaults to `False`.

**Returns:**
- A frame with blurred faces (and optionally bounding boxes).

### `main()`

This function captures video from the default webcam, detects faces, applies the blur effect, and displays the resulting video with blurred faces in real-time. The video stream continues until the user presses the 'q' key to quit.

## How It Works

1. **Face Detection**: MediaPipe's `FaceDetection` model is used to detect faces in each frame from the webcam.
2. **Blurring Faces**: Once a face is detected, a bounding box is computed based on the relative coordinates. The region inside the bounding box is then blurred using OpenCV's `cv2.blur()` function.
3. **Display**: The modified frame is displayed with the blurred faces, and optionally, bounding boxes can be drawn around the faces.

## Usage

To run the program, simply execute the script. It will open the webcam feed and apply the face blurring effect in real-time.

```bash
python face_anonymizer.py
```

Press 'q' to close the webcam feed and exit the program.