#when measured in one time, generate one csv file
import serial
import time
import csv
import sys
import os
import numpy as np
from datetime import datetime

def passiveserial(writtenby, maxylim, maxarraysize):
    #what criteria to csvfile written. you can switch thesis
    ways_writtenby = {'0' : 'passtime', '1' : 'masuretimes', '2' : 'anytiming', '3' : 'continuously'}
    writtenby = writtenby


    maxylim = maxylim
    maxarraysize = maxarraysize
    SAMPLE_RATE = 1000

    ser = serial.Serial()
    ser.baudrate = 57600
    ser.port = '/dev/tty.SLAB_USBtoUART'
    ser.open()

    firstlever = []
    secoundlever = []
    thirdlever = []

    ifiterate = False
    ifwrite = False

    j = 0 #which cantilever getten
    times = 0
    starttime = time.time()
    while(True):
       try:
           line = ser.readline().decode()
           print(line)

           if "\r\n" in line:
               line = line.replace("\r\n", "")

           else:
               continue

           if j == 0:
               firstlever.append(line)
               j += 1

           elif j == 1:
               secoundlever.append(line)
               j += 1

           else:
               thirdlever.append(line)
               j = 0
               times += 1


           if (j == 0) and ( writtenby == ways_writtenby['0'] ): #passtime
               now = time.time()
               passtime = 3

               if now - starttime > passtime:

                   starttime = time.time()
                   if ifwrite == True:
                        writecsv(firstlever, secoundlever, thirdlever)
                        ifwrite = False
                        print("write")

                   else:
                       ifwrite = True
                       print("not write")

                   firstlever = []
                   secoundlever = []
                   thirdlever = []

           if writtenby == ways_writtenby['1']: #masuretimes:
               samplingrate = 1000 #refer arduino
               secounds = 10 #anytime

               if times == samplingrate * secounds:
                   writecsv(firstlever, secoundlever, thirdlever)
                   times = 0

           # if writtenby == ways_writtenby['2']: #anytiming:
           #     hotkey = hogehoge

           # if writtenby == ways_writtenby['3']:#continuously
           #

           # time.sleep(0.1)#CPU利用率を抑える．ただシリアルが送られてくるタイミングとの同期がどうなってんのかわからん

       except KeyboardInterrupt:
           ser.close()
           break


def writecsv(firstlever, secoundlever, thirdlever):
    datadir = '/Users/sota/Labratory_Local/TactileSensor/data/'
    category = 'testtest20210614'
    category = datadir + category
    os.makedirs(category +'/csvs', exist_ok = True)
    datetime_now = datetime.now()

    print(firstlever)
    print(secoundlever)
    print(thirdlever)
    firstlever = list( map(int, firstlever) )
    secoundlever = list( map(int, secoundlever) )
    thirdlever = list( map(int, thirdlever) )

    identifier = 'test20210614'
    csvname = category + '/csvs/' + identifier + '_' + datetime_now.strftime('%Y_%m_%d_%H_%M_%S')

    with open(csvname + '.csv', 'w') as file:
        writer = csv.writer(file)

        firstleverarray = np.array(firstlever)
        secoundleverarray = np.array(secoundlever)
        thirdleverarray = np.array(thirdlever)

        #tare processing
        firstleverarray = firstleverarray - firstleverarray[0]
        secoundleverarray = secoundleverarray - secoundleverarray[0]
        thirdleverarray = thirdleverarray - thirdleverarray[0]

        writer.writerow(firstleverarray)
        writer.writerow(secoundleverarray)
        writer.writerow(thirdleverarray)



def main():
    writtenby = 'passtime'
    maxylim = 1500
    maxarraysize = 1000

    #処理開始直後は変な値がシリアルで送り付けられてくる？
    time.sleep(5)

    while(True):
        passiveserial(writtenby, maxylim, maxarraysize)

if __name__ == "__main__":
    main()
