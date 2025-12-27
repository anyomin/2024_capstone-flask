# 👚 딥러닝 기반 의류 관리 & 코디 추천 앱

## < 프로젝트 한줄 소개 >
> 사용자의 의류를 등록·분류하고, 룩북/날씨/체형 기반 코디 추천을 제공하는 모바일 서비스

---

## 📌 목차
- [🧩 Tech Stack](#-tech-stack)
- [✅ 핵심 기능 (요약)](#-핵심-기능-요약)
- [🗺️ 시스템 구성도](#-시스템-구성도)
- [🎥 데모 영상 & 🖼️ 핵심 기능 스크린샷](#-데모-영상--%EF%B8%8F-핵심-기능-스크린샷)
- [🗃️ DB 테이블 요약](#%EF%B8%8F-db-테이블-요약)

---

## 🧩 Tech Stack
- **Backend**: Python, Flask (REST API)
- **DB**: MySQL
- **ML 연동**: TensorFlow / Keras (분류/추론 모듈 호출)
- **Image 처리**: 배경제거 모듈 연동
- **Dev/Etc**: Git, VS Code, ngrok(연동 테스트), CORS

---

## ✅ 핵심 기능 (요약)
- **의류 등록**: 이미지 업로드 → 배경제거 → 카테고리 분류 → DB 저장
- **옷장 조회/관리**: 카테고리별 목록 조회, 메모 조회/수정/삭제
- **룩북**: 코디(상의/하의/신발/가방) 조합 저장 및 조회
- **날씨 기반 추천**: OpenWeather 연동 → 날씨에 맞는 코디 추천
- **체형 분석(연동)**: 이미지 업로드 → 체형 분석 → 체형 기반 코디 추천

---

## 🗺️ 시스템 구성도
<img width="1134" height="446" alt="system" src="https://github.com/user-attachments/assets/af07221b-33fc-4e32-82a0-7e3b2bda41b4" />

> **앱(Flutter)** ↔ **Flask API 서버** ↔ **MySQL**  
> 필요 시 **ngrok**로 로컬 서버를 외부 URL로 열어 **앱-서버 연동 테스트** 진행

---

## 🎥 데모 영상 & 🖼️ 핵심 기능 스크린샷

### 🎥 데모 영상
[![Demo Video](https://img.youtube.com/vi/gGcU2lqVKR4/0.jpg)](https://youtu.be/gGcU2lqVKR4)

### 🖼️ 주요 화면
<!-- ✅ 옆으로 안 가고 밑으로 내려가면: "한 줄에 img 2개" 형태로 쓰는 게 제일 안정적 -->
<p>
  <img src="https://github.com/user-attachments/assets/023249a8-8f6d-44db-b715-ff9d6d83eea2" width="49%"/>
  <img src="https://github.com/user-attachments/assets/595e36c6-bbbf-430f-b991-2debbd336506" width="49%"/>
</p>
<p>
  <img src="https://github.com/user-attachments/assets/b0b2abc5-7456-4078-a6ea-481de94c469e" width="49%"/>
  <img src="https://github.com/user-attachments/assets/a72aa0d4-6320-44aa-99f7-28b0bbab2196" width="49%"/>
</p>

---

## 🗃️ DB 테이블 요약

### 개발 환경(버전)
| 개발 도구 | 버전 |
|---|---|
| Visual Studio | 1.95.3 |
| Python | 3.11.3 |
| MySQL Workbench | 6.2 |
| TensorFlow | 2.12.0 |
| Keras | 2.12.0 |
| Flask | 3.0.3 |

### closet 테이블 구조
| Field | Type | Null | Key | Default | Extra |
|---|---|---|---|---|---|
| num | int(11) | NO | PRI | NULL | auto_increment |
| category | varchar(255) | YES |  | NULL |  |
| memo | text | YES |  | NULL |  |
| image | varchar(255) | YES |  | NULL |  |

- `num`: 의류 고유번호(PK)
- `category`: 의류 카테고리
- `memo`: 메모
- `image`: 이미지 파일 경로

### lookbook 테이블 구조
| Field | Type | Null | Key | Default | Extra |
|---|---|---|---|---|---|
| top | int(11) | YES |  | NULL |  |
| bottom | int(11) | YES |  | NULL |  |
| shoes | int(11) | YES |  | NULL |  |
| bag | int(11) | YES |  | NULL |  |
| lookname | varchar(100) | YES |  | NULL |  |
| looknum | int(11) | NO | PRI | NULL | auto_increment |

- `looknum`: 코디 고유번호(PK)
- `top/bottom/shoes/bag`: 코디에 사용된 의류 번호(closet.num 참조)
- `lookname`: 코디 이름
