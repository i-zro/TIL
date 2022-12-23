### awscli 설치
- curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
- sudo installer -pkg AWSCLIV2.pkg -target /

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
01-03. 강의 준비

[default]

 region=ap-northeast-2
           output=json
      aws_access_key_id=AKIAIOSFODNN7EXAMPLE  aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY 

[profile user1] 
aws_access_key_id=AKIAI44QH8DHBEXAMPLE 
aws_secret_access_key=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMDg2NjIyNjYsLTIyMDEwNjY5LDUwOT
kzMTQwNiwtNTk5NjkwMTIwXX0=
-->