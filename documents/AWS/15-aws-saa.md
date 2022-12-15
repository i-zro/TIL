Q. 솔루션 설계자는 회사의 스토리지 비용을 줄이기 위한 솔루션을 구현해야 합니다. 회사의 모든 데이터는 Amazon S3 Standard 스토리지 클래 스에 있습니다. 회사는 모든 데이터를 최소 25년 동안 보관해야 합니다. 최근 2년 동안의 데이터는 가용성이 높고 즉시 검색할 수 있어야 합니 다. 어떤 솔루션이 이러한 요구 사항을 충족합니까?

(A). Amazon S3에 로그 저장 AWS Backup을 사용하여 S3 Glacier Deep Archive로 1개월 이상 된 로그 이동 (B). Amazon S3에 로그 저장 S3 수명 주기 정책을 사용하여 1개월 이상 된 로그를 S3 Glacier Deep Archive로 이동 (C). Amazon CloudWatch Logs에 로그 저장. AWS Backup을 사용하여 1개월 이상 된 로그를 S3 Glacier Deep Archive로 이동 (D). Amazon CloudWatch Logs에 로그를 저장. Amazon S3 수명 주기 정책을 사용하여 S3 Glacier Deep Archive로 1개월 이상 된 로그를 이동 합니다.

A. (B)

이 문항 CloudWatch Logs랑 S3 중 헷갈렸는데 `aws backup` 은 애초에 리소스 백어

![](https://i.imgur.com/tQY1cqO.png)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExOTg1NzU4MTYsLTI2MTY5NDhdfQ==
-->