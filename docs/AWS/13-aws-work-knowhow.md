- 221205, 디지털 카탈로그 CQX 처리 과정
	- 사용자에게 정책 추가할 때 인라인으로 추가할 때도 있지만, 보통은 그룹 Policy를 붙여서 사용한다.

	- Cloud Watch 로그그룹 - 쌓이는 곳은 S3 - 보존 기간 설정 자체는 Cloud Watch > 로그 > 로그 그룹 페이지에서 설정 

	- VPC 기본 Quota는 5개, 늘리려면 Service Quotas에서 VPCs per Region 에서 요청 가능

	- RDS 성능 performance insights 활성화는 t2 이상 부터 가능 - https://techblog.woowahan.com/2593/

- 221206, 키오스크 CQX 처리 과정
	- 키오스크의 경우 aws backup 서비스 사용하여 OS+데이터는 AMI로 주 1회 뜨고, 데이터만 따로 매일 1회 스냅샷 떠서 EC2의 두 가지 방법의 복원 방안을 만들어놓음. - https://aws.amazon.com/ko/backup/
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcwOTI4NTc2MCwtMjE5NzY1NjYzLDE2Mz
A2OTA4MTUsMTk0MjEzNjA1M119
-->