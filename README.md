# 키로깅 TXT 생성 및 이메일 전송 프로그램 LOGGEE
## self-made keylogger(for education and study only)**

**제작자 - 스꾸(ben8169)  
깃허브 - https://github.com/ben8169/loggee  
티스토리(시연 설명) - https://ben8169.tistory.com/9** 

<hr>   


> ### Updates
 
### V.1.0.0.

#### 1.로깅 시작-종료시간, 각 key 별 개별 입력시간 기록
#### 2.각 key별 개별 log, 모든 log를 string으로 모은 concatenated log 두 가지 log 제공
#### 3.concatenated log >> 백스페이스 입력시 로그도 삭제, 특수키는 \t 처리, 가독성 높임
#### 4.key.left 정상종료시 자신의 gmail을 연동하여 log.txt 전송받고 로컬에서 삭제, 은폐성 향상

<hr>

> ### How to Use

**1. log.txt를 임시로 저장할 Path 설정**   
![image](https://user-images.githubusercontent.com/48664269/229177575-ad10ed0a-23ca-4fae-a4f8-670691a07755.png)

**2. stmp모듈용 google 계정의 '앱 비밀번호'를 발급뱓아 입력** (참고 - https://support.bespinglobal.com/ko/support/solutions/articles/73000545275--gmail-%EC%95%B1-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EC%83%9D%EC%84%B1%EB%B0%A9%EB%B2%95)
![image](https://user-images.githubusercontent.com/48664269/229174541-ed887d3c-c18b-4dda-be4e-b8dbc69a5ec4.png)          
<<발급 후 하단 빨간box 수정>>         
![image](https://user-images.githubusercontent.com/48664269/229175409-d885f16e-1ed6-47b3-96de-7a94961cde37.png)

**3. log.txt 받을 수신 메일 설정 (default 값: 본인 Mail)**         
![image](https://user-images.githubusercontent.com/48664269/229175743-c6e73a0b-1004-477f-8797-abe58172820e.png)        


**4. 키보드 왼쪽 키 입력시 logging 종료되고, 지정한 Email로 log 파일 전송 및 log.txt 로컬에서 제거!**

