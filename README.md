# openPIV_demoClass

For more information about openPIV visit the original repository: [openPIV](https://github.com/OpenPIV/openpiv-python)

## To Install openPIV
* create a environment:
  * Best: Use the Anaconda Navigator
  * Alternative:
    _conda create --name openpiv python=3.11.11_
* activate the environment:
    _conda activate openpiv_

* Install openPIV: _pip install openpiv_

## Additional installs:

* ipykernel: _pip install ipykernel_
* siphash24: _pip install siphash24_
* openCV (recommended for video editing): _pip install opencv-python_


# OpenPIV Python Scripts

This repository contains two Python scripts for processing and visualizing Particle Image Velocimetry (PIV) data using the `openpiv` library:

1. **`openPIV_codeExammple.py`**: Processes PIV images and generates vector field data.
2. **`plot_PIVfileds.py`**: Visualizes the PIV vector fields, optionally overlaying them on an image.

---

## Requirements

Before using the scripts, ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  - `numpy`
  - `matplotlib`
  - `openpiv`
  - `Pillow`
  - `PyYAML`
 
### To Install openPIV
* create a environment:
  * Best: Use the Anaconda Navigator
  * Alternative:
    _conda create --name openpiv python=3.11.11_
* activate the environment:
    _conda activate openpiv_

* Install openPIV: _pip install openpiv_

### Additional installs (not always required, depends on your OS):

* ipykernel: _pip install ipykernel_
* siphash24: _pip install siphash24_
* openCV (recommended for video editing): _pip install opencv-python_


## openPIV_codeExammple.py :
### Description
This script processes PIV images based on parameters specified in a YAML configuration file. It performs PIV analysis, post-processing, scaling, and saves the results as vector field data.

### usage
python openPIV_codeExammple.py <parameterFile>


### Arguments
parameterFile: Path to the YAML file containing PIV processing parameters.

## Example of parameter file:
- input_folder: "./input_images/"
- output_folder: "./output_results/"
- extension: ".png"
- isPostProcess: True
- threshold_sigNoise: 1.2
- kernel_size: 5
- isScaling: True
- scaling_factor: 96.52
- dtPIV: 1
- isProcessAll: True
- step: 1
- window_sizePIV: 48
- search_area_sizePIV: 64
- overlapPIV: 24

### Output
Processed PIV vector fields saved as text files in the specified output folder.

## plot_PIVfileds.py

### Description
This script visualizes the PIV vector fields generated by openPIV_codeExammple.py. It can optionally overlay the vector field on an image.

### usage
python plot_PIVfileds.py <fileName> [--scaling_factor <float>] [--scale <float>] 
                         [--width <float>] [--on_img <bool>] [--image_name <str>]

or simply without options
python plot_PIVfileds.py <fileName> 

### Arguments

* fileName: Path to the PIV vector field file (e.g., .txt or .dat).
* --scaling_factor: Scaling factor for the image (default: 1). 
* --scale: Arrow length in the vector field (default: 50).
* --width: Thickness of the arrows (default: 0.0035).
* --image_name: Path to the image to overlay with PIV field.(if not specified, noe image overlay)

example: 
python plot_PIVfileds.py vectors.txt --scaling_factor 2 --scale 75 --width 0.004 --on_img True --image_name background.png

### output
A plot of the vector field, optionally overlaid on the specified image.

## Workflow
* Prepare a YAML configuration file for openPIV_codeExammple.py.
* Place the input images in the folder specified in the YAML file.
* Run openPIV_codeExammple.py to process the images and generate vector field data.
* Use plot_PIVfileds.py to visualize the vector fields.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
OpenPIV Library























# TO RUN THE CODE EXAMPLE
"""
Script to process Particle Image Velocimetry (PIV) images.

* Usage:
   _python openPIV_codeExammple.py parameterFile_

* Arguments:
    parameterFile (str): Path to the YAML file containing PIV processing parameters.

* Description:
    This script processes PIV images using the `openpiv` library. It reads parameters 
    from a YAML configuration file, performs PIV analysis on pairs of images, and 
    optionally applies post-processing, scaling, and coordinate transformations. 
    The results are saved as text files in the specified output directory.

* Steps:
    1. Prepare a YAML file with the required parameters (e.g., input/output folders, 
       PIV settings, post-processing options).
    2. Place the images to be processed in the input folder specified in the YAML file.
    3. Run the script with the path to the YAML file as an argument.

* Example:
    python openPIV_codeExammple.py parameters.yaml

* YAML File Example:
    input_folder: "./input_images/"
    output_folder: "./output_results/"
    extension: ".png"
    isPostProcess: True
    threshold_sigNoise: 1.2
    kernel_size: 5
    isScaling: True
    scaling_factor: 96.52
    dtPIV: 1
    isProcessAll: True
    step: 1
    window_sizePIV: 48
    search_area_sizePIV: 64
    overlapPIV: 24

* Requirements:
    - Python 3.x
    - Libraries: numpy, openpiv, PIL, PyYAML

* Output:
    - Processed PIV vector fields saved in the output folder as text files.
"""

