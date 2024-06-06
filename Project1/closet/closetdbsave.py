from flask import jsonify
import pymysql
con = pymysql.connect(host='localhost', user='root', password='apmsetup', db='closetapp', charset='utf8',
                            autocommit=True, cursorclass=pymysql.cursors.DictCursor)

def save_to_database(request_data):
    try:
        # JSON 데이터에서 필요한 정보 추출
        category = request_data['category']
        memo = request_data['memo']
        image = request_data['image']
        
        with con.cursor() as cursor:
            sql = "INSERT INTO closet (category, memo, image) VALUES (%s, %s, %s)"
            cursor.execute(sql, (category, memo, image))
            con.commit()
        # 받은 데이터 서버 터미널에 출력
        print(f"Received data from app: Category: {category}, Memo: {memo}, Image: {image}")    
        # 성공 메시지 반환
        return jsonify({"success": True}), 200
    except Exception as e:
        # 예외 발생 시 오류 메시지 반환
        return jsonify({"success": False, "error": str(e)}), 400