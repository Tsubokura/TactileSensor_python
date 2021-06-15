import csv
import time
import numpy as np
import os
import re
import sys
import datetime
import glob
from scipy import signal
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
from pandas.tseries.offsets import DateOffset
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
from matplotlib.dates import date2num

def load_file_NIMAX(fname):
    csv = pd.read_csv(fname, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
    data = np.array(csv, dtype = np.float32).T

    def0 = data[0][0]
    def1 = data[1][0]
    def2 = data[2][0]

    for index, item in enumerate(data[0]):
        #最初の値を引くとき
        data[0][index] = data[0][index] - def0
        data[1][index] = data[1][index] - def1
        data[2][index] = data[2][index] - def2

    return np.array(data, dtype = np.float32)

def load_file_acc(fname):
    csv = pd.read_csv(fname, sep = ',', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])
#    with codecs.open("fname", "r", "Shift-JIS", "ignore") as file:
#        csv = pd.read_table(file, delimiter=",")
        #date = np.array(csv.iloc[:,:1], dtype = np.datetime64).T
        #data = np.array(csv.iloc[:,2:4], dtype = np.float32).T
    temp = csv.values.T
    date = temp[0][:]
    data = temp[1:][:]
    #print(type(test))
    def0 = data[0][0]
    def1 = data[1][0]
    def2 = data[2][0]

    for index, item in enumerate(data[0]):
        #最初の値を引くとき
        data[0][index] = data[0][index] - def0
        data[1][index] = data[1][index] - def1
        data[2][index] = data[2][index] - def2

    return date, data

# ローパスフィルタ処理
def lowpass(data, SAMPLE_RATE):
    # 時系列のサンプルデータ作成
    # n = len(data[0])              # データ数
    dt = 1/SAMPLE_RATE              # サンプリング間隔
    fn = 1/(2*dt)                   # ナイキスト周波数
    # t = np.linspace(1, n, n)*dt-dt

    # パラメータ設定
    fp = 10                         # 通過域端周波数[Hz]
    fs = 50                         # 阻止域端周波数[Hz]
    gpass = 1                       # 通過域最大損失量[dB]
    gstop = 40                      # 阻止域最小減衰量[dB]
    # 正規化
    Wp = fp/fn
    Ws = fs/fn

    # ローパスフィルタで波形整形
    # バターワースフィルタ
    N, Wn = signal.buttord(Wp, Ws, gpass, gstop)
    b1, a1 = signal.butter(N, Wn, "low")

    data_0_lp = signal.filtfilt(b1, a1, data[0])
    data_1_lp = signal.filtfilt(b1, a1, data[1])
    data_2_lp = signal.filtfilt(b1, a1, data[2])

    return data_0_lp, data_1_lp, data_2_lp

# 微分処理
def differential(data):
    data_roll_0 = np.roll(data[0], 300)
    data_roll_1 = np.roll(data[1], 300)
    data_roll_2 = np.roll(data[2], 300)
    diff_0 = data[0] - data_roll_0
    diff_1 = data[1] - data_roll_1
    diff_2 = data[2] - data_roll_2

    return diff_0, diff_1, diff_2

def main():
    #名前のリストを取得する
    datadir = "/Users/sota/Labratory_Local/FoodRecognition/data/test"
    formalized_csvdatadir = "/Users/sota/Labratory_Local/FoodRecognition/data/formalized_data"
    files = os.listdir(datadir)
    print(files)

    SAMPLE_RATE = 2000 #1秒で取るサンプル数[hz]
    UPDATE_RATE = 20 #秒間のデータ更新間隔[hz]
    index = 0

    for file_name in files:

        with open(datadir +  "/" + file_name, encoding="utf_8", errors='ignore') as f:

            reader = csv.reader(f, delimiter='\t')
            l = [row for row in reader]

        data = load_file_NIMAX(datadir +  "/" + file_name)
        data_lp = np.array(lowpass(data, SAMPLE_RATE), dtype = np.float32) #カンチレバー3軸の値が出てくる

        a = data_lp[1]
        maxid = signal.argrelmax(a, order=6000) # 局所的最大値, 6000はデータ幅
        #print(maxid)
        start_flag = False
        end_flag = False

        #ここで点を２つ計算する ピーク値の10分の1が出たら終わりとする
        for k in maxid[0]:
            #print(k)
            #print(a[k])

            x =a[k]/10
            for t in range(len(a)-k):
                if x > a[k+t]:
                    end_id = k+t
                    #print(k+t)
                    end_flag = True
                    break

        for k in maxid[0]:
            #print(k)
            #print(a[k])
            x =a[k]/10
            for t in range(len(a)):
                if x > a[k-t]:
                    start_id = k-t
                    #print(k-t)
                    start_flag = True
                    break

        # new_filename = splited_file_name[0] + "." + splited_file_name[1] + "." + splited_file_name[2] + ".csv"


        if start_flag and end_flag and not os.path.exists(formalized_csvdatadir + "/" + file_name):
            index +=1
            with open(formalized_csvdatadir + "/" + file_name, 'w',newline="") as wf:
                writer = csv.writer(wf,delimiter='\t')
                print(l)
                for a in range(start_id, end_id):
                    writer.writerow(l[a])


        #print("-" * 20)
        print("index")
        print(index)

if __name__ == '__main__':
    main()
