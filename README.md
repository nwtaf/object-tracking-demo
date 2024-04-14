# Object Tracking Demo

For learning and testing the performance of [object tracking using the Ultralytics implementation of YOLOv8](https://docs.ultralytics.com/modes/track/#tracking) (You Only Look Once) real-time object detection system. 

## Table of Contents
- [Requirements](#requirements)
    - [Version and Package Managers](#version-and-package-managers)
    - [Virtual Environment Activation](#virtual-environment-activation)
- [Usage](#usage)
- [Explaination](#explaination)

## Requirements
### Version and Package Managers

*Robust and Recommended Route:*
#### Windows, MacOS, and *Nix

Use [miniconda](https://docs.anaconda.com/free/miniconda/index.html) installer for the version and package manager [conda](https://packaging.python.org/en/latest/key_projects/#conda). Works well in conjunction with pip. 

#### Raspberry Pi:
- Miniconda is not officially supported on raspberry pi, despite the apparent availability of aarch-64 installers with every update. Instead, refer to [miniforge](https://github.com/conda-forge/miniforge) for raspberry pi installation. Miniforge has been tested and works with raspberry pi 4 Bookworm OS as of April 2024. [Installation Instructions](https://github.com/conda-forge/miniforge/?tab=readme-ov-file#install)

*Difficult Route:*

Use package manager [pip](https://pip.pypa.io/en/stable/) with [version managers](https://packaging.python.org/en/latest/guides/tool-recommendations/) like [venv](https://packaging.python.org/en/latest/key_projects/#venv) or [virtualenv](https://packaging.python.org/en/latest/key_projects/#virtualenv) to access [package index](https://packaging.python.org/en/latest/glossary/#term-Package-Index) [PyPI](https://packaging.python.org/en/latest/glossary/#term-Python-Package-Index-PyPI).

### Virtual Environment Activation
#### Conda, Miniconda, Miniforge
```bash
conda create -n minienv python=3.11 -y
```

#### VSCode Setting
This makes it so that it activates every time, but these are windows command line instructions for venv named venv.
```bash
source venv/bin/activate
```

```bash
mkdir -p .vscode && echo '{"python.pythonPath": "venv/Scripts/python.exe"}' > .vscode/settings.json
```

#### Install Dependencies
Ultralytics comes with many dependencies, including bytetrack and botsort.
```bash
pip install -r requirements.txt
```

## Usage

To run the script, simply execute the following command:

```bash
python3 yolov8_practice.py
```

## Explaination

1. **Imports and Initializations**: Import necessary libraries and initialize the YOLO model and tracker. Set up video source for processing.

2. **Video Processing**: The script opens the video file using OpenCV's `cv2.VideoCapture` function and loops through each frame. For each frame, it runs the YOLO model's `track` method to detect and track objects in the frame. 

3. **Working with Results**
- [Prediction Boxes](https://docs.ultralytics.com/modes/predict/#boxes) [results.boxes reference](https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.Boxes)
- Store object `results` (class) properties in temporary variables that are updated with each iteration (new frame).
- Note, Index [0] refers to the first predicted image, but in this case, model.track is passed one frame per iteration, so only [0] values of object results is needed. It records the preprocessing, inference, and postprocessing times for each frame, as well as the total processing time and the confidence of the detection.

3. **Live Visualization**: The script then visualizes the results by plotting the detected objects on the frame and displaying the annotated frame in a window.

4. **Results**: After processing the video, the script calculates the average total processing time and average confidence over all frames, and prints these values. It also creates two graphs: one showing the various processing times versus the frame number, and another showing the confidence versus the frame number. These graphs are saved as PNG files in the 'data/graphs/' directory.
# TODO add the following comments to the main code, make module with functions for annotating and showing frame and graphing.