- 우분투는 원하는 부분 드래그 후 원하는 곳에 휠 클릭 만으로 복사 - 붙여넣기 됨
- find 명령어 filelist라는 파일에 저장하고 싶을 때 : find > filelist
- ls 명령어가 어느 경로에 있는지 알고 싶다 -> which ls
- PATH 환경변수 보고 싶다 : echo $PATH
- 파일 전체 정보 보여주기 : ls -al
- 직전 디렉토리 이동 : cd -
- 파일 앞 3줄만 보기 : head abc.txt -n 3
- ls -al 중 kern.log 포함 된 것만 찾기 : ls -al | grep kern.log
- /etc 경로에서 conf 확장자 가지는 파일 다 출력 : find /etc -name "*.conf" -print
- filelist라는 파일 압축하고 싶을 때 : gzip filelist
- filelist.zip 파일 압축해제 하고 싶을 때 : gunzip filelist.zip
- filelist.gz snap/ 사진 폴더를 test.tar.gz로 압축하고 싶을 때 : tar -czf test.tar.gz filelist.gz snap/ 사진
- testdir에 test.tar.gz 압축 풀고 싶을 때 : tar -zxf ../test.tar.gz
<!--stackedit_data:
eyJoaXN0b3J5IjpbODc2ODkwOTQ4LDEyMjY5Nzg4MzJdfQ==
-->