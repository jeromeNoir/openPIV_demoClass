"""
Script to plot Particle Image Velocimetry (PIV) results.

Usage:
    python plot_PIVfileds.py <fileName> [--scaling_factor <float>] [--scale <float>] 
                             [--width <float>] [--image_name <str>]

Arguments:
    fileName (str): Path to the PIV parameter file containing vector field data.
    --scaling_factor (float): Scaling factor for the image (default: 1).
    --scale (float): Scale defines the arrow length in the vector field (default: 50).
    --width (float): Thickness of the arrows in the vector field (default: 0.0035).
    --image_name (str): Path to the image file to overlay the vector field on (optional).

Example:
    python plot_PIVfileds.py vectors.txt --scaling_factor 2 --scale 75 --width 0.004 --image_name background.png

Description:
    This script reads a PIV parameter file and optionally overlays the vector field on an image.
    It uses the `openpiv` library for processing and `matplotlib` for visualization.
"""

import matplotlib.pyplot as plt
import argparse
from openpiv import tools


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="plot PIV results.")
    parser.add_argument("fileName", type=str, help="PIV parameter file.")
    parser.add_argument("--scaling_factor", type=float, default=1, help="scaling factor for the image")
    parser.add_argument("--scale", type=float, default=50, help="scale defines here the arrow length")
    parser.add_argument("--width", type=float, default=0.0035, help="width is the thickness of the arrow")
    parser.add_argument("--image_name", type=str, default=None, help="name of the image to overlay the arrows on")
    args = parser.parse_args()

# print (args.fileName)

if args.image_name is None:
    isImageOn = False
else:
    isImageOn = True
    # check if the image exists
    try:
        img = tools.imread(args.image_name)
    except FileNotFoundError:
        print(f"Image {args.image_name} not found.")
        isImageOn = False

#plot the results
fig, ax = plt.subplots(figsize=(8,8))
tools.display_vector_field(args.fileName, 
                           ax=ax, scaling_factor=args.scaling_factor, # scaling factor for the image
                           scale=args.scale, # scale defines here the arrow length
                           width=args.width, # width is the thickness of the arrow
                           on_img=isImageOn, # overlay on the image
                           image_name=args.image_name);


