# Object Tracking Demo

For learning and testing the performance of [object tracking using the Ultralytics implementation of YOLOv8](https://docs.ultralytics.com/modes/track/#tracking) (You Only Look Once) real-time object detection system. 

## Table of Contents
- [Suggested Tools](#suggested-tools)
    1. [Version Manager](#version-manager)
    2. [Virtual Environment Creation and Activation](#virtual-environment-creation-and-activation)
    3. [Install Dependencies](#install-dependencies)
- [Usage](#usage)
- [Explanation](#explanation)

## Suggested Tools
The [official tool set](https://packaging.python.org/en/latest/guides/tool-recommendations/) does not support version management. As a result, teams on different operating systems and devices will encounter interpreter version conflicts (e.g., dependencies that work on one device but not on others).

This section offers a solution for managing virtual environments, Python interpreter versions, packages, and package indexes across various devices and operating systems. 


A typical setup includes a [version manager](https://packaging.python.org/en/latest/guides/tool-recommendations/), [virtual environment](https://packaging.python.org/en/latest/glossary/#term-Virtual-Environment), and one or more package managers (like [pip](https://pip.pypa.io/en/stable/) or [conda](https://packaging.python.org/en/latest/key_projects/#conda)) to access [package indexes](https://packaging.python.org/en/latest/glossary/#term-Package-Index) that contain downloadable [packages](https://packaging.python.org/en/latest/overview/).

### 1. Version Manager

#### Windows, MacOS, and *Nix ✅

Version manager [miniconda](https://docs.anaconda.com/free/miniconda/index.html) and package manager [conda](https://packaging.python.org/en/latest/key_projects/#conda) ensures a reliable and consistent environment setup across different operating systems. It works well in conjunction with [pip](https://pip.pypa.io/en/stable/), allowing you to easily install and manage packages from various package indexes. [Miniconda installation instructions](https://docs.anaconda.com/free/miniconda/index.html#quick-command-line-install).

#### Raspberry Pi ✅
Miniconda is not officially supported, despite the apparent availability of aarch-64 installers with every update. [Miniforge](https://github.com/conda-forge/miniforge) has proven to be an effective alternative on Raspberry Pi 4 Bookworm OS. [Installation instructions](https://github.com/conda-forge/miniforge/?tab=readme-ov-file#install).

#### Official Tool Stack ❌
Manual version management can be performed if multiple versions of python are installed on a local system by specifying a python interpreter version while [creating a new virtual environment](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments) with [venv](https://packaging.python.org/en/latest/key_projects/#venv) or [virtualenv](https://packaging.python.org/en/latest/key_projects/). This method only includes pip, which limits package index to [PyPI](https://packaging.python.org/en/latest/glossary/#term-Python-Package-Index-PyPI) solely.

### 2. Virtual Environment Creation and Activation
```bash
conda create -n .minienv python=3.11 -y
```
```bash
conda activate .minienv
```
#### ~/.bashrc Settings

If miniconda has been installed, `conda init` appended a conda initialization script to the bottom of `~/.bashrc`. See `conda init -h` for more info. 

If bash shell starts with the Conda `(base)` environment activated:
```bash
conda config --set auto_activate_base false
```

Then, restart shell or open a new terminal window for the changes to take effect.

#### VSCode Automatic Interpreter Selection and Activation Setting
Automatically activate the new virtual environment's python interpreter with vscode settings. 

Bash:

```bash
mkdir -p .vscode && echo '{"python.pythonPath": "/home/pi/miniforge3/envs/.minienv/bin/python"}' > .vscode/settings.json
```

Windows command line with virtual environment from venv named 'venv':
```bash
source venv/bin/activate
```

```cmd
mkdir -p .vscode && echo '{"python.pythonPath": "venv/Scripts/python.exe"}' > .vscode/settings.json
```


### 3. Install Dependencies
Install packages with conda but use pip if package is not in conda.
```bash
conda install -requirements.txt || pip install -r requirements.txt
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