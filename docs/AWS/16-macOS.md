# 자주 쓰는 단축어
- 현재 자격증명 정보 확인 : aws sts get-caller-identity

### awscli 설치
- curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
- sudo installer -pkg AWSCLIV2.pkg -target /

## IAM 사용자 만들기
- Services(서비스)에서 IAM 을 검색
- 사용자 → 사용자 추가 클릭

  - 사용자 이름 : 자유롭게 작성
  - 액세스 유형 : 프로그래밍 방식, AWS Management Console 액세스
  - 콘솔 비밀번호: 자유롭게 설정

![Image](https://i.imgur.com/fpEdDxr.png)

- 기존 정책 직접 연결 → AdministratorAccess 체크

## awscli 자격증명 설정 (AccessKey)
- ~/.aws/config

```bash
[default]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE      
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

### 사용자 프로파일 추가
- ~/.aws/config

```bash
[default]
region=ap-northeast-2
output=json         
aws_access_key_id=AKIAIOSFODNN7EXAMPLE  
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY 

[profile user1] 
aws_access_key_id=AKIAI44QH8DHBEXAMPLE 
aws_secret_access_key=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
```



### **Error:** **Unsupported Terraform Core version**
- terraform init 과정
- 해결 : required_version을 ~> 1.0.0 에서 >= 1.0.0으로 바꿈. 크게 버전에 따른 문제는 없어서 실행 조건만 바꿔준 것.

```bash
terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg1OTMyODcsLTk3OTc2ODcyMiwtODg2MT
Y3MjA2LC0yMjAxMDY2OSw1MDk5MzE0MDYsLTU5OTY5MDEyMF19

-->