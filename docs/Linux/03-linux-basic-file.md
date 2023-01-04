# 03. 파일

# 1. 파일의 종류

- 일반 파일
- 디렉터리
- 심볼릭 링크 파일 ( = 윈도우 바로가기 )
- 블록 디바이스 파일
- 문자 디바이스 파일
- 파이프 파일 : 파이프를 나타내는 파일. 프로세스간 통신에 사용 됨.
- 소켓 : 소켓을 나타내는 파일. 프로세스간 통신에 사용됨.

# 2. 디렉토리

## 대표적인 디렉토리

![](https://i.imgur.com/41F0DC2.png)

- /bin : 모든 사용자 사용가능한 `실행` 파일 위치
- /sbin : 시스템 관리자 권한으로 실행 가능한 `실행` 파일 위치
- /usr : 사용자가 추가한 `실행` 파일 위치

- /etc : 여러 가지 **설정** 파일
- /lib : 공유 라이브러리 디렉토리
- /home : 사용자들의 홈 디렉토리
- /mnt : 일시적으로 파일 시스템에 마운트하는 경우 사용하는 디렉토리

- /proc, /sys : 시스템 정보 설정/조회할 수 있는 디렉토리 (App - OS 통로)
- /tmp : 임시 디렉토리
- /dev : 디바이스 파일 디렉토리

# 3. 아이노드 그리고 하드링크와 소프트링크

## 파일 구조

- Inode가 file의 정보를 갖고 있는 방식

![](https://i.imgur.com/idgcRZI.png)

## 하드링크와 소프트링크

- 하드링크(hard-link) vs 소프트링크(soft-link == symbolic link == symlink)

    ![](https://i.imgur.com/O57V2xB.png)

    - 하드링크는 inode를 공유하는 것, 소프트링크는 윈도우 바로가기 느낌으로 경로만 따오는 것
    - 일반적으로 소프트링크를 많이 사용.

# [실습] 파일 다루기

- 파일 이름 바꾸기 
    - testfile을 apple로 바꾸기
        - mv testfile apple

# [실습] 디렉토리 다루기

- 디렉토리 지우기
    - testdir 지우기
        - rm -rf testdir/    

# [실습] 아이노드와 하드링크

![](https://i.imgur.com/6SvM9yi.png)

- 아이노드 확인
    - ls -i
- 디렉토리 내 전체 아이노드 확인
    - ls -ali
- 하드 링크 만들기
    - ln TARGET LINK_NAME
        - ln pineapple hello

        ![](https://i.imgur.com/xlMojuN.png)

- 파일의 상세 정보 (아이노드 내용 포함)
    - stat [파일명]

# [실습] 소프트링크

- 소프트링크 만들기
    - ls -s TARGET LINK_NAME
        - ls -s pineapple hello

        ![](https://i.imgur.com/DsEWsmS.png)
        
        
- 하드링크 파일은 추후 경로를 바꿔도 그대로 유지
- 소프트링크 파일은 경로가 바뀌면 링크 깨짐, 대신 당연히 절대경로로 지정하면 가능

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk0NzI2ODg2MF19
-->