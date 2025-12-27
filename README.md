# 👚 딥러닝 기반 의류 관리 & 코디 추천 앱 (Flask API 서버)

## 1) 프로젝트 한줄 소개
> Flutter 앱과 통신하는 Flask REST API를 구현하고, MySQL에 옷장/룩북 데이터를 저장·조회하며 이미지 업로드 시 배경제거/카테고리 분류 결과를 JSON(Base64 이미지 포함)으로 반환하는 서비스

---

## 2) 핵심 기능 스크린샷 & 데모 영상

### 🎥 데모 영상
[![Demo Video](https://img.youtube.com/vi/gGcU2lqVKR4/0.jpg)](https://youtu.be/gGcU2lqVKR4)

### 🖼️ 주요 화면
<table>
  <tr>
    <th>옷장</th>
    <th>룩북</th>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/023249a8-8f6d-44db-b715-ff9d6d83eea2" width="430"/></td>
    <td><img src="https://github.com/user-attachments/assets/595e36c6-bbbf-430f-b991-2debbd336506" width="430"/></td>
  </tr>
</table>

<table>
  <tr>
    <th>날씨 기반 코디 추천</th>
    <th>체형 분석</th>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/b0b2abc5-7456-4078-a6ea-481de94c469e" width="430"/></td>
    <td><img src="https://github.com/user-attachments/assets/a72aa0d4-6320-44aa-99f7-28b0bbab2196" width="430"/></td>
  </tr>
</table>

---

## 3) DB ERD/테이블 요약

### closet (의류)
- `num` (PK, auto_increment): 의류 고유번호
- `category`: 의류 카테고리
- `memo`: 메모
- `image`: 이미지 파일 경로

### lookbook (코디)
- `looknum` (PK, auto_increment): 코디 고유번호
- `top`, `bottom`, `shoes`, `bag`: 코디에 사용된 의류 번호(closet.num 참조)
- `lookname`: 코디 이름
