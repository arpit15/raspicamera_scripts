from camera_util import get_camera
from camera_util import cap_jpeg
from argparse import ArgumentParser
import numpy as np
from os.path import join
import time

if __name__ == '__main__':

    parser = ArgumentParser(description='Create RGB image from individual image')
    parser.add_argument('--folder', '-f', type=str, 
          default = "../test",
          help='output folder containing all captured images')
    parser.add_argument('--filename', '-n', type=str, 
          default = "test",
          help='output folder containing all captured images')
    parser.add_argument('-s', action='store_true', default=False, help='single imaging mode')
    parser.add_argument('-m', action='store_true', default=False, help='multiple imaging mode')
    parser.add_argument('--camera','-c', type=str, default='v1', help='camera type: v1, v2')
    parser.add_argument('--exposure','-e', type=int, nargs='+', help='list of exposure value')
    default_exposure = range(4,23)


    args = parser.parse_args()
    
    camera = get_camera(args.camera)
    if args.s:
        fn = join(args.folder,args.filename)
        #start = time.time()
        output, _ = cap_jpeg(camera=camera,exposure=int(args.exposure[0]),name=f"{fn}.jpeg", returnOut=False)
        #end = time.time()
        #print("running time: {time:.2f}".format(time=end-start))
    elif args.m:
        if args.exposure is None:
            args.exposure = default_exposure

        exposure = []
        for i in args.exposure:
            exposure.append(2**i)

        for e in exposure:
            print(e)
            fn = join(args.folder,f"{args.filename}exp{e}")
            #start = time.time()
            output, _ = cap_jpeg(camera,e, f"{fn}.jpeg", False)
            #end = time.time()
            #print("running time: {time:.2f}".format(time=end-start))
    camera.close()
