# 02. 최소한의 커맨드라인 사용법

# 1. 리눅스 쉘

- 리눅스에서 커널 바깥 껍질

![](https://i.imgur.com/R8LUxRF.png)

- 사용자는 터미널 통해 쉘 사용

![](https://i.imgur.com/0PiK1BA.png)

# 2. 기본 쉘 명령어

- 매뉴얼 조회: man
    - 사용 예시 : ls 명령어 대해 알고 싶다 -> man ls
    - 찾기 : 이후 매뉴얼에서 'word' 찾고 싶다 -> /word
    
- 파일 목록/내용 조회 관련 명령어: ls, cat, head, tail
    - 파일 전체 정보 보여주기 : ls -al
    - 직전 디렉토리 이동 : cd -
    - 파일 앞 3줄만 보기 : head abc.txt -n 3
    
- 검색/탐색 관련 명령어: grep, find
    - dpkg.log에서 startup packages configure 찾기 : grep "startup packages configure" dpkg.log
    - ls -al 중 kern.log 포함 된 것만 찾기 : ls -al | grep kern.log
    - /etc 경로에서 conf 확장자 가지는 파일 다 출력 : find /etc -name "*.conf" -print
- 압축/해제 관련 명령어: tar, gzip/gunzip, zip/unzip
    - filelist라는 파일 압축하고 싶을 때 : gzip filelist
    - filelist.zip 파일 압축해제 하고 싶을 때 : gunzip filelist.zip
    - filelist.gz snap/ 사진 폴더를 test.tar.gz로 압축하고 싶을 때 : tar -czf test.tar.gz filelist.gz snap/ 사진
    - testdir에 test.tar.gz 압축 풀고 싶을 때 : tar -zxf ../test.tar.gz
    
    ![](https://i.imgur.com/2w2Astm.png)

- 시간 관련 명령어: date, cal
    - 오늘 날짜, 시간 보기 : date
        - UTC 시간 보고 싶다 -> date -u
        - 연도 -> date +%Y
    - 이번 달 달력 보기 : cal
        - 2022년 전체 달력 보고 싶다 -> cal 2022
        - 1997년 12월 보고 싶다 -> cal -d 1997-12
- 기타 명령어: echo, exit, history
    - 이전 커맨드들 목록 : history
        - history 16번째 실행 하고 싶다 -> !16
    - 직전 커맨드 실행 : !!
    - PATH 환경변수 보고 싶다 : echo $PATH
        - 참고 : PATH는 명령어가 저장된 경로
- 관리자 권한 실행: sudo
- 패키지 매니저: apt
- 텍스트 에디터: nano

## 기타 명령어
- 우분투는 원하는 부분 드래그 후 원하는 곳에 휠 클릭 만으로 복사 - 붙여넣기 됨
- find 명령어 filelist라는 파일에 저장하고 싶을 때 : find > filelist
- ls 명령어가 어느 경로에 있는지 알고 싶다 -> which ls


<!--stackedit_data:
eyJoaXN0b3J5IjpbOTM0MTEzNjA0XX0=
-->