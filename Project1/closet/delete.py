from flask import jsonify, request
import pymysql

# MySQL 연결
con = pymysql.connect(host='localhost', user='root', password='apmsetup', db='closetapp', charset='utf8',
                            autocommit=True, cursorclass=pymysql.cursors.DictCursor)
def delete_closet():
    try:
        # 클라이언트가 보낸 JSON 데이터 가져오기
        request_data = request.json
        
        # JSON 데이터에서 필요한 정보 추출
        num = request_data['num']
        
        # 데이터베이스에서 해당 옷 정보 삭제
        with con.cursor() as cursor:
            sql = "DELETE FROM closet WHERE num = %s"
            cursor.execute(sql, (num,))
            con.commit()
        
        # 성공 메시지 반환
        return jsonify({"success": True}), 200
    except Exception as e:
        # 예외 발생 시 오류 메시지 반환
        return jsonify({"success": False, "error": str(e)}), 400