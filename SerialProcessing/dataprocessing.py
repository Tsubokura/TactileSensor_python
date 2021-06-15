import serial
import time
import csv
import sys
import os
import numpy as np
import pandas as pd
from scipy import signal
from matplotlib import pyplot as plt

#cutoff


#lowpass
def lowpass(data, SAMPLE_RATE):
    # 時系列のサンプルデータ作成
    # n = len(data[0])              # データ数
    dt = 1/SAMPLE_RATE              # サンプリング間隔
    fn = 1/(2*dt)                   # ナイキスト周波数
    # t = np.linspace(1, n, n)*dt-dt

    # パラメータ設定
    fp = 10                         # 通過域端周波数[Hz]
    fs = 100                         # 阻止域端周波数[Hz]
    gpass = 1                       # 通過域最大損失量[dB]
    gstop = 30                      # 阻止域最小減衰量[dB]
    # 正規化
    Wp = fp/fn
    Ws = fs/fn

    # ローパスフィルタで波形整形
    # バターワースフィルタ
    N, Wn = signal.buttord(Wp, Ws, gpass, gstop)
    b1, a1 = signal.butter(N, Wn, "low")

    data = signal.filtfilt(b1, a1, data)

    return data


#csv to png by matplotlib
def generategraph(data):


    os.makedirs(category +'/imgs', exist_ok = True)
    imgname = category + '/imgs/' + str( (len(os.listdir(category + '/imgs')) + 1) )

    firstlever = data[0]
    secoundlever = data[1]
    thirdlever = data[2]

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax1.set_ylim([-maxylim, maxylim])
    ax1.plot(firstlever)
    ax1.plot(secoundlever)
    ax1.plot(thirdlever)

    ax2.set_ylim([-maxylim, maxylim])
    ax2.plot(firstlever)
    ax2.plot(secoundlever)
    ax2.plot(thirdlever)

    plt.savefig(imgname + '.png')


def main():
    csvdir = ''

    csvnames = os.listdir(csvdir)

    for csvname in csvnames:
        csv = pd.read_csv(datadir + "/" + filename, sep = '\t', encoding = "shift-jis", error_bad_lines = False, header = None,skiprows=[0])


    csvname =
