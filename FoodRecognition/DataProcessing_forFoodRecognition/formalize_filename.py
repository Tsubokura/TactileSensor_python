import os

def main():
    datadir = "/Users/sota/Labratory_Local/FoodRecognition/data/csvdata"
    filenames = os.listdir(datadir)

    for filename in filenames:
        if filename == ".DS_Store":
            continue #in MacOS, hidden file is everytime generated, so if filename is this hidden file, process is skiped

        print(filename)
        splited_filename = filename.split(".")
        new_filename = splited_filename[1] + "_" + splited_filename[0] + "_" + splited_filename[2] + ".csv"

        os.rename(datadir + "/" +  filename, datadir + "/" + new_filename)

if __name__ == '__main__':
    main()
