# [도커와 쿠버네티스를 이용한 서비스 운영] 02_01. 도커 이미지와 컨테이너

## 컨테이너 시작

1. 컨테이너 생성 후 시작

docker create [image]

docker start [container]

2. 컨테이너 생성 및 시작

docker run [image]

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

## 컨테이너 종료

1. 컨테이너 종료 (SIGTERM 시그널 전달)

docker stop [container]

2. 모든 컨테이너 종료

docker stop $(docker ps -a -q)


## 컨테이너 삭제

1. 컨테이너 삭제 (실행중인 컨테이너 불가)

docker rm [container]

2. 컨테이너 강제 종료 후 삭제 (SIGKILL 시그널 전달)

docker rm -f [container]

3. 중지된 모든 컨테이너 삭제

docker container prune

## 엔트리 포인트와 커맨드

- 엔트리포인트 (Entrypoint)

도커 컨테이너가 실행할 때 고정적으로 실행되는 스크립트 혹은 명령어
생략할 수 있으며, 생략될 경우 커맨드에 지정된 명령어로 수행

    - 예시


    FROM node:12-alpine
    RUN apk add --no-cache python3 g++ make
    WORKDIR /app
    COPY . .
    RUN yarn install --production
    ENTRYPOINT ["docker-entrypoint.sh"]
    CMD ["node"]
    

- 엔트리포인트가 커맨드 앞에 붙는 방식임 (아래 커맨드에서 echo 엔트리포인트가 커맨드 hello world 앞에 붙음)
    - docker run --entrypoint sh ubuntu:focal
    - docker run --entrypoint echo ubuntu:focal hello world

![](https://i.imgur.com/nDK1yoq.png)


## 도커 환경변수 주입

1. -e

docker run -i -t -e MY_HOST=ENV_TEST ubuntu:focal bash

![](https://i.imgur.com/qMnmWdm.png)

2. --env-file

```
"test.env" 
MY_NAME=SIMON
MY_AGE=345
MY_FACE=GOOD
```

docker run -i -t --env-file ./test.env ubuntu:focal env

## 도커 exec

- 실행중인 컨테이너에 명령어를 실행 (디버깅이나 이슈해결 목적)

```
$ docker exec [container] [command]
# my-nginx 컨테이너에 Bash 셸로 접속하기
$ docker exec -i -t my-nginx bash
# my-nginx 컨테이너에 환경변수 확인하기
$ docker exec my-nginx env
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjQ1ODg0NDk0LC0yMDg4NzQ2NjEyXX0=
-->