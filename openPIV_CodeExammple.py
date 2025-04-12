'''
To use the code
python3 openPIV <path to parameter file>

input_folder: '<Images Folder>/'
output_folder: '<Results Folder>/'
extension: 'tif' extension of the images to be processed ('jpg', 'png', 'tif', etc.)


The code processes the Images without preprocessing, 
save the results and plots the first PIV field.

This Code is based on the openPIV code 
'''


#Standar libraries
import numpy as np
import os
import argparse
import yaml
from openpiv import tools, pyprocess, validation, filters, scaling
from PIL import Image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process PIV images using DPIVSoft.")
    parser.add_argument("fileName", type=str, help="PIV parameter file.")
    args = parser.parse_args()


#===========================================================================
# FUNCTIONS
# ==========================================================================

#Function to compute the PIV
def computePIV(frame_a,frame_b,window_sizePIV=48,search_area_sizePIV=64,overlapPIV=24,dtPIV=1):
    
    frame_a=np.array(frame_a,dtype=np.int32)#frame_a.astype(np.int32)
    frame_b=np.array(frame_b,dtype=np.int32)#frame_b.astype(np.int32)

    u, v, sig2noise = pyprocess.extended_search_area_piv( \
            frame_a, frame_b, \
            window_size=window_sizePIV, \
            overlap=overlapPIV, \
            dt=dtPIV, \
            search_area_size=search_area_sizePIV, \
            sig2noise_method='peak2peak' )

    x, y = pyprocess.get_coordinates( \
            image_size=frame_a.shape, \
            search_area_size=search_area_sizePIV, 
            overlap=overlapPIV )
    
    
    
    return x,y,u,v,sig2noise


#Function to read the parameters from a YAML file
def readParameters(fileName):
        """
        Read parameters from a yaml file
        """
        with open(fileName) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            print("starting")
        return data
#==========================================================================






# =========================================================================
# READ PARAMETERS
# =========================================================================
# Read parameters from the YAML file
# parameterFile = args.fileName
param = readParameters(args.fileName)

#directories
dirImg = param['input_folder']
dirRes = param['output_folder']
extension = param['extension'] if param['extension'].startswith(".") else f".{param['extension']}" 

#post-processing parameters
isPostProcess=param['isPostProcess'] #True
threshold=param['threshold_sigNoise'] #1.2
kernel_size=param['kernel_size'] #5

#optional scaling
isScaling=param['isScaling'] #True
scaling_factor=param['scaling_factor'] #96.52 microns/pixel
dtPIV=param['dtPIV'] #1



#PIV analysis parameters from the parameter.yaml file
isProcessAll=param['isProcessAll'] #True
step=param['step'] #1
window_sizePIV=param['window_sizePIV'] #48
search_area_sizePIV=param['search_area_sizePIV'] #64
overlapPIV=param['overlapPIV']#8 (needs to be smaller than the window size)

# =========================================================================


# =========================================================================
# SETING UP FOLDERS
# Check if the input folder is empty
# =========================================================================
if not os.path.exists(dirImg):
    print(f"Error: Input folder '{dirImg}' does not exist.")
    exit(1)
if not os.path.exists(dirRes):
    os.makedirs(dirRes)


# =========================================================================
# LIST OF IMAGES TO PROCESS
# =========================================================================
files = sorted([f for f in os.listdir(dirImg) if f.endswith(extension)])
if len(files) < 2:
    print("Error: Not enough images to process. At least two images are required.")
    exit(1)
print(f"Found {len(files)} images to process: {files}")


# =========================================================================
# PROCESSING of IMAGES
# =========================================================================
if isProcessAll:
    # Process all images
    for i in range(0, len(files)-1, step):
        imageFile1=dirImg+files[i]
        imageFile2=dirImg+files[i+1]
        image1=Image.open(imageFile1).convert('L')
        image2=Image.open(imageFile2).convert('L')
        
        #Compute PIV
        x,y,u,v,sig2noise=computePIV(image1,image2,window_sizePIV,\
                                     search_area_sizePIV,overlapPIV,dtPIV)
        # =========================================================================
        # POST-PROCESSING 
        # =========================================================================

        if isPostProcess:
             #filter outliers
            invalid_mask = validation.sig2noise_val(
                            sig2noise,
                            threshold = threshold
                            )#local_median_val( u, v,7,7,size=1 )
                #u, v = openpiv.filters.replace_outliers( u, v, method='localmean', max_iter=5,kernel_size=2)
            u2, v2 = filters.replace_outliers(u, v,invalid_mask,method='localmean',max_iter=3,kernel_size=kernel_size)
        else:
            u2, v2 = u, v

        if isScaling:
            #optional scaling:

            # convert x,y to mm
            # convert u,v to mm/sec
            x, y, u3, v3 = scaling.uniform(x, y, u2, v2, 
                                           scaling_factor = scaling_factor ) # 96.52 microns/pixel
        else:
            x, y, u3, v3 = x, y, u2, v2

        #optional rotation of the coordinate system:

        # 0,0 shall be bottom left, positive rotation rate is counterclockwise
        x4, y4, u4, v4 = tools.transform_coordinates(x, y, u3, v3)
        #save results
        tools.save(dirRes+'pivFields_' + files[i].split('.')[0]+'.txt', x4, y4, u4, v4)

else:
    # Process only the first two images
    if len(files) > 2:
        print("Warning: More than 2 images found, processing only the first two.")


    #Process two Images
    imageFile1=dirImg+files[0]
    imageFile2=dirImg+files[1]
    image1=Image.open(imageFile1).convert('L')
    image2=Image.open(imageFile2).convert('L')


    #Compute PIV
    x,y,u,v,sig2noise=computePIV(image1,image2,window_sizePIV,\
    search_area_sizePIV,overlapPIV,dtPIV)
    # =========================================================================
    # POST-PROCESSING 
    # =========================================================================

    if isPostProcess:
            #filter outliers
        invalid_mask = validation.sig2noise_val(
                        sig2noise,
                        threshold = threshold
                        )#local_median_val( u, v,7,7,size=1 )
            #u, v = openpiv.filters.replace_outliers( u, v, method='localmean', max_iter=5,kernel_size=2)
        u2, v2 = filters.replace_outliers(u, v,invalid_mask,method='localmean',max_iter=3,kernel_size=kernel_size)
    else:
        u2, v2 = u, v

    if isScaling:
        #optional scaling:

        # convert x,y to mm
        # convert u,v to mm/sec
        x, y, u3, v3 = scaling.uniform(x, y, u2, v2, 
                                        scaling_factor = scaling_factor ) # 96.52 microns/pixel
    else:
        x, y, u3, v3 = x, y, u2, v2

    #optional rotation of the coordinate system:

    # 0,0 shall be bottom left, positive rotation rate is counterclockwise
    x4, y4, u4, v4 = tools.transform_coordinates(x, y, u3, v3)
    #save results

    #save in the simple ASCII table format
    tools.save(dirRes+'FirstTwoImages.txt', x4, y4, u4, v4)


