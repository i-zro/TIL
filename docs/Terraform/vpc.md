# 실습 Cloud9에서 VPC 생성

1. Cloud9 > New file > vpc.tf 생성, Create Folder 3.vpc 생성
	1. Terraform Registry > provider 추가
	2. Terraform Registry > VPC
		1. VPC CIDR 10.0.0.0/16
		2. Subnet
			1. Public 10.0.1.0/24 2a, 10.0.2.0/24 2c
			2. Private 10.0.3.0/24 2a, 10.0.4.0/24 2c
		3. Internet Gateway
		4. Routing Table
			1. Public 1개
			2. Private 2개
		5. Routing Table Associate
			1. Public subnet 10.0.1.0/24, 10.0.2.0/24
			2. Private subnet1 10.0.3.0/24
			3. Private subnet2 10.0.4.0/24
		6. EIP(Elastic IP) 2a, 2c
		7. NAT GW 2a, 2c
			1. EC2 Pri1, Pri2
		8. EC2 생성
			1. EC2 bastion, private subnet1, private subnet2
		9. ALB(Application Load Balancer)
		10. AMI(Amazon Machine Image)

2. 실습 정리
	1. tf destroy

3. 구성도
![Image](https://i.imgur.com/4Lu3B3U.png)