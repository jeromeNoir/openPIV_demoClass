# openPIV_demoClass

For more information visit the original repository: [openPIV](https://github.com/OpenPIV/openpiv-python)

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

