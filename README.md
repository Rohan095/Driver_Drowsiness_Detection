# Drowsiness Detection System

A real-time computer vision system that monitors driver alertness by analyzing facial landmarks and eye movements to detect drowsiness and prevent accidents.

## 🚗 Overview

This system uses advanced computer vision techniques to monitor a person's eyes through a webcam feed. When prolonged eye closure is detected (indicating drowsiness), the system triggers audio and visual alerts to wake up the user. This is particularly useful for drivers, security personnel, or anyone who needs to stay alert during extended periods of focus.

## ✨ Features

- **Real-time eye tracking** using facial landmark detection
- **Eye Aspect Ratio (EAR) calculation** for precise drowsiness detection
- **Audio alerts** with customizable sound files
- **Visual warnings** displayed on screen
- **Adjustable sensitivity** through threshold parameters
- **Cross-platform compatibility** (Windows, macOS, Linux)

## 🛠️ Technologies Used

- **OpenCV** - Computer vision and image processing
- **dlib** - Facial landmark detection
- **scipy** - Mathematical computations for distance calculations
- **pygame** - Audio alert system
- **imutils** - Image processing utilities

## 📋 Prerequisites

Before running the system, ensure you have:

- Python 3.6 or higher
- A working webcam
- Required Python packages (see Installation section)
- dlib facial landmark predictor file

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/drowsiness-detection.git
   cd drowsiness-detection
   ```

2. **Install required packages:**
   ```bash
   pip install opencv-python dlib scipy imutils pygame
   ```

3. **Download the facial landmark predictor:**
   - Download `shape_predictor_68_face_landmarks.dat` from [dlib's model repository](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
   - Extract and rename it to `face_landmarks.dat`
   - Place it in the project directory

4. **Add alert sound:**
   - Place your alert sound file (WAV format) in the project directory
   - Name it `Alert.wav` or update the filename in the code

## 🚀 Usage

1. **Run the system:**
   ```bash
   python drowsiness_detection.py
   ```

2. **Position yourself in front of the camera:**
   - Ensure good lighting
   - Keep your face clearly visible
   - Maintain a reasonable distance from the camera

3. **System operation:**
   - Green contours will appear around your eyes when detected
   - If drowsiness is detected, red warning text will appear
   - An audio alert will play to wake you up
   - Press 'q' to quit the application

## ⚙️ Configuration

You can customize the system behavior by modifying these parameters in the code:

```python
ear_threshold = 0.25        # EAR threshold (lower = more sensitive)
frame_counter = 20          # Frames before triggering alert
music_file = "Alert.wav"    # Path to alert sound file
```

### Recommended Settings:
- **Normal sensitivity:** `ear_threshold = 0.25`, `frame_counter = 20`
- **High sensitivity:** `ear_threshold = 0.3`, `frame_counter = 15`
- **Low sensitivity:** `ear_threshold = 0.2`, `frame_counter = 30`

## 📊 How It Works

1. **Face Detection:** Uses dlib's frontal face detector to locate faces in the video stream
2. **Landmark Detection:** Identifies 68 facial landmarks, focusing on eye regions
3. **EAR Calculation:** Computes Eye Aspect Ratio using the formula:
   ```
   EAR = (|p2-p6| + |p3-p5|) / (2|p1-p4|)
   ```
4. **Drowsiness Detection:** Monitors EAR values over consecutive frames
5. **Alert System:** Triggers audio and visual alerts when drowsiness is detected

## 🎯 Applications

- **Driver monitoring systems** in vehicles
- **Workplace safety** for security guards, operators
- **Medical monitoring** for patients with sleep disorders
- **Educational tools** for studying attention and alertness
- **Gaming and entertainment** applications

## 🔍 Troubleshooting

**Camera not detected:**
- Check if camera is connected and not used by other applications
- Try changing camera index: `cv2.VideoCapture(1)` instead of `cv2.VideoCapture(0)`

**Face not detected:**
- Ensure adequate lighting
- Position face directly in front of camera
- Remove glasses or objects that might obstruct facial features

**Audio not playing:**
- Check if `Alert.wav` file exists in the project directory
- Verify audio file format (WAV recommended)
- Test system audio output

**Performance issues:**
- Reduce frame resolution in the code
- Close unnecessary applications
- Check CPU usage

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- [dlib library](http://dlib.net/) for facial landmark detection
- [OpenCV community](https://opencv.org/) for computer vision tools
- Research papers on Eye Aspect Ratio for drowsiness detection
- Contributors and testers who helped improve the system

## 📞 Support

If you encounter any issues or have questions, please:
- Check the troubleshooting section above
- Open an issue on GitHub
- Contact the maintainer

---

**⚠️ Disclaimer:** This system is designed for educational and assistance purposes. It should not be solely relied upon for critical safety applications. Always prioritize proper rest and safe driving practices.
