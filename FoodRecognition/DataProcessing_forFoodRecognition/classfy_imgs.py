import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def main():

    imgdir = "/Users/sota/Labratory_Local/FoodRecognition/data/imgs"
    cucumber_inside_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/cucumberinside_imgs"
    cucumber_outside_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/cucumberoutside_imgs"
    eggplant_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/eggplant_imgs"
    gumi_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/gumi_imgs"
    konnyaku_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/konnyaku_imgs"
    marshmallow_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/marshmallow_imgs"
    kamaboko_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/kamaboko_imgs"

    imgnames = os.listdir(imgdir)

    for imgname in imgnames:

        if imgname == ".DS_Store":
            continue #in MacOS, hidden file is everytime generated, so if filename is this hidden file, process is skiped

        if imgname.split("_")[0] == "cucumberinside" :
            os.rename(imgdir + "/" +  imgname, cucumber_inside_dir + "/" + imgname)

        if imgname.split("_")[0] == "cucumberoutside" :
            os.rename(imgdir + "/" +  imgname, cucumber_outside_dir + "/" + imgname)

        if imgname.split("_")[0] == "konnyaku" :
            os.rename(imgdir + "/" +  imgname, konnyaku_dir + "/" + imgname)

        if imgname.split("_")[0] == "eggplant" :
            os.rename(imgdir + "/" +  imgname, eggplant_dir + "/" + imgname)

        if imgname.split("_")[0] == "gumi" :
            os.rename(imgdir + "/" +  imgname, gumi_dir + "/" + imgname)

        if imgname.split("_")[0] == "marshmallow" :
            os.rename(imgdir + "/" +  imgname, marshmallow_dir + "/" + imgname)

        if imgname.split("_")[0] == "kamaboko" :
            os.rename(imgdir + "/" +  imgname, kamaboko_dir + "/" + imgname)


        print(imgname)

if __name__ == '__main__':
    main()
