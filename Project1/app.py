import json
import pymysql
from flask import Flask
from http import HTTPStatus
from flask_cors import CORS
from closet.rem_bg import removebg
from flask import Flask, jsonify, redirect, render_template, request, url_for,send_file,Blueprint
import os
import base64
import json
from flask import make_response
from closet.category import get_category_list
from closet.closetdbsave import save_to_database
from closet.modify import modify_closet
from closet.delete import delete_closet
from lookbook.addlook import add_look
from lookbook.showlook import show_look
from lookbook.getimage import get_image
from model import classify_image
from closet.weather import get_random_image_by_category
from bodytype import inference

app = Flask(__name__)

#ngrok로 웹페이지 실행시 visit site라는 페이지가 안뜨게 함
CORS(app)



# --closet 옷장기능 -----

# 데이터베이스에 연결
con = pymysql.connect(host='localhost', user='root', password='apmsetup', db='closetapp', charset='utf8',
                            autocommit=True, cursorclass=pymysql.cursors.DictCursor)
@app.route('/closet')
def get_user_list():
    cursor = con.cursor()

    # User Info : followers, followings, last updated time
    cursor.execute("SELECT * FROM closet")
    
    data = json.dumps(cursor.fetchall(),ensure_ascii=False)
    
    res = make_response(data)
    return res

#앱에서 카테고리 선택시 해당 카테고리에 속하는 옷 이미지 전달
@app.route('/closet/<category>')
def category_list(category):
    return get_category_list(category)


Closet_FOLDER = 'closet'
UPLOAD_FOLDER = os.path.join(Closet_FOLDER, 'Before_Removebg')
AFTER_REMOVEBG_FOLDER =os.path.join(Closet_FOLDER, 'After_Removebg')

# #앱(배경제거x)->서버(배경제거o)->앱(배경제거o)
# class ImageRouters:
#     @staticmethod
#     def get_blueprint():
#         api_blueprint = Blueprint('closet', __name__)
        
#         @api_blueprint.route('/upload', methods=['POST'])
#         def get_image():
#             file = request.files['image']
    
#             if file:
#                 filename = file.filename
#                 filepath = os.path.join(UPLOAD_FOLDER, filename)
#                 file_name= os.path.join(AFTER_REMOVEBG_FOLDER, filename)
#                 file_sql='closet'+'\\'+'After_Removebg'+'\\'+f"{os.path.splitext(filename)[0]}.png"
#                 with con.cursor() as cursor:
#                     # 이미지가 이미 데이터베이스에 존재하는지 확인하는 쿼리
#                     sql = "SELECT * FROM closet WHERE image = %s"
#                     cursor.execute(sql, (file_sql,))
#                     result = cursor.fetchone()
            
#             # 이미지가 데이터베이스에 존재하면 오류 반환
#                     if result:
#                         print("file_sql:", file_sql)
#                         return jsonify({'error': 'Image already exists in the database'}), 400
            
#                 file.save(filepath)
#                 removebg(filepath)
#                 removed_image_path = os.path.join(AFTER_REMOVEBG_FOLDER, os.path.splitext(filename)[0] + '.png')
#             return send_file(removed_image_path, mimetype='image/png')
        
#         return api_blueprint
# app.register_blueprint(ImageRouters.get_blueprint(), url_prefix='/closet')  


@app.route('/closet/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    
    if file:
        filename = file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file_name= os.path.join(AFTER_REMOVEBG_FOLDER, filename)
        file_sql='closet'+'\\'+'After_Removebg'+'\\'+f"{os.path.splitext(filename)[0]}.png"
        
        with con.cursor() as cursor:
            # 이미지가 이미 데이터베이스에 존재하는지 확인하는 쿼리
            sql = "SELECT * FROM closet WHERE image = %s"
            cursor.execute(sql, (file_sql,))
            cursor.execute(sql, (file_sql,))
            result = cursor.fetchone()
            
            # 이미지가 데이터베이스에 존재하면 오류 반환
            if result:
                
                print("file_sql:", file_sql)
                return jsonify({'error': 'Image already exists in the database'}), 400
            
            
        file.save(filepath)
        removebg(filepath)
        predicted_category = classify_image(filepath)
       # 배경 제거된 이미지 파일 경로
        removed_image_path = os.path.join(AFTER_REMOVEBG_FOLDER, os.path.splitext(filename)[0] + '.png')
        # 파일이 존재하는지 확인하고 이미지를 base64로 인코딩하여 반환
        if os.path.exists(removed_image_path):
            with open(removed_image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return jsonify({'message': 'File uploaded successfully', 'filename': removed_image_path, 'image': encoded_string,'category': predicted_category})
        else:
            return jsonify({'error': 'Failed to remove background'})
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})
    
    # 오류처리
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    




#앱에서 배경제거된 사진을 받고 카테고리, 메모를 입력 후 db에 저장 +이미지경로
@app.route('/closet/dbsave', methods=['POST'])
def upload_to_database():
    request_data = request.json
    return save_to_database(request_data)


#앱에서 옷 클릭하면 옷의 상세정보창 띄움
@app.route('/closet/giveinfo', methods=['GET', 'POST'])
def closet_info():
    try:
        if request.method == 'POST':
            request_data = request.json
            num = request_data.get('num')
            if not num:
                return jsonify({'error': 'No number provided in the request'}), 400
        elif request.method == 'GET':
            num = request.args.get('num')
            if not num:
                return jsonify({'error': 'No number provided in the request'}), 400
        else:
            return jsonify({'error': 'Unsupported request method'}), 405

        cursor = con.cursor()
        sql = "SELECT memo FROM closet WHERE num = %s"
        cursor.execute(sql, (num,))
        memo = cursor.fetchmany()

        if memo:
            return jsonify({'memo': memo}), 200
        else:
            return jsonify({'error': 'No memo found for the given number'}), 404
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

#옷 상세정보창에서 옷 정보 수정
@app.route('/closet/modify', methods=['POST'])
def modify_closet_route():
    return modify_closet()


#옷 상세정보창에서 옷 정보 삭제
@app.route('/closet/delete', methods=['POST'])
def delete_closet_route():
    return delete_closet()

#-------------------------------
# --lookbook 룩북기능 -----
#룩북 추가
@app.route('/lookbook/add', methods=['POST'])
def add_closet_route():
    return add_look()

app.register_blueprint(show_look(), url_prefix='/lookbook')

@app.route('/lookbook/show/get_image/<num>', methods=['GET'])
def get_image_route(num):
    return get_image(num)



@app.route('/weather/<category>', methods=['GET'])
def get_random_image(category):
    return get_random_image_by_category(category)
#체형진단
@app.route('/bodyupload', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image provided'}), 400
    
    file_path = os.path.join('closet/Body_type', file.filename)
    file.save(file_path)

    try:
        result = inference(file_path)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({'body_shape': result})
#-------
if __name__ == '__main__':
    app.run(debug=True)