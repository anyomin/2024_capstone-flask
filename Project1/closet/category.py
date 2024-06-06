import json
import pymysql
import re
import os
import base64
from flask import Flask, jsonify, redirect, render_template, request

Closet_FOLDER = 'closet'
AFTER_REMOVEBG_FOLDER =os.path.join(Closet_FOLDER, 'After_Removebg')

con = pymysql.connect(host='localhost', user='root', password='apmsetup', db='closetapp', charset='utf8',
                            autocommit=True, cursorclass=pymysql.cursors.DictCursor)

def get_category_list(category):
    cursor = con.cursor()

    # 카테고리에 해당하는 이미지 검색
    cursor.execute("SELECT num, image FROM closet WHERE category = %s", (category,))
    
    # 결과 가져오기
    data = cursor.fetchall()
    
    # 각 이미지를 하나씩 처리하여 인코딩하고 앱에 반환
    images = []
    for item in data:
        file_name = re.search(r'[\\/]([^\\/]+)$', item['image']).group(1)
        removed_image_path = os.path.join(AFTER_REMOVEBG_FOLDER, file_name)
        
        # 파일이 존재하는지 확인하고 이미지를 base64로 인코딩하여 반환
        if os.path.exists(removed_image_path):
            with open(removed_image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                images.append({'num': item['num'], 'filename': file_name, 'image': encoded_string})
    
    # 만약 해당 카테고리에 이미지가 없는 경우 빈 응답을 반환
    if not images:
        return jsonify({'message': 'No images found for the category'})
    
    return jsonify(images)