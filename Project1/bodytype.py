import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import pickle


def resize_img(img_path, img_size=224):    
    img = cv2.imread(img_path) # 행렬 변환

    if(img.shape[1] > img.shape[0]) : # 한 변의 길이를 비교하여 더 긴 변의 길이에 맞게 비율 변환 
        ratio = img_size/img.shape[1]
    else :
        ratio = img_size/img.shape[0]

    img = cv2.resize(img, dsize=(0, 0), fx=ratio, fy=ratio, interpolation=cv2.INTER_LINEAR)

    # 그림 주변에 검은색으로 패딩 처라
    w, h = img.shape[1], img.shape[0]

    dw = (img_size-w)/2 # img_size와 w의 차이
    dh = (img_size-h)/2 # img_size와 h의 차이

    M = np.float32([[1,0,dw], [0,1,dh]])  #(2*3 이차원 행렬)
    img_re = cv2.warpAffine(img, M, (224, 224)) #이동변환  
    img_re = cv2.cvtColor(img_re, cv2.COLOR_BGR2GRAY).reshape(224,224,1) #그레이스케일

    return img_re

def compute_mean(imgs):
    return np.mean(imgs, axis=0)

def mean_img(train_dataset): # mean_img 생성
    train_data = []

    for label, filenames in train_dataset.items():
        for filename in filenames:
            image = resize_img(filename)
            train_data.append(image)
    train_data = np.array(train_data)
    mean_img = compute_mean(train_data)

    with open('mean_img.pickle', 'wb') as f:
        pickle.dump(mean_img, f)
    
    return mean_img

def zero_centering(image):
    sub_mean_img = image.astype('int8') - mean_img.astype('int8')
    return sub_mean_img



def inference(image_filename):
    # 모델 로드
    resnet = tf.keras.models.load_model('C:/Users/user/body_type_deeplearning/Bodyshape/pth/resnet.h5')
    #resnet.summary()
    # 평균 이미지 로드
    mean_img_path = 'mean_image.jpg'
    mean_img = cv2.imread(mean_img_path, cv2.IMREAD_COLOR)
    if mean_img is None:
        raise ValueError(f"평균 이미지를 찾을 수 없거나 잘못된 이미지 경로입니다: {mean_img_path}")
    
    # 입력 이미지 로드
    
    image_example = cv2.imread(image_filename, cv2.IMREAD_COLOR)

    if image_example is None:
        raise ValueError(f"이미지를 찾을 수 없거나 잘못된 이미지 경로입니다: {image_filename}")
    
    new_img = resize_img(image_filename)
    sub_img = new_img - mean_img

    label2index = {
        '원형': 0,
        '모래시계형': 1,
        '일자형': 2,
        '삼각형': 3
    }
    index2label = {v: k for k, v in label2index.items()}

    pred = np.argmax(resnet.predict(np.expand_dims(sub_img, axis=0), verbose=0), axis=-1)[0]
    
    return index2label[pred]

