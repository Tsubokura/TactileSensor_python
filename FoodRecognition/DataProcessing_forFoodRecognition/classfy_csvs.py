import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def main():

    csvdir = "/Users/sota/Labratory_Local/FoodRecognition/data/csv_for1DCNN"
    cucumber_inside_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/cucumberinside_csv"
    cucumber_outside_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/cucumberoutside_csv"
    eggplant_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/eggplant_csv"
    gumi_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/gumi_csv"
    konnyaku_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/konnyaku_csv"
    marshmallow_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/marshmallow_csv"
    kamaboko_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/kamaboko_csv"

    csvnames = os.listdir(csvdir)
    print(csvnames)

    for csvname in csvnames:

        if csvname == ".DS_Store":
            continue #in MacOS, hidden file is everytime generated, so if filename is this hidden file, process is skiped

        if csvname.split("_")[0] == "cucumberinside" :
            os.rename(csvdir + "/" +  csvname, cucumber_inside_dir + "/" + csvname)

        if csvname.split("_")[0] == "cucumberoutside" :
            os.rename(csvdir + "/" +  csvname, cucumber_outside_dir + "/" + csvname)

        if csvname.split("_")[0] == "konnyaku" :
            os.rename(csvdir + "/" +  csvname, konnyaku_dir + "/" + csvname)

        if csvname.split("_")[0] == "eggplant" :
            os.rename(csvdir + "/" +  csvname, eggplant_dir + "/" + csvname)

        if csvname.split("_")[0] == "gumi" :
            os.rename(csvdir + "/" +  csvname, gumi_dir + "/" + csvname)

        if csvname.split("_")[0] == "marshmallow" :
            os.rename(csvdir + "/" +  csvname, marshmallow_dir + "/" + csvname)

        if csvname.split("_")[0] == "kamaboko" :
            os.rename(csvdir + "/" +  csvname, kamaboko_dir + "/" + csvname)


        print(csvname)

if __name__ == '__main__':
    main()
