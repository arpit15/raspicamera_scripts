from __future__ import (
    unicode_literals,
    absolute_import,
    print_function,
    division,
    )


import io
import time
from picamera import PiCamera
# from picamerax import PiCamera
# import picamerax.array
import numpy as np
from numpy.lib.stride_tricks import as_strided
from PIL import Image
from fractions import Fraction
import csv

def get_camera(cam_type='hq'):
    # v1
    if cam_type == 'v1':
        print("V1 camera")
        camera = PiCamera(resolution = (2592,1944))
    # v2
    elif cam_type == 'v2':
        print("v2 camera")
        camera = PiCamera(resolution=(3280, 2464))
    # HQ
    else:
        print("HQ camera")
        camera = PiCamera(resolution=(2028, 1520), framerate=Fraction(1,30), sensor_mode=2)
    # Set ISO to the desired value
    # exposure has precedence over this setting
    # 100 : lower, 400:higher, [0,1600]
    camera.iso = 100  # to set analog_gain to 1.0
    # Let the camera warm up for a couple of seconds
    time.sleep(2)
    # camera.resolution = (1024, 768)
    # camera.digital_gain = 1.0
    camera.exposure_mode = 'off'

    g = camera.awb_gains
    print("Starting gains", g)

    camera.awb_mode = 'off'
    camera.awb_gains = 1 #(Fraction(0,256), Fraction(0,256)) #g

    camera.image_denoise = False

#     camera.analog_gain = Fraction(19,16)
#     camera.digital_gain = 1

    time.sleep(2)
    print("gains", camera.awb_gains)
    print("brightness", camera.brightness)
    print("analog gain", camera.analog_gain)
    print("color effect", camera.color_effects) # default None
    # print("contrast", camera.constrast)
    print("crop", camera.crop)
    print("digital gain", camera.digital_gain)
    print("drc strength", camera.drc_strength)
    print("exposure compensation", camera.exposure_compensation)
    print("denoising", camera.image_denoise)
    print("meter mode", camera.meter_mode)
    print("saturation", camera.saturation)
    # sharpness [-100,100] , default 0 
    print("sharpness", camera.sharpness) 
#     print("exposure compensation", camera.exposure_compensation)
    return camera

def cap_jpeg(camera,exposure=None, name=None, returnOut=False):
    if name is None:
        fname = './snap%05d.png'%exposure
    else:
        fname = name
    if exposure is not None:
        ratio = 1e6/(exposure*1.5)
        if ratio > 1:
            framerate = np.min((int(ratio),70))
        else:
            framerate = Fraction(1,int(1/ratio))
        #print("framerate: ", framerate)
        camera.framerate = framerate
        camera.shutter_speed = exposure
    camera.capture(name, 'jpeg',bayer=True)


    if returnOut:
        print("return output")
        image = Image.open(name)
        output = np.array(image)
    else: output = None

    measured_exp = camera.shutter_speed
    print("Exposure val:%5d"%measured_exp)
    return output, measured_exp
