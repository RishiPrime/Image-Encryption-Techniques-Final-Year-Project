from PIL import Image
import numpy as np
import pickle

import Paillier

def ImgEncrypt(public_key, plainimg):
    cipherimg = np.asarray(plainimg)
    shape = cipherimg.shape
    cipherimg = cipherimg.flatten().tolist()
    cipherimg = [Paillier.Encrypt(public_key, pix) for pix in cipherimg]
    
    return np.asarray(cipherimg).reshape(shape)


def ImgDecrypt(public_key, private_key, cipherimg):
    shape = cipherimg.shape
    plainimg = cipherimg.flatten().tolist()
    plainimg = [Paillier.Decrypt(public_key, private_key, pix) for pix in plainimg]
    plainimg = [pix if pix < 255 else 255 for pix in plainimg]
    plainimg = [pix if pix > 0 else 0 for pix in plainimg]
    
    return Image.fromarray(np.asarray(plainimg).reshape(shape).astype(np.uint8))


def homomorphicBrightness(public_key, cipherimg, factor):
    shape = cipherimg.shape
    brightimg = cipherimg.flatten().tolist()
    factor = max(-255, min(255, factor))
    brightimg = [Paillier.homomorphic_add_constant(public_key, pix, factor) for pix in brightimg]
    
    return np.asarray(brightimg).reshape(shape)
import os

def saveEncryptedImg(cipherimg, filename):
    directory = "ENCRYPT"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, "wb") as fstream:
        pickle.dump(cipherimg, fstream)
        
    # filename = "encrypted-images/" + filename
    # fstream = open(filename, "wb")
    # pickle.dump(cipherimg, fstream)
    # fstream.close()


def loadEncryptedImg(filename):
    filename = "encrypted-images/" + filename    
    fstream = open(filename, "rb")
    cipherimg = pickle.load(fstream)
    fstream.close()
    return cipherimg