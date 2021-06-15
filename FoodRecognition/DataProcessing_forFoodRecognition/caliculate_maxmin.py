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

max_dataarray_one = -np.inf
max_dataarray_seccound = -np.inf
min_dataarray_one = np.inf
min_dataarray_seccound = np.inf

max_alldata = -np.inf
min_alldata = np.inf

max_dataarraysize = 2000

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
  #dataarray_one = data_deleted[0] - data_deleted[0][0] #tare processing
  #dataarray_secound = data_deleted[1] - data_deleted[1][0] #tare processing

  #for i in range(dataarray_one.size, max_dataarraysize):
  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 10):

    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    ax_dataarray_one = np.max(data_array_zero[0])
    max_dataarray_seccound = np.max(data_array_zero[1])
    min_dataarray_one = np.min(data_array_zero[0])
    min_dataarray_seccound = np.min(data_array_zero[1])

    max_alldata = max(max_dataarray_one, max_dataarray_seccound, max_alldata)
    min_alldata = min(min_dataarray_one, min_dataarray_seccound, min_alldata)

  print(max_alldata)
  print(min_alldata)

print("aaa")


for csvname in list_csvs(datadir + '/cucumberoutside_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 10):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    ax_dataarray_one = np.max(data_array_zero[0])
    max_dataarray_seccound = np.max(data_array_zero[1])
    min_dataarray_one = np.min(data_array_zero[0])
    min_dataarray_seccound = np.min(data_array_zero[1])

    max_alldata = max(max_dataarray_one, max_dataarray_seccound, max_alldata)
    min_alldata = min(min_dataarray_one, min_dataarray_seccound, min_alldata)

  print(max_alldata)
  print(min_alldata)

print("bbb")


for csvname in list_csvs(datadir + '/eggplant_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 10):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    ax_dataarray_one = np.max(data_array_zero[0])
    max_dataarray_seccound = np.max(data_array_zero[1])
    min_dataarray_one = np.min(data_array_zero[0])
    min_dataarray_seccound = np.min(data_array_zero[1])

    max_alldata = max(max_dataarray_one, max_dataarray_seccound, max_alldata)
    min_alldata = min(min_dataarray_one, min_dataarray_seccound, min_alldata)

  print(max_alldata)
  print(min_alldata)

print("ccc")

for csvname in list_csvs(datadir + '/konnyaku_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 10):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    ax_dataarray_one = np.max(data_array_zero[0])
    max_dataarray_seccound = np.max(data_array_zero[1])
    min_dataarray_one = np.min(data_array_zero[0])
    min_dataarray_seccound = np.min(data_array_zero[1])

    max_alldata = max(max_dataarray_one, max_dataarray_seccound, max_alldata)
    min_alldata = min(min_dataarray_one, min_dataarray_seccound, min_alldata)

  print(max_alldata)
  print(min_alldata)

print("ddd")

for csvname in list_csvs(datadir + '/gumi_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 10):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    ax_dataarray_one = np.max(data_array_zero[0])
    max_dataarray_seccound = np.max(data_array_zero[1])
    min_dataarray_one = np.min(data_array_zero[0])
    min_dataarray_seccound = np.min(data_array_zero[1])

    max_alldata = max(max_dataarray_one, max_dataarray_seccound, max_alldata)
    min_alldata = min(min_dataarray_one, min_dataarray_seccound, min_alldata)
  print(max_alldata)
  print(min_alldata)

print("eee")

for csvname in list_csvs(datadir + '/kamaboko_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 10):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    ax_dataarray_one = np.max(data_array_zero[0])
    max_dataarray_seccound = np.max(data_array_zero[1])
    min_dataarray_one = np.min(data_array_zero[0])
    min_dataarray_seccound = np.min(data_array_zero[1])

    max_alldata = max(max_dataarray_one, max_dataarray_seccound, max_alldata)
    min_alldata = min(min_dataarray_one, min_dataarray_seccound, min_alldata)
  print(max_alldata)
  print(min_alldata)

print("fff")

for csvname in list_csvs(datadir + '/marshmallow_csv/'):
  csvdata = pd.read_csv(csvname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
  data_delbefore = np.array(csvdata, dtype = np.float32).T
  data_deleted = np.delete(data_delbefore, 0, axis = 0) #delete meaningless law
  data_array = data_deleted - data_deleted.mean(axis=0)
  print(data_array.T.shape)

  for i in range(0, int(max_dataarraysize - data_array.shape[1]), 10):
    data_array_zero = np.zeros((max_dataarraysize, 2))
    data_array_zero[:data_array.shape[1], :] = data_array.T
    ax_dataarray_one = np.max(data_array_zero[0])
    max_dataarray_seccound = np.max(data_array_zero[1])
    min_dataarray_one = np.min(data_array_zero[0])
    min_dataarray_seccound = np.min(data_array_zero[1])

    max_alldata = max(max_dataarray_one, max_dataarray_seccound, max_alldata)
    min_alldata = min(min_dataarray_one, min_dataarray_seccound, min_alldata)

print("aaaaaa")
print(max_alldata)
print(min_alldata)
