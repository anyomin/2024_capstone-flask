from flask import Blueprint, jsonify
import pymysql

def show_look():
    # 데이터베이스 연결
    con = pymysql.connect(host='localhost', user='root', password='apmsetup', db='closetapp', charset='utf8',
                            autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    
    # 블루프린트 생성
    showlook_blueprint = Blueprint('lookbook', __name__)
    
    # 룩북 정보를 클라이언트에게 전송하는 엔드포인트
    @showlook_blueprint.route('/show', methods=['GET'])
    def show_closet_route():
        try:
            # 룩북 정보를 데이터베이스에서 가져옴
            with con.cursor() as cursor:
                sql = "SELECT top, bottom, shoes, bag, lookname FROM lookbook"
                cursor.execute(sql)
                lookbook_data = cursor.fetchall()
                
            if lookbook_data:
                lookbooks = []
                for item in lookbook_data:
                    lookbook = {}
                    # 룩북 항목들의 정보를 저장
                    lookbook['lookname'] = item['lookname']
                    lookbook['상의'] = item['top']
                    lookbook['하의'] = item['bottom']
                    lookbook['신발'] = item['shoes']
                    lookbook['가방'] = item['bag']
                    lookbooks.append(lookbook)
                
                return jsonify({'lookbooks': lookbooks}), 200
            else:
                return jsonify({'error': 'Lookbook not found'}), 404
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return showlook_blueprint