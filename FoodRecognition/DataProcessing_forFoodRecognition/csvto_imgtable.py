import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#need to align length of data and to remove axis! → done(20210123)

def main():

    datadir = "/Users/sota/Labratory_Local/FoodRecognition/data/formalized_data"
    imgdir = "/Users/sota/Labratory_Local/FoodRecognition/data/imgs"
    filenames = os.listdir(datadir)
    nunber_delarray = 0 # 0th array in data of this time has no meaning, so delete it
    extension = ".jpg"
    max_dataarray_one = -np.inf
    max_dataarray_seccound = -np.inf
    min_dataarray_one = np.inf
    min_dataarray_seccound = np.inf

    max_alldata = -np.inf
    min_alldata = np.inf

    max_dataarraysize = 0
    cap_dataarraysize = 2000

    reachcap_filenames = []

    for filename in filenames:
        if filename == ".DS_Store":
            continue #in MacOS, hidden file is everytime generated, so if filename is this hidden file, process is skiped

        csv = pd.read_csv(datadir + "/" + filename, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
        data_delbefore = np.array(csv, dtype = np.float32).T
        data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
        dataarray_one = data_deleted[0] - data_deleted[0][0] #tare processing
        dataarray_secound = data_deleted[1] - data_deleted[1][0] #tare processing

        max_dataarray_one = np.max(dataarray_one)
        max_dataarray_seccound = np.max(dataarray_secound)
        min_dataarray_one = np.min(dataarray_one)
        min_dataarray_seccound = np.min(dataarray_secound)

        max_alldata = max(max_dataarray_one, max_dataarray_seccound, max_alldata)
        min_alldata = min(min_dataarray_one, min_dataarray_seccound, min_alldata)

        print(filename)
        print("max")
        print(max_alldata)
        print("\n")
        print("min")
        print(min_alldata)
        print("\n")
        print("maxdatasize")
        print(max_dataarraysize)
        print("\n")

        if (dataarray_one.size > cap_dataarraysize) or (dataarray_secound.size > cap_dataarraysize):
            print("reach cap size")
            reachcap_filenames.append(filename)
            continue #cap data size.

        max_dataarraysize = max(dataarray_one.size, dataarray_secound.size, max_dataarraysize)

    print("-" * 20)

    for filename in filenames:

        if filename == ".DS_Store":
            continue #in MacOS, hidden file is everytime generated, so if filename is this hidden file, process is skiped

        if filename in reachcap_filenames:
            continue # skip reach cap data

        csv = pd.read_csv(datadir + "/" + filename, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
        data_delbefore = np.array(csv, dtype = np.float32).T
        data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
        dataarray_one = data_deleted[0] - data_deleted[0][0] #tare processing
        dataarray_secound = data_deleted[1] - data_deleted[1][0] #tare processing

        imgname = filename.split(".")[0]
        fig = plt.figure()
        print(imgname)

        if index == 0:
            ax1 = fig.add_subplot(3, 3, 1)
            ax1.figure(figsize=(4.0, 4.0))

            ax1.figure(figsize=(4.0, 4.0))
            ax1.xlim(0, max_dataarraysize)
            ax1.ylim(min_alldata, max_alldata)
            ax1.plot(dataarray_one, linewidth = 0.5)
            ax1.plot(dataarray_secound, linewidth = 0.5)

            ax1.savefig(imgdir + "/" + imgname + extension)


        elif == 1:
            ax2 = fig.add_subplot(3, 3, 1)
            ax2.figure(figsize=(4.0, 4.0))

            ax2.figure(figsize=(4.0, 4.0))
            ax2.xlim(0, max_dataarraysize)
            ax2.ylim(min_alldata, max_alldata)
            ax2.plot(dataarray_one, linewidth = 0.5)
            ax2.plot(dataarray_secound, linewidth = 0.5)

            ax2.savefig(imgdir + "/" + imgname + extension)

        elif == 2:
            ax3 = fig.add_subplot(3, 1, 1)
            ax3.figure(figsize=(4.0, 4.0))

            ax3.figure(figsize=(4.0, 4.0))
            ax3.xlim(0, max_dataarraysize)
            ax3.ylim(min_alldata, max_alldata)
            ax3.plot(dataarray_one, linewidth = 0.5)
            ax3.plot(dataarray_secound, linewidth = 0.5)

            ax3.savefig(imgdir + "/" + imgname + extension)

        elif == 3:

        elif == 4:

        elif == 5:

        elif == 6:

        elif == 7:

        else:
            plt.savefig(imgdir + "/" +"table" + str(index) + extension)
            plt.clf()
            index +=1

if __name__ == '__main__':
    main()
