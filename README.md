# 👚 딥러닝 기반 의류 관리 & 코디 추천 앱

## 1) 프로젝트 한줄 소개
> 사용자의 의류를 등록·분류하고, 룩북/날씨/체형 기반 코디 추천을 제공하는 모바일 서비스

---
## 🧩 Tech Stack
- **Backend**: Python, Flask (REST API)
- **DB**: MySQL
- **ML 연동**: TensorFlow/Keras (분류/추론 모듈 호출)
- **Image 처리**: 배경제거 처리 모듈 연동
- **Dev/Etc**: Git, VS Code, ngrok(연동 테스트), CORS
---

## ✅ 핵심 기능 (요약)
- **의류 등록**: 이미지 업로드 → 배경제거 → 카테고리 분류 → DB 저장
- **옷장 조회/관리**: 카테고리별 목록 조회, 메모 조회/수정/삭제
- **룩북**: 코디(상의/하의/신발/가방) 조합 저장 및 조회
- **날씨 기반 추천**: OpenWeather 연동해서 날씨에 어울리는 룩북 추천
- **체형 분석(연동)**: 이미지 업로드 후 체형 분석하여 체형별 룩북 추천
---
## 🗺️ 시스템 구성도
<img width="1134" height="446" alt="image" src="https://github.com/user-attachments/assets/af07221b-33fc-4e32-82a0-7e3b2bda41b4" />
> **앱(Flutter)** ↔ **Flask API 서버** ↔ **MySQL**  
> (필요 시 **ngrok**로 로컬 서버를 외부 URL로 열어서 앱-서버 연동 테스트)
---

## 2) 데모 영상 & 핵심 기능 스크린샷 
 
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
