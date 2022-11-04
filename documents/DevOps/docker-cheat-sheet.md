# 도커 Cheat-Sheet

## 컨테이너 시작 주요 옵션

```
docker run \
-i \ # 호스트의 표준 입력을 컨테이너와 연결 (interactive)
-t \ # TTY 할당
--rm \ # 컨테이너 실행 종료 후 자동 삭제
-d \ # 백그라운드 모드로 실행 (detached)
--name hello-world \ # 컨테이너 이름 지정
-p 80:80 \ # 호스트 - 컨테이너 간 포트 바인딩
-v /opt/example:/example \ # 호스트 - 컨테이너 간 볼륨 바인딩
fastcampus/hello-world:latest \ # 실행할 이미지
my-command # 컨테이너 내에서 실행할 명령어
```

## 모든 컨테이너 종료

docker stop $(docker ps -a -q)

### 환경 변수 주입

- docker run -i -t -e MY_HOST=ENV_TEST ubuntu:focal bash

- docker run -i -t --env-file ./test.env ubuntu:focal env

<!--stackedit_data:
eyJoaXN0b3J5IjpbMzYzNjkyNjM5XX0=
-->