# Object Tracking Demo

For learning and testing the performance of [object tracking using the Ultralytics implementation of YOLOv8](https://docs.ultralytics.com/modes/track/#tracking) (You Only Look Once) real-time object detection system. 

## Table of Contents
- [Suggested Tools](#suggested-tools)
- [Version and Package Managers](#version-and-package-managers)
- [Virtual Environment Creation and Activation](#virtual-environment-creation-and-activation)
- [Usage](#usage)
- [Explanation](#explanation)

## Suggested Tools
The [official tool set](https://packaging.python.org/en/latest/guides/tool-recommendations/) does not support version management. As a result, teams on different operating systems and devices will encounter interpreter version conflicts (e.g., dependency works on one device but not on another).

This section offers a solution for managing virtual environments, Python interpreter versions, packages, and package indexes across various devices and operating systems. 


A typical setup includes a [virtual environment](https://packaging.python.org/en/latest/glossary/#term-Virtual-Environment), [version manager](https://packaging.python.org/en/latest/guides/tool-recommendations/), and one or more package managers (like [pip](https://pip.pypa.io/en/stable/) or [conda](https://packaging.python.org/en/latest/key_projects/#conda)) to access [package indexes](https://packaging.python.org/en/latest/glossary/#term-Package-Index) that contain downloadable [packages](https://packaging.python.org/en/latest/overview/).

### Windows, MacOS, and *Nix ✅

Using the version manager [miniconda](https://docs.anaconda.com/free/miniconda/index.html) and package manager [conda](https://packaging.python.org/en/latest/key_projects/#conda) ensures a reliable and consistent environment setup across different operating systems. It works well in conjunction with [pip](https://pip.pypa.io/en/stable/), allowing you to easily install and manage packages from various package indexes.

### Raspberry Pi ✅
Miniconda is not officially supported, despite the apparent availability of aarch-64 installers with every update. [Miniforge](https://github.com/conda-forge/miniforge) has proven to be an effective alternative on Raspberry Pi 4 Bookworm OS. [Installation instructions](https://github.com/conda-forge/miniforge/?tab=readme-ov-file#install).

### Official Tool Stack ❌
Manual version management can be performed if multiple versions of python are installed on a local system by specifying a python interpreter version while [creating a new virtual environment](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments) with [venv](https://packaging.python.org/en/latest/key_projects/#venv) or [virtualenv](https://packaging.python.org/en/latest/key_projects/). This method only includes pip, which limits package index to [PyPI](https://packaging.python.org/en/latest/glossary/#term-Python-Package-Index-PyPI) soley.




## Virtual Environment Creation and Activation
```bash
conda create -n .minienv python=3.11 -y
```
```bash
conda activate .minienv
```
### ~/.bashrc Script Settings

Add quick note on `~/.bashrc` configuration, as miniconda installation may have inadvertently made some settings in bash.

### VSCode Automatic Interpreter Selection and Activation Setting
Automatically activate the new virtual environment's python interpreter with vscode settings. 

Note: the following are commands for windows command line, not bash shell.
```bash
source venv/bin/activate
```

```bash
mkdir -p .vscode && echo '{"python.pythonPath": "venv/Scripts/python.exe"}' > .vscode/settings.json
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
To explore object detection with ultralytics YOLOv8, run the following command:
```bash
python custom_module.py
```
To generate graphs for testing and benchmarking purposes, simply execute the following command:
```bash
python yolov8_demo.py
```

## YOLOv8 Demo Explanation

1. **Imports and Initializations**

    Import necessary libraries and initialize the YOLO model and tracker. Set up video source. Many functions are defined in custom_module.py. 

2. **Video Processing**: 

    The script opens the video file using OpenCV's `cv2.VideoCapture` function and loops through each frame. For each frame, it runs the YOLO model's `track` method to detect and track objects in the frame. 

3. **Working with Results**

    Store object `results` (class) properties in temporary variables that are updated with each iteration (new frame).
    - [prediction boxes reference](https://docs.ultralytics.com/modes/predict/#boxes) 
    - [results.boxes reference](https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.Boxes)

    Note, index [0] refers to the first predicted image, but in this case, model.track is passed one frame per loop iteration, so only [0] values of object results will be needed. 

3. **Live Visualization**

    The script then visualizes the results by plotting the detected objects on the frame, resizing the frame and displaying the annotated frame in a window.

4. **Graphs**

    After processing the video, the script calculates the average total processing time and average confidence over all frames, and prints these values. It also saves two graphs:  
    - `data/graphs/{tracker}_total_processing_times_graph.png`
    - `data/graphs/{tracker}_confidence_graph.png`