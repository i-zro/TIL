# 실습 Key pair 생성

1. AWS Management Console Key Pair 생성
	1. AWS Management Console > EC2 Dashboard > Key-Pair --> Create Key-Pair --> pem 형식으로 다운로드
	2. *.pem > 편집기로 열기 > 전체 복사
	3. Cloud9 > New file > 붙여넣기 > 저장
	4. Cloud9 > New Terminal > Ownership 변경 > sudo chown ec2-user.ec2-user *.pem
	5. Cloud9 Terminal > ssh-keygen -y -f *.pem >> *.pub
	
2. 리눅스 ssh-keygen 명령어를 이용해서 Key Pair 생성 후 AWS Import
	1. ssh-keygen --help
	2. ssh-keygen -t rsa -b 4096 -C "" -f "$HOME/.ssh/<키페어이름>" -N ""
	3. sudo cp /home/ec2-user/.ssh/<키페어이름> /home/ec2-user/.ssh/<키페어이름>.pem
	4. AWS CLI로 AWS Import
		1. aws ec2 import-key-pair --key-name "<키페어이름>" --public-key-material fileb://~/.ssh/<키페어이름>.pub
		
3. Terraform Code를 작성 후 실행하여 AWS로 Key-Pair 전송
	Terraform aws key pair 검색 > Terraform Registry에서 aws_key_pair 예제 참조
	1. Cloud9 > New File > 예제 붙여 넣기
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNDQyODUwODNdfQ==
-->