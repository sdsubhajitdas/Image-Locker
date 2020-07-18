import os
from PIL import Image
from mimetypes import MimeTypes
from image_encryptor import *
import numpy as np


def checkIfImage(filePath: str):
    """Checks if a given image is image type or not."""
    if os.path.exists(filePath):
        mimeType = MimeTypes().guess_type(filePath)[0]
        if mimeType:
            mimeType = mimeType.split("/")[0]
        else:
            return False
        return True if(mimeType == "image") else False
    else:
        print("File does not exit")


def getImageDims(width: int, height: int,):
    while height*width > DIM_HEIGHT*DIM_WIDTH:
    #while height > DIM_HEIGHT or width > DIM_WIDTH:
        height = int(height*0.90)
        width = int(width*0.90)

    return (width, height)


def openSingleImage(imagePath: str):
    """ Reads an image from disk, resizes it to below 1080p and then changes
        it to numpy array.
    """
    image = Image.open(imagePath)
    width, height = getImageDims(image.size[0], image.size[1])
    image = image.resize((width, height))
    return np.array(image)
