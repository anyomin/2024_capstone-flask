

<div align=center>
<h3>의류 관리&추천 애플리케이션(서버) <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Grinning%20Squinting%20Face.png" alt="Grinning Squinting Face" width="25" height="25" />
</h3>

📚 Languages / Library / Tools 📚
  
![js](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=white)
![js](https://img.shields.io/badge/HTML-E34F26?style=flat&logo=html5&logoColor=white)
![js](https://img.shields.io/badge/CSS-239120?&style=flat&logo=css3&logoColor=white)
![js](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)



![js](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=flat&logo=visual%20studio%20code&logoColor=white)

<h3>기술스택</h3>
<img width="1778" height="810" alt="image" src="https://github.com/user-attachments/assets/f6c15f54-8ca8-4537-af07-ac564e7d38a3" />
<h3>전체 시스템 구성도</h3>
<img width="1134" height="446" alt="image" src="https://github.com/user-attachments/assets/af07221b-33fc-4e32-82a0-7e3b2bda41b4" />

# 👚 딥러닝 기반 의류 관리 & 코디 추천 앱 (Server/API)

> 사용자의 의류를 등록·분류하고, 룩북/날씨/체형 기반 코디 추천을 제공하는 모바일 서비스의 **Flask API 서버**

---

## ✅ 핵심 기능 (요약)
- **의류 등록**: 이미지 업로드 → 배경제거 → 카테고리 분류 → DB 저장
- **옷장 조회/관리**: 카테고리별 목록 조회, 메모 조회/수정/삭제
- **룩북**: 코디(상의/하의/신발/가방) 조합 저장 및 조회
- **날씨 기반 추천**: OpenWeather 연동(앱/서버 흐름 기반)
- **체형 분석(연동)**: 이미지 업로드 후 bodytype 결과 반환

---

## 🧩 Tech Stack
- **Backend**: Python, Flask (REST API)
- **DB**: MySQL
- **ML 연동**: TensorFlow/Keras (분류/추론 모듈 호출)
- **Image 처리**: 배경제거 처리 모듈 연동
- **Dev/Etc**: Git, VS Code, ngrok(연동 테스트), CORS

---

## 🗺️ 시스템 구성도
![architecture](docs/images/architecture.png)

> **앱(Flutter)** ↔ **Flask API 서버** ↔ **MySQL**  
> (필요 시 **ngrok**로 로컬 서버를 외부 URL로 열어서 앱-서버 연동 테스트)

---

## 🖼️ 스크린샷
| 옷장 | 룩북 |
|---|---|
| ![closet](docs/images/screen_closet.png) | ![lookbook](docs/images/screen_lookbook.png) |

| 날씨 추천 | 체형 분석 |
|---|---|
| ![weather](docs/images/screen_weather.png) | ![body](docs/images/screen_bodytype.png) |

---

## 🔌 API (주요 엔드포인트)
> 앱 ↔ 서버는 **HTTP 요청/응답(JSON)** 기반으로 통신합니다.

| Method | Endpoint | 설명 |
|---|---|---|
| GET | `/closet` | 의류 전체 목록 조회 |
| GET | `/closet/<category>` | 카테고리별 의류 목록 조회 |
| POST | `/closet/upload` | 이미지 업로드 → 배경제거/분류 → Base64 이미지+category 반환 |
| POST | `/closet/dbsave` | 카테고리/메모/이미지 경로 DB 저장 |
| GET/POST | `/closet/giveinfo` | 의류 memo 상세 조회 |
| POST | `/closet/modify` | 의류 정보 수정 |
| POST | `/closet/delete` | 의류 정보 삭제 |
| POST | `/lookbook/add` | 룩북(코디) 추가 |
| GET | `/weather/<category>` | 날씨/카테고리 기반 추천 |
| POST | `/bodyupload` | 체형 분석용 이미지 업로드 → 결과 반환 |

### 예시 응답 (업로드)
```json
{
  "message": "File uploaded successfully",
  "image": "base64_encoded_string...",
  "category": "hoodie"
}


