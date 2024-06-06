from flask import request, jsonify
import base64
import pymysql
import os
# 데이터베이스에 연결
con = pymysql.connect(host='localhost', user='root', password='apmsetup', db='closetapp', charset='utf8',
                            autocommit=True, cursorclass=pymysql.cursors.DictCursor)
def add_look():
    try:
         # 클라이언트가 보낸 JSON 데이터 가져오기
        request_data = request.json
        print(request_data)
        
        # JSON 데이터에서 필요한 정보 추출
        items = request_data.get('items')
        lookname = None
        top = bottom = shoes = bag = None
        for item in items:
            category = list(item.keys())[0]  # 카테고리 추출
            num = item.get(category)  # 번호 추출
            if category == '상의':
                top = num
            elif category == '하의':
                bottom = num
            elif category == '신발':
                shoes = num
            elif category == '가방':
                bag = num
            elif category == 'lookname':
                lookname = num
        # lookbook 테이블에 데이터 추가
        with con.cursor() as cursor:
            sql = "INSERT INTO lookbook (top, bottom, shoes, bag, lookname) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (top, bottom, shoes, bag, lookname))
            con.commit()

        # closet 테이블에서 이미지들을 가져와 인코딩하여 앱에 반환
    

        return jsonify({"success": True}), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400
