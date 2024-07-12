
# Webcam Face Capture

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 


This Python script captures faces from a webcam, converts them to grayscale, and saves them to a specified folder.

### Explanation:

- **Installation**: 
```python
pip install webcam_face_capture

```

# Usage
```python
import webcam_face_capture as wb
wb.webcam_face_capture('folder_apth')
```

#### Additional Details
- Dependencies: Ensure you have opencv-python installed, as it's a requirement for this package.

- Customization: Modify the face detection parameters (scaleFactor, minNeighbors, minSize) inside the webcam_face_capture function in webcam_face_capture.py based on your webcam setup and environment for optimal detection.

- Feedback: Real-time feedback on the webcam feed includes the number of images saved and face detection status. Press 'q' to quit the capture.

