import serial
import time
import csv
import sys
import os
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

times = np.zeros(100)
maxylim= 200
ser = serial.Serial()
ser.baudrate = 112500
ser.port = '/dev/tty.usbmodem141101'
ser.open()

j = 0
t = 0
maxarraysize = 1000
SAMPLE_RATE = 1000

firstlever = np.zeros(maxarraysize + 1)
secoundlever = np.zeros(maxarraysize + 1)
thirdlever = np.zeros(maxarraysize + 1)
xaxis = [i for i in range(0, maxarraysize + 1)]

category = '/Users/sota/Labratory_Local/TactileSensor/' +  sys.argv[1]
os.makedirs(category +'/imgs', exist_ok = True)
os.makedirs(category +'/csvs', exist_ok = True)

imgname = category + '/imgs/' + str( (len(os.listdir(category + '/imgs')) + 1) )
csvname = category + '/csvs/' + str( (len(os.listdir(category + '/csvs')) + 1) )

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
    gstop = 40                      # 阻止域最小減衰量[dB]
    # 正規化
    Wp = fp/fn
    Ws = fs/fn

    # ローパスフィルタで波形整形
    # バターワースフィルタ
    N, Wn = signal.buttord(Wp, Ws, gpass, gstop)
    b1, a1 = signal.butter(N, Wn, "low")

    data = signal.filtfilt(b1, a1, data)

    return data


while(True):
   try:
       line = float(ser.readline().decode())
#       print(line)
       if j == 0:
           firstlever[t] = line
           j += 1
        
       elif j == 1:
           secoundlever[t] = line
           j += 1
        
       else:
           thirdlever[t] = line
           j = 0     
           t += 1

       if t == maxarraysize:
           print("aaa")
           with open(csvname + '.csv', 'w') as file:
               writer = csv.writer(file)
               firstlever = firstlever - firstlever[0]
               secoundlever = secoundlever - secoundlever[0]
               thirdlever = thirdlever - thirdlever[0]

               firstlever = lowpass(firstlever, SAMPLE_RATE)
               secoundlever = lowpass(secoundlever, SAMPLE_RATE)
               thirdlever = lowpass(thirdlever, SAMPLE_RATE)
               writer.writerow(firstlever)
               writer.writerow(secoundlever)
               writer.writerow(thirdlever)

               plt.ylim(-maxylim, maxylim)
               plt.plot(xaxis, firstlever)
               plt.plot(xaxis, secoundlever)
               plt.plot(xaxis, thirdlever)

               plt.savefig(imgname + '.png')

               ser.close()
               print("end")
               exit()
       print('times : ' + str(t))
   except KeyboardInterrupt:
       ser.close()
       break

   
