import json
import pymysql
import re
import os
import base64
import random  # 추가된 부분
from flask import Flask, jsonify, redirect, render_template, request

Closet_FOLDER = 'closet'
AFTER_REMOVEBG_FOLDER = os.path.join(Closet_FOLDER, 'After_Removebg')

con = pymysql.connect(host='localhost', user='root', password='apmsetup', db='closetapp', charset='utf8',
                      autocommit=True, cursorclass=pymysql.cursors.DictCursor)

def get_random_image_by_category(category):
    cursor = con.cursor()

    # 카테고리에 해당하는 이미지 검색
    cursor.execute("SELECT image FROM closet WHERE category = %s", (category,))

    # 결과 가져오기
    data = cursor.fetchall()

    # 해당 카테고리의 이미지 수를 가져옴
    num_images = len(data)
    
    # 무작위로 하나의 이미지 선택
    random_index = random.randint(0, num_images - 1)
    random_image = data[random_index]

    file_name = re.search(r'[\\/]([^\\/]+)$', random_image['image']).group(1)
    removed_image_path = os.path.join(AFTER_REMOVEBG_FOLDER, file_name)

    # 선택된 이미지가 존재하는지 확인하고 이미지를 base64로 인코딩하여 반환
    if os.path.exists(removed_image_path):
        with open(removed_image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            image_data = {'image': encoded_string}
            return jsonify(image_data)
    else:
        return jsonify({'message': 'Image not found for the category'})
