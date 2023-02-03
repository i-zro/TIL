# [AWS JAM - DB] DMS로 Oracle DB에서 Aurora로 옮기기 (PUT YOUR DATABASE TO WORK....)


## Background

*   AnyCompany built the corporate database using Oracle. The database has not been built using a **highly available architecture** or in a way that will **keep operational costs low**.

*   The company CIO has tasked _you_ with **migrating** the database from **Oracle** to **Amazon Aurora MySQL**.

*   After researching the options, you have determined that [**AWS Database Migration Service**](https://aws.amazon.com/dms/) is the right tool for the job.

*   Using **DMS** will allow the **source database** to remain fully operational during the migration, helping to minimize downtime for applications that rely on the database.

## Task

*   Use the Database Migration Service (DMS) **Migration Wizard** to setup the **Database Migration Task**.

*   The Database Migration Task will replicate from **Oracle** to **Aurora MySQL**. The **Credentials** for Oracle and Aurora are in the **challenge output** section.

*   **Oracle's** Database **port** is: `1521`

*   **MySQL's** Database **port** is: `3306`

*   There is a **Security Group** for use with the Database Migration Instance: `Replication-Instance-SG`

*   The **Oracle** Database **SID** is: `DMSSMPL`

*   The **Oracle** Database **Schema** is: `DMS_SAMPLE`

*   Be sure to use the **VPC** named: `DbMigrateJam`

*   You do not need to use [**Schema Conversion Tool (SCT)**](https://aws.amazon.com/documentation/SchemaConversionTool/)

### While setting up the "Tasks" for replication:

*   Keep the `default` value for **Target Table Operations Mode**

*   Include **LOB **_**(Large Object Binary)**_ columns in replication by setting the **Max LOB** size

### Monitoring DMS Progress

*   Under the **DMS Task**, click on **Table Statistics**. You will be able to monitor individual tables, number of rows inserted, and state.

*   The **DMS Task** may display an error about **Replicating with Errors**. It is possible for a DMS Task to successfully replicate a database while still encountering trivial errors that do not impact the data integrity.

## Inventory

_The following resources have been precreated for this challenge:_

*   VPC _(Virtual Private Cloud)_

*   Security Groups

    *   Database-SG

    *   Replication-Instance-SG

*   Oracle Database

*   RDS Aurora MySQL Database

## Services you should use

*   DMS _(Database Migration Service)_

## Getting Started

*   Create a DMS Endpoint

*   Create a DMS Instance

*   Create a DMS Task

*   Run the DMS Task to replicate data from Oracle to Aurora

## Validation

In the **Output Properties** section there is a link titled: `CheckURL`. The **CheckURL** webpage will provide you with details of the challenge progress. **After the DMS Task has completed** successfully, a **secret answer** will be displayed. Cut-and-paste the secret answer to complete the jam challenge. The answer is **CaSe SeNsItIvE**, so ensure to copy the answer instead of re-typing it.

### Factors that must be true for the task to be successful:

*   The number of rows in the Aurora MySQL database table must match the row count in the source Oracle database table.

### Output Properties

<table data-layout="default" data-local-id="5ed7259a-2278-4971-9924-7cd71fcb03a2" class="confluenceTable" style="margin: 10px 0px 0px; overflow-x: auto; font-family: Arial, sans-serif; letter-spacing: normal;"><colgroup><col style="width: 340px;"><col style="width: 340px;"></colgroup>

<tbody>

<tr>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

CheckUrl

</td>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

[http://52.25.130.210/index.php](http://52.25.130.210/index.php)

</td>

</tr>

<tr>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

SourceDbName

</td>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

dmssmpl

</td>

</tr>

<tr>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

SourceEndpoint

</td>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

[dmssmpl.cislylx2zhmz.us-west-2.rds.amazonaws.com](http://dmssmpl.cislylx2zhmz.us-west-2.rds.amazonaws.com/)

</td>

</tr>

<tr>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

SourcePassword

</td>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

Fleshy_gave0Antony

</td>

</tr>

<tr>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

SourcePort

</td>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

1521

</td>

</tr>

<tr>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

SourceUsername

</td>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

dmssample2

</td>

</tr>

<tr>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

TargetEndpoint

</td>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

[labstack-prewarm-7723d44b-auroramysqldatabaseaf3e5-hrmi3pwh4wkm.cluster-cislylx2zhmz.us-west-2.rds.amazonaws.com](http://labstack-prewarm-7723d44b-auroramysqldatabaseaf3e5-hrmi3pwh4wkm.cluster-cislylx2zhmz.us-west-2.rds.amazonaws.com/)

</td>

</tr>

<tr>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

TargetPassword

</td>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

Bill_strike5patent

</td>

</tr>

<tr>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

TargetPort

</td>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

3306

</td>

</tr>

<tr>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

TargetUsername

</td>

<td class="confluenceTd" style="border: 1px solid rgb(221, 221, 221); padding: 7px 10px; vertical-align: top; min-width: 8px;">

clusteradmin

</td>

</tr>

</tbody>

</table>

# 실행 과정 및 결과

* * *

참고 : [https://cloudest.tistory.com/70](https://cloudest.tistory.com/70)

* * *

## 서브넷 그룹 생성

*   DMS 콘솔 → 서브넷 그룹 → 서브넷 그룹 생성

![](https://i.imgur.com/D9VZTYC.png)


## 복제 인스턴스 생성

![](https://i.imgur.com/NHNqRa6.png)

![](https://i.imgur.com/F7zfs9b.png)

## DMS Endpoint 만들기

*   소스 엔드포인트

![](https://i.imgur.com/41iltk7.png)


*   대상 엔드포인트

![](https://i.imgur.com/XyIEx42.png)


## DMS Instance 만들기

![](https://i.imgur.com/8jjUS2Y.png)

![](https://i.imgur.com/xDpOTPP.png)


## DB Migration Task 생성

![](https://i.imgur.com/0HtPvEg.png)

![](https://i.imgur.com/pQxIyCC.png)

![](https://i.imgur.com/exdLbZX.png)


*   만들면 자동으로 실행됨

![](https://i.imgur.com/0oAqIBX.png)

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NjMwODQzOV19
-->