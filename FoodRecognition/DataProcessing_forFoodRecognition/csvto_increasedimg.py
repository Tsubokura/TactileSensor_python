# coding:utf-8
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import re
import os


def list_csvs(directory):
  filename_list = []
  filenames = os.listdir(directory)
  for filename in filenames:

    if filename == ".DS_Store":
            continue #in MacOS, hidden file is everytime generated, so if filename is this hidden file, process is skiped

    filename = os.path.join(directory, filename)
    filename_list.append(filename)

  return filename_list

max_dataarraysize = 4423
max_alldata = 1.5
min_alldata = -1.5 #予め求めた
imgindex = 0
extension = ".jpg"

datadir = "/Users/sota/Labratory_Local/FoodRecognition/data"
dataarrays = []

for csvname in list_csvs(datadir + '/cucumberinside_csv/'):

  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 50):

    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    plt.figure(figsize=(2.0, 2.0))
    plt.xlim(0, max_dataarraysize)
    plt.ylim(min_alldata, max_alldata)
    plt.plot(data_array_zero.T[0], linewidth = 0.5)
    plt.plot(data_array_zero.T[1], linewidth = 0.5)

    plt.savefig(datadir + '/cucumberinside_imgs/' + str(imgindex) + extension)
    plt.clf()
    plt.close()
    imgindex += 1

print("imgindex")
print(imgindex)
imgindex = 0

for csvname in list_csvs(datadir + '/cucumberoutside_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 50):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    plt.figure(figsize=(2.0, 2.0))
    plt.xlim(0, max_dataarraysize)
    plt.ylim(min_alldata, max_alldata)
    plt.plot(data_array_zero.T[0], linewidth = 0.5)
    plt.plot(data_array_zero.T[1], linewidth = 0.5)

    plt.savefig(datadir + '/cucumberoutside_imgs/' +str(imgindex) + extension)
    plt.clf()
    plt.close()
    imgindex += 1

print("imgindex")
print(imgindex)
imgindex = 0

for csvname in list_csvs(datadir + '/eggplant_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 50):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    plt.figure(figsize=(2.0, 2.0))
    plt.xlim(0, max_dataarraysize)
    plt.ylim(min_alldata, max_alldata)
    plt.plot(data_array_zero.T[0], linewidth = 0.5)
    plt.plot(data_array_zero.T[1], linewidth = 0.5)

    plt.savefig(datadir + '/eggplant_imgs/' +str(imgindex) + extension)
    plt.clf()
    plt.close()
    imgindex += 1

print("imgindex")
print(imgindex)
imgindex = 0


for csvname in list_csvs(datadir + '/konnyaku_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 50):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    plt.figure(figsize=(2.0, 2.0))
    plt.xlim(0, max_dataarraysize)
    plt.ylim(min_alldata, max_alldata)
    plt.plot(data_array_zero.T[0], linewidth = 0.5)
    plt.plot(data_array_zero.T[1], linewidth = 0.5)

    plt.savefig(datadir + '/konnyaku_imgs/' + str(imgindex) + extension)
    plt.clf()
    plt.close()
    imgindex += 1

print("imgindex")
print(imgindex)
imgindex = 0

for csvname in list_csvs(datadir + '/gumi_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 50):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    plt.figure(figsize=(2.0, 2.0))
    plt.xlim(0, max_dataarraysize)
    plt.ylim(min_alldata, max_alldata)
    plt.plot(data_array_zero.T[0], linewidth = 0.5)
    plt.plot(data_array_zero.T[1], linewidth = 0.5)

    plt.savefig(datadir + '/gumi_imgs/' + str(imgindex) + extension)
    plt.clf()
    plt.close()
    imgindex += 1

print("imgindex")
print(imgindex)
imgindex = 0

for csvname in list_csvs(datadir + '/kamaboko_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 50):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    plt.figure(figsize=(2.0, 2.0))
    plt.xlim(0, max_dataarraysize)
    plt.ylim(min_alldata, max_alldata)
    plt.plot(data_array_zero.T[0], linewidth = 0.5)
    plt.plot(data_array_zero.T[1], linewidth = 0.5)

    plt.savefig(datadir + '/kamaboko_imgs/' + str(imgindex) + extension)
    plt.clf()
    plt.close()
    imgindex += 1

print("imgindex")
print(imgindex)
imgindex = 0

for csvname in list_csvs(datadir + '/marshmallow_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 50):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    plt.figure(figsize=(2.0, 2.0))
    plt.xlim(0, max_dataarraysize)
    plt.ylim(min_alldata, max_alldata)
    plt.plot(data_array_zero.T[0], linewidth = 0.5)
    plt.plot(data_array_zero.T[1], linewidth = 0.5)

    plt.savefig(datadir + '/marshmallow_imgs/' + str(imgindex) + extension)
    plt.clf()
    plt.close()
    imgindex += 1

print("imgindex")
print(imgindex)
imgindex = 0

print("aaa")

print(np.shape(dataarrays) )
