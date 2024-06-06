from flask import request, jsonify
import os
import base64
from rem_bg import removebg  # assuming removebg function is in remove_background module
import pymysql


UPLOAD_FOLDER = 'Before_Removebg'
AFTER_REMOVEBG_FOLDER = 'After_Removebg'



def upload_file(con):
    file = request.files['image']
    
    if file:
        filename = file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file_name= os.path.join(AFTER_REMOVEBG_FOLDER, filename)
        with con.cursor() as cursor:
            # 이미지가 이미 데이터베이스에 존재하는지 확인하는 쿼리
            sql = "SELECT * FROM closet WHERE image = %s"
            cursor.execute(sql, (file_name,))
            result = cursor.fetchone()
            
            # 이미지가 데이터베이스에 존재하면 오류 반환
            if result:
                return jsonify({'error': 'Image already exists in the database'}), 400

        
        file.save(filepath)
        removebg(filepath)
       # 배경 제거된 이미지 파일 경로
        removed_image_path = os.path.join(AFTER_REMOVEBG_FOLDER, os.path.splitext(filename)[0] + '.png')
        # 파일이 존재하는지 확인하고 이미지를 base64로 인코딩하여 반환
        if os.path.exists(removed_image_path):
            with open(removed_image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return jsonify({'message': 'File uploaded successfully', 'filename': removed_image_path, 'image': encoded_string})
        else:
            return jsonify({'error': 'Failed to remove background'})
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})
    
    # 오류처리
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    if file.filename == '':
        return jsonify({'error': 'No selected file'})