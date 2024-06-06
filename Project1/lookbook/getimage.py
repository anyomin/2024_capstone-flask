from flask import Flask, request, send_file, jsonify
import pymysql



def get_image(num):
    
    # 데이터베이스 연결
    con = pymysql.connect(host='localhost', user='root', password='apmsetup', db='closetapp', charset='utf8',
                          autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with con.cursor() as cursor:
            # num을 이용해서 데이터베이스에서 이미지 파일 경로를 가져옴
            sql = "SELECT image FROM closet WHERE num = %s"
            cursor.execute(sql, (num,))
            result = cursor.fetchone()
            
            if result:
                image_path = result['image']
                
                return send_file(image_path, mimetype='image/png')  # 이미지 파일 전송
            else:
                return jsonify({'error': 'Image not found for the given num'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        con.close()  # 데이터베이스 연결 닫기


