# coding:utf-8
import keras
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.preprocessing.image import array_to_img, img_to_array, list_pictures, load_img
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def main():

    imgwide = 640
    imghigh = 480
    imgdata_dir = "/Users/sota/Labratory_Local/FoodRecognition/data/imgs"#in local enviolenment, so must change

    imgs = []
    label = []

    for picture in list_pictures(imgdata_dir + '/cucumberinside_imgs/'):
        img = img_to_array(load_img(picture, target_size=(imgedge,imghigh), grayscale=True))
        imgs.append(img)
        label.append(0)

    for picture in list_pictures(imgdata_dir + '/cucumberoutside_imgs/'):
        img = img_to_array(load_img(picture, target_size=(imgedge,imghigh), grayscale=True))
        imgs.append(img)
        label.append(1)

    for picture in list_pictures(imgdata_dir + '/eggplant_imgs/'):
        img = img_to_array(load_img(picture, target_size=(imgedge,imghigh), grayscale=True))
        imgs.append(img)
        label.append(2)

    for picture in list_pictures(imgdata_dir + '/gumi_imgs/'):
        img = img_to_array(load_img(picture, target_size=(imgedge,imghigh), grayscale=True))
        imgs.append(img)
        label.append(3)

    for picture in list_pictures(imgdata_dir + '/kamaboko_imgs/'):
        img = img_to_array(load_img(picture, target_size=(imgedge,imghigh), grayscale=True))
        imgs.append(img)
        label.append(4)

    for picture in list_pictures(imgdata_dir + '/konnyaku_imgs/'):
        img = img_to_array(load_img(picture, target_size=(imgedge,imghigh), grayscale=True))
        imgs.append(img)
        label.append(5)

    for picture in list_pictures(imgdata_dir + '/marshmallow_imgs/'):
        img = img_to_array(load_img(picture, target_size=(imgedge,imghigh), grayscale=True))
        imgs.append(img)
        label.append(6)



    imgs = np.asarray(imgs)
    imgs = imgs.astype('float32')
    imgs = imgs / 255.0

    label = np.asarray(label)

    # generate train and test data automatically, using scikit-learn
    # how diside random state size???
    img_train, img_test, label_train, label_test = train_test_split(imgs, label, test_size=0.25, random_state=111)


    # CNNを構築
    model = keras.Sequential([
    keras.layers.Flatten(input_shape=(imgwide, imghigh)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(7, activation='softmax')
    ])

    model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

    # 実行。出力はなしで設定(verbose=0)。
    history = model.fit(img_train, label_train, batch_size=5, epochs=200,
                       validation_data = (img_test, label_test), verbose = 0)
