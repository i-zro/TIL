
# [AWS JAM - DB] MySQL RDS 만들고 MySQL Workbench로 연결 (Create and Connect to mySQL RDS Instance!)

# MySQL Workbench 설치

![](https://i.imgur.com/G73VvaG.png)


-   Oracle 로그인 및 설치
    

# RDS 생성하기

## 조건

-   지역 : US-EAST2 (Ohio)
    
-   템플릿 : 프리티어 항목
    
-   username과 password는 자유
    
-   "yes" for publicly accessible
    
-   새로운 보안 그룹 (보안그룹은 default X)
    
-   데이터 베이스 이름 지정
    
-   삭제 방지
    

### a. Amazon RDS 콘솔의 오른쪽 위 모서리에서 DB 인스턴스를 생성할 _리전_을 선택합니다.

![](https://i.imgur.com/A3aliXs.png)


### b. **Create database** 섹션에서 **Create database**를 선택합니다.

-   RDS 검색
    
-   데이터베이스 생성 클릭

![](https://i.imgur.com/PUCORQT.png)

    

### c. 이제 엔진을 선택할 수 있는 옵션이 표시됩니다. 이 자습서에서는 _MySQL 아이콘_을 클릭하고, **Only enable options eligible for RDS Free Usage Tier**를 선택한 다음, **Next**를 클릭합니다.

-   엔진 유형은MySQL 선택
    
    ![](https://i.imgur.com/yBuuM1s.png)


-   템플릿은 프리티어 선택

    ![](https://i.imgur.com/aHH1Yrc.png)


### d. 이제 DB 인스턴스를 구성합니다. 아래 목록은 본 자습서에서 사용할 수 있는 설정의 예를 보여줍니다.

**Instance specifications**:

-   **License model**: MySQL의 일반 라이선스 계약을 사용하도록 기본값인 _general-public-license_를 선택합니다. MySQL에는 단 하나의 라이선스 모델만 있습니다.
    
-   **DB engine version**: MySQL의 기본 버전을 선택합니다. 일부 리전에서는 Amazon RDS가 여러 버전의 MySQL을 지원합니다.
    
-   **DB instance class**: _db.t2.micro --- 1vCPU, 1 GIB RAM_을 선택합니다. 이는 1GB 메모리 및 1vCPU에 해당합니다. 지원되는 인스턴스 클래스 목록을 보려면 [Amazon RDS 제품 세부 정보](https://aws.amazon.com/rds/details/)를 참조하십시오.
    
-   **Multi-AZ deployment**: 다중 AZ 배포에 대해서는 비용이 부과됩니다. 다중 AZ 배포를 사용하면 다른 가용 영역에 동기식 예비 복제본을 자동으로 프로비저닝하고 유지합니다. 자세한 내용은 [고가용성 배포](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)를 참조하십시오.
    
-   **Storage type**: _General Purpose (SSD)_를 선택합니다. 스토리지에 대한 자세한 내용은 [Amazon RDS용 스토리지](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html)를 참조하십시오.
    
-   **Allocated storage**: 기본값인 20을 선택하여 데이터베이스에 20GB의 스토리지를 할당합니다. Amazon RDS for MySQL에서는 최대 16TB까지 확장할 수 있습니다.
    
-   **Enable storage autoscaling**: 워크로드가 주기적이거나 예측할 수 없는 경우 스토리지 autoscaling을 활성화하여 필요할 때 RDS가 스토리지를 자동으로 확장하도록 하십시오. 이 자습서에서는 이 옵션을 적용하지 않습니다.
    

**Settings**:

-   **DB instance identifier**: 선택한 리전의 계정에 대해 고유한 DB 인스턴스 이름을 입력합니다. 본 자습서에서는 이름을 _rds-mysql-10minTutorial_로 지정합니다.
    
    -   jam-database-2로 지정
        
-   **Master username**: DB 인스턴스에 로그인할 때 사용할 사용자 이름을 입력합니다. 본 예제에서는 _masterUsername_을 사용합니다.
    
    -   naa0로 지정
        
-   **Master password**: 마스터 사용자 암호에 8~41개의 인쇄용 ASCII 문자(/, " 및 @ 제외)가 포함된 암호를 입력합니다.
    
    -   et1234!!로 지정
        
-   **Confirm password**: 암호를 다시 입력합니다.
    
-   **Allocated Storage**: 5를 입력하여 데이터베이스에 5GB의 스토리지를 할당합니다. 스토리지 할당에 대한 자세한 내용은 Amazon Relational Database Service 기능 페이지를 참조하십시오.(순서 변경, 스토리지 유형 다음에 위치)
    
![](https://i.imgur.com/0FyuJ4K.png)


### e. 이제 **Configure Advanced Settings** 페이지입니다. 여기에서 RDS가 MySQL DB 인스턴스를 시작하는 데 필요한 추가 정보를 제공할 수 있습니다. 아래 목록은 예제 DB 인스턴스에 대한 설정을 보여줍니다.

**Network & Security**

-   **Virtual Private Cloud (VPC**): _Default VPC_를 선택합니다. VPC에 대한 자세한 내용은 [Amazon RDS 및 Amazon Virtual Private Cloud(VPC)](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSVPC.html)를 참조하십시오.
    
    -   Default VPC 선택
        
-   **Subnet group**: _default_ 서브넷 그룹을 선택합니다. 서브넷 그룹에 대한 자세한 내용은 [DB 서브넷 그룹을 사용한 작업](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets)을 참조하십시오.
    
-   **Public accessibility:** _Yes_를 선택합니다. 이렇게 하면 데이터베이스 인스턴스에 대한 IP 주소가 할당되므로 사용자 디바이스에서 데이터베이스에 직접 연결할 수 있습니다.
    
    -   예 선택
        
-   **Availability zone**: _No preference_ 를 선택합니다. 자세한 내용은 [리전 및 가용 영역](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html)을 참조하십시오.
    
-   **VPC security groups**: _Create new VPC security group_을 선택합니다. 이렇게 하면 현재 사용하고 있는 디바이스의 IP 주소에서, 생성된 데이터베이스로 연결할 수 있는 보안 그룹이 생성됩니다.
    
    -   jam-db-sg 생성
        
        ![](https://i.imgur.com/5fbYowl.png)


**Database options**

-   **Database name**: 데이터베이스 이름으로 1~64자의 영숫자 문자를 입력합니다. 이름을 제공하지 않으면 Amazon RDS가 자동으로 데이터베이스를 지금 생성하고 있는 DB 인스턴스에 생성하지는 않습니다.
    
    -   추가구성에서 확인 가능 - jamdb로 설정

        ![](https://i.imgur.com/PajKlP2.png)


-   **Port**: 기본값인 _3306_을 유지합니다.
    
-   **DB parameter group**: 기본값인 _default.mysql5.6_을 유지합니다. 자세한 내용은 [DB 파라미터 그룹 작업](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)을 참조하십시오.
    
-   **Option group**: 기본값인 _default:mysql5.7_ 을 선택합니다. Amazon RDS는 옵션 그룹을 사용하여 추가 기능을 활성화 및 구성합니다. 자세한 내용은 [옵션 그룹 작업](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html)을 참조하십시오.
    
-   **IAM DB authentication**: _Disable_을 선택합니다. 이 옵션은 AWS IAM 사용자 및 그룹을 사용하여 데이터베이스 자격 증명을 관리하도록 허용합니다.
    

**Encryption**

이 옵션은 프리 티어에서 제공하지 않습니다. 자세한 내용은 [Amazon RDS 리소스 암호화](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)를 참조하십시오.

-   **프리티어인데 이 부분이 해제가 기본적으로 안돼있어서 DB Connection Error 일어남. 반드시 해제!**

![](https://i.imgur.com/mBupEoM.png)

    

**Backup**

-   **Backup retention period**: 생성한 백업을 보관할 일수를 선택할 수 있습니다. 본 자습서의 경우 이 값을 _1 day_로 설정합니다.
    
-   **Backup window**: 기본값인 _No preference_를 사용합니다.
    

**Monitoring**

-   **Enhanced Monitoring:** 프리 티어 범위를 벗어나지 않도록 _Disable enhanced monitoring_ 를 선택합니다. 향상된 모니터링 기능을 활성화하면 DB 인스턴스가 실행되는 운영 체제(OS)에 대한 지표가 실시간으로 제공됩니다. 자세한 내용은 [DB 인스턴스 지표 보기](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html)를 참조하십시오.
    

**Performance Insights**

본 자습서에서는  _Disable Performance Insights_를 선택합니다.

**Maintenance**

-   **Auto minor version upgrade:** _Enable auto minor version upgrade_를 선택하여 자동 업데이트가 제공될 때 이를 수신합니다.
    
-   **Maintenance Window:** _No preference_를 선택합니다.
    

**Deletion protection**

본 자습서에서는 _Enable deletion protection_ 선택을 취소합니다. 이 옵션이 활성화되면 데이터베이스를 삭제할 수 없습니다.

-   추가 구성에서 확인 가능 - 삭제 방지 활성화
    
![](https://i.imgur.com/gtOqzd2.png)


**Create database**를 클릭합니다.

# [오류] Cannot create a publicly accessible DBInstance. The specified VPC has no internet gateway attached.Update the VPC and then try again**

**[해결] 퍼블릭 액세스를 허용했지만, default VPC에 인터넷 게이트웨이가 붙어있지 않아서 생긴 문제**

-   VPC > 인터넷 게이트웨이 생성
    
    -   default-igw
  
      ![](https://i.imgur.com/WjgwSvQ.png)


-   방금 생성한 인터넷 게이트웨이를 선택한 후 **Actions, Attach to VPC(작업, VPC에 연결)**을 선택
    
    ![](https://i.imgur.com/ktdC3Fc.png)


# MySQL Workbench에서 RDS 연결해보기

-   Hostname에 엔드포인트, 포트, Username과 password까지 입력해주고 연결

![](https://i.imgur.com/tV9m0zO.png)

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NjA4NDAxMzUsLTEyOTk2NTYyNjddfQ
==
-->