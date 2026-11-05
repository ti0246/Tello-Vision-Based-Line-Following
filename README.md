# Tello Vision-Based Line Following

A computer vision-based autonomous line-following system developed for the DJI Tello drone using Python, OpenCV, and PID control.

## Overview

This project focuses on developing a vision-based navigation system that enables a DJI Tello drone to follow a predefined line using visual information captured by its onboard camera.

The system integrates image processing, line detection, and PID-based control to process visual feedback and generate flight control commands.

## Key Features

- **Computer Vision:** Image processing using OpenCV.
- **Line Detection:** Visual line detection and tracking.
- **PID Controller:** Feedback-based control for flight adjustments.
- **Drone Communication:** Control interface for the DJI Tello.
- **HSV Tuning:** Tools for adjusting color detection parameters.
- **Camera Testing:** Utilities for testing the drone's camera feed.

## System Architecture

```text
DJI Tello Camera
       |
       v
 Image Acquisition
       |
       v
 Image Processing
       |
       v
  Line Detection
       |
       v
 PID Controller
       |
       v
 Flight Commands
       |
       v
   DJI Tello
```

## Project Structure

```text
Tello-Vision-Based-Line-Following/
│
├── main.py
├── config.py
├── requirements.txt
├── .gitignore
│
├── modules/
│   ├── line_detection.py
│   ├── pid_controller.py
│   ├── tello_controller.py
│   └── utils.py
│
└── test/
    ├── camera_test.py
    └── hsv_tuner.py
```

## Technologies

- Python
- OpenCV
- NumPy
- DJITelloPy
- Computer Vision
- PID Control

## Installation

Clone the repository:

```bash
git clone https://github.com/ti0246/Tello-Vision-Based-Line-Following.git

cd Tello-Vision-Based-Line-Following
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Power on the DJI Tello drone.
2. Connect your computer to the drone's Wi-Fi network.
3. Ensure the flight environment is safe and unobstructed.
4. Run the main program:

```bash
python main.py
```

## Project Goals

- Explore vision-based autonomous navigation.
- Implement image processing techniques for line detection.
- Apply PID control to drone navigation.
- Develop practical experience in autonomous UAV systems.

## Author

**Vu Van Thuc**

- GitHub: [@ti0246](https://github.com/ti0246)

## License

This project is currently developed for educational and research purposes.

---

*Developed as part of an ongoing exploration of Computer Vision and Autonomous Drone Systems.*
