from camera_util import get_camera
from camera_util import cap_jpeg
from argparse import ArgumentParser
import numpy as np
from os.path import join
import matplotlib.pyplot as plt

if __name__ == '__main__':

    parser = ArgumentParser(description='Create RGB image from individual image')
    parser.add_argument('--folder', '-f', type=str, 
          default = "/media/arpit/datadisk1/prosilica_imagesetup/brdf_char_v4",
          help='output folder containing all captured images')
    parser.add_argument('-s', action='store_true', default=False, help='single imaging mode')
    parser.add_argument('-m', action='store_true', default=False, help='multiple imaging mode')
    


    args = parser.parse_args()
    
    camera = get_camera('v2')
    if args.s:
        fn = args.folder
        output, _ = cap_jpeg(camera=camera,name="%s.jpeg"%fn, returnOut=False)
    elif args.m:
        exposure = []

        #for i in range(6,23):
        #    exposure.append(2**i)

        exposure.append(int(5e6))
        exposure.append(int(6e6))
        for e in exposure:
            print(e)
            fn = args.folder+'/exp%s'%(e)
            output, _ = cap_jpeg(camera,e, "%s.jpeg"%fn, False)
    camera.close()
