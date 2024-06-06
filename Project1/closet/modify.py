from flask import jsonify, request
import pymysql

# MySQL 연결
con = pymysql.connect(host='localhost', user='root', password='apmsetup', db='closetapp', charset='utf8',
                            autocommit=True, cursorclass=pymysql.cursors.DictCursor)
def modify_closet():
    try:
        # 클라이언트가 보낸 JSON 데이터 가져오기
        request_data = request.json
        
        # JSON 데이터에서 필요한 정보 추출
        num = request_data['num']
        category = request_data['category']
        memo = request_data['memo']
        
        # 데이터베이스에서 해당 옷 정보 업데이트
        with con.cursor() as cursor:
            sql = "UPDATE closet SET category = %s, memo = %s WHERE num = %s"
            cursor.execute(sql, (category, memo, num))
            con.commit()
        
        # 성공 메시지 반환
        return jsonify({"success": True}), 200
    except Exception as e:
        # 예외 발생 시 오류 메시지 반환
        return jsonify({"success": False, "error": str(e)}), 400