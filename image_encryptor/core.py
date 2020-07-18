import base64
from cryptography.fernet import Fernet, InvalidToken
from image_encryptor import utils, keys
from image_encryptor import *
from tqdm import tqdm
import os
import sys
from PIL import Image
import numpy as np


def __writeEncryptedImage(imagePath: str, imageEncrypted: str, single):
    """Writes encrypted image on to disk"""
    if not os.path.exists(ENCRYPTED_OUTPUT_DIR):
        os.makedirs(ENCRYPTED_OUTPUT_DIR)

    imageName = os.path.basename(imagePath) + ".txt"

    outputFileName = imageName if single else os.path.join(
        ENCRYPTED_OUTPUT_DIR, imageName)

    with open(outputFileName, "w") as file:
        file.write(imageEncrypted.decode())

    if single:
        print(f"Output file at location :  {outputFileName}")


def encryptSingleImage(imagePath: str, password: str, single=True):
    """Encrypts one single image"""
    image = utils.openSingleImage(imagePath)
    shape = ""
    for dim in image.shape:
        shape = shape + str(dim) + " "

    image = list(map(str, image.flatten()))
    image = shape + ","+" ".join(image)
    # print(image[:20])

    passKey = keys.getPasswordGeneratedKey(password)
    imageEncrypted = Fernet(passKey).encrypt(image.encode())
    __writeEncryptedImage(imagePath, imageEncrypted, single)


def encryptDirectory(dirPath: str, password):
    """Encrypts whole directory of images excluding others"""
    imageList = os.listdir(dirPath)

    for _ in tqdm(range(len(imageList))):
        imageName = imageList[_]
        imagePath = os.path.join(dirPath, imageName)
        if(utils.checkIfImage(imagePath)):
            encryptSingleImage(imagePath, password, single=False)


def __writeDecryptedImage(encryptedImagePath: str, image, single):
    """Writes original image on to disk"""
    if not os.path.exists(DECRYPTED_OUTPUT_DIR):
        os.makedirs(DECRYPTED_OUTPUT_DIR)

    imageName = os.path.basename(encryptedImagePath)[:-4]

    outputFileName = imageName if single else os.path.join(
        DECRYPTED_OUTPUT_DIR, imageName)

    image = Image.fromarray(np.uint8(image))
    image.save(outputFileName)

    if single:
        print(f"Output file at location :  {outputFileName}")


def decryptSingleImage(encryptedimagePath: str, password: str, single=True):
    encryptedimage = None
    with open(encryptedimagePath, 'r') as file:
        encryptedimage = file.read()

    passKey = keys.getPasswordGeneratedKey(password)
    try:
        image = Fernet(passKey).decrypt(encryptedimage.encode())
        image = image.decode()
        # print(image[:20])
    except InvalidToken:
        print("\tWrong Password! Try Again")
        sys.exit(0)

    shape, image = image.split(',')
    shape = list(map(int, shape.strip().split()))
    image = list(map(int, image.strip().split()))
    image = np.resize(np.array(image), shape)

    __writeDecryptedImage(encryptedimagePath, image, single)


def decrptDirectory(dirPath: str, password):
    encryptedimageList = os.listdir(dirPath)

    for _ in tqdm(range(len(encryptedimageList))):
        encryptedimageName = encryptedimageList[_]
        encryptedimagePath = os.path.join(dirPath, encryptedimageName)
        decryptSingleImage(encryptedimagePath, password, single=False)
