- 검색창에 IAM 검색 이후, 사용자 - 사용자 추가를 눌러 준다.

<img width="1434" alt="image" src="https://user-images.githubusercontent.com/48379869/234640719-834ad937-9f7f-4de6-8a49-dfdd76080ac6.png">

- 이름을 적당히 지어준다.

<img width="1396" alt="image" src="https://user-images.githubusercontent.com/48379869/234640981-4db70f5a-864c-4d3b-a551-9d668f6bc625.png">


- 정책 연결에서 AmazonS3FullAccess 를 우선 눌러준다.

<img width="1375" alt="image" src="https://user-images.githubusercontent.com/48379869/234641127-4e2a543f-c3cf-41b9-acb7-ef852ddb3c34.png">

- 보안 자격 증명에서 액세스 키를 만들어 준다.

<img width="1128" alt="image" src="https://user-images.githubusercontent.com/48379869/234641383-b6ab2f70-b5aa-4745-a9c1-d56997a5b366.png">

<img width="1133" alt="image" src="https://user-images.githubusercontent.com/48379869/234641546-add56fa3-f103-46f5-9d60-dbc7391cad93.png">

- 이 부분은 애플리케이션을 선택해 준다.

<img width="884" alt="image" src="https://user-images.githubusercontent.com/48379869/234641725-3a83d270-2d07-4694-8b0a-153eca721172.png">

- 이후 나오는 화면에서 액세스 키 저장

- aws cli가 설치가 되어있다면, 다음과 같이 cmd에서 s3 버킷이 잘 잡히는 지 확인 가능
  - 먼저 aws configure로 액세스 키, 시크릿 키, 리전, 출력형식(공백으로 둬도됨) 으로 만들어준 s3 iam user를 설정해준다.
<img width="322" alt="image" src="https://user-images.githubusercontent.com/48379869/234642835-8bf88be9-0fef-4294-bd06-8944d9f90a03.png">

  - 두번째로 s3에 접근 가능한지 확인하도록 `aws s3 ls` 명령어를 입력해 버킷이 잘 나오는 지 확인 한다.
  
  <img width="260" alt="image" src="https://user-images.githubusercontent.com/48379869/234643205-b99a22ed-7f64-4fe6-84cb-b32180c434dc.png">
