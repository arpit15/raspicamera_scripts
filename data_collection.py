from camera_util import get_camera
from camera_util import cap_jpeg
from argparse import ArgumentParser
import numpy as np
from os.path import join
import matplotlib.pyplot as plt

if __name__ == '__main__':

    parser = ArgumentParser(description='Create RGB image from individual image')
    parser.add_argument('--folder', '-f', type=str, 
          default = "../test/",
          help='output folder containing all captured images')
    parser.add_argument('--filename', '-n', type=str, 
          default = "test",
          help='output folder containing all captured images')
    parser.add_argument('-s', action='store_true', default=False, help='single imaging mode')
    parser.add_argument('-m', action='store_true', default=False, help='multiple imaging mode')
    parser.add_argument('--camera','-c', type=str, default='v1', help='camera type: v1, v2')
    parser.add_argument('--exposure','-e', type=int, nargs='+', help='list of exposure value')
    default_exposure = range(8,22)


    args = parser.parse_args()
    
    camera = get_camera(args.camera)
    if args.s:
        fn = args.folder+args.filename
        output, _ = cap_jpeg(camera=camera,name="%s.jpeg"%fn, returnOut=False)
    elif args.m:
        if args.exposure is None:
            args.exposure = default_exposure

        exposure = []
        for i in args.exposure:
            exposure.append(2**i)

        for e in exposure:
            print(e)
            fn = args.folder+args.filename+'exp%s'%(e)
            output, _ = cap_jpeg(camera,e, "%s.jpeg"%fn, False)
    camera.close()
