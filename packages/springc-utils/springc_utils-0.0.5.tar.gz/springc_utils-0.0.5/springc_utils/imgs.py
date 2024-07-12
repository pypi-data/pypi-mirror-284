import cv2
import numpy as np

def read_img(img_path):
    return cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)

def save_img(img, sv_path, suffix=".jpg"):
    cv2.imencode(suffix, img)[1].tofile(sv_path)