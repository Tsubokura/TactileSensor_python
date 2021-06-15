import os
import csv
import numpy as np
import pandas as pd


#need to align length of data and to remove axis! → done(20210123)

def main():

    datadir = "/Users/sota/Labratory_Local/FoodRecognition/data/csv_for1DCNN"
    testdir = "/Users/sota/Labratory_Local/FoodRecognition/data/test"
    filenames = os.listdir(datadir)
    nunber_delarray = 0 # 0th array in data of this time has no meaning, so delete it
    max_dataarray_one = -np.inf
    max_dataarray_seccound = -np.inf
    min_dataarray_one = np.inf
    min_dataarray_seccound = np.inf

    max_alldata = -np.inf
    min_alldata = np.inf

    max_dataarraysize = 0
    cap_dataarraysize = 2000

    paddingsize = 0

    reachcap_filenames = []

    for filename in filenames:
        if filename == ".DS_Store":
            continue #in MacOS, hidden file is everytime generated, so if filename is this hidden file, process is skiped

        csvdata = pd.read_csv(datadir + "/" + filename, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
        data_delbefore = np.array(csvdata, dtype = np.float32).T
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

        # if (dataarray_one.size > cap_dataarraysize) or (dataarray_secound.size > cap_dataarraysize):
        #     print("reach cap size")
        #     reachcap_filenames.append(filename)
        #     continue #cap data size.

        paddingsize = max( len(max_dataarraysize - dataarray_one), len(max_dataarraysize - dataarray_secound) )
        max_dataarraysize = max(dataarray_one.size, dataarray_secound.size, max_dataarraysize)




    print("-" * 20)

    for filename in filenames:
        if filename == ".DS_Store":
            continue #in MacOS, hidden file is everytime generated, so if filename is this hidden file, process is skiped

        # if filename in reachcap_filenames:
        #     continue # skip reach cap data

        csvdata = pd.read_csv(datadir + "/" + filename, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
        data_delbefore = np.array(csvdata, dtype = np.float32).T
        data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
        dataarray_one = data_deleted[0] - data_deleted[0][0] #tare processing
        dataarray_secound = data_deleted[1] - data_deleted[1][0] #tare processing

        for i in range(dataarray_one.size, max_dataarraysize):
            dataarray_one = np.append(dataarray_one, 1)

        for i in range(dataarray_secound.size, max_dataarraysize):
            dataarray_secound = np.append(dataarray_secound, 1)

        csvname = filename.split(".")[0]
        print(csvname)
        print(dataarray_one)

        with open(testdir + "/" + filename, 'w',newline="") as wf:
            writer = csv.writer(wf,delimiter='\t')
            writer.writerow(dataarray_one)
            writer.writerow(dataarray_secound)

        break

if __name__ == '__main__':
    main()
