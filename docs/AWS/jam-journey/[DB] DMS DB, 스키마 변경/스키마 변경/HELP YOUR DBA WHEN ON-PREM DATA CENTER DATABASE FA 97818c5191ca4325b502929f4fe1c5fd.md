# HELP YOUR DBA WHEN ON-PREM DATA CENTER DATABASE FAILS CLI Access

**Background**

Your company has decided to use AWS for Disaster Recovery (DR). As part of this initiative, on-prem databases are now replicated to AWS. AWS Database Migration Service (DMS) was chosen to perform the initial database load and subsequent replication of ongoing changes. Your DBA worked on this and set up AWS DMS to replicate your DEV database to AWS. They also duplicated all the DMS resources from the DEV environment , but the before the production setup is done, he left on vacation.

**Your Task**

You have the task to edit the dev instance setup and set it up for production. There are few differences in dev vs prod setup:

1. The onprem database port for prod is 1521
2. The data should be validated after migration
3. The database schema is HR in prod instead of HUMAN_RESOURCE in dev

**Inventory**

1. AWS DMS Replication Instance
2. AWS DMS Source Endpoint
3. AWS DMS Target Endpoint
4. AWS DMS Replication Task
5. AWS RDS Target database (simulate database on AWS)
6. EC2 source database (simulate onprem database)

**Task Validation**

After completing the tasks, click on Check Progress to see if all the requirements are satisfied. You may need to give it a minute or two once the task is complete.

**Getting Started**

If the DMS task returns error, then before restarting the task you may need to change the additional setting. Select "Drop tables on target" and save it before starting it again. Otherwise reset the challenge if it persists.

⇒ 너무 안돼서 결국 클루 다 까고 따라갔다.

Walk through

1. Go to AWS Service DMS
2. Go to item "Endpoints"
3. Select the one that has type "Source" and modfiy it
4. Change the port from 5000 to 1521

![Untitled](HELP%20YOUR%20DBA%20WHEN%20ON-PREM%20DATA%20CENTER%20DATABASE%20FA%2097818c5191ca4325b502929f4fe1c5fd/Untitled.png)

1. Go to "Database migration tasks"
2. Select the identifier
3. Click on Actions to modify the identifier
    
    7.1. at "Task setings" enable "Enable validation"
    
    ![Untitled](HELP%20YOUR%20DBA%20WHEN%20ON-PREM%20DATA%20CENTER%20DATABASE%20FA%2097818c5191ca4325b502929f4fe1c5fd/Untitled%201.png)
    
    7.2. at "Table mapping" change both "Schema names" from HUMAN_RESOURCES to HR
    
    ![Untitled](HELP%20YOUR%20DBA%20WHEN%20ON-PREM%20DATA%20CENTER%20DATABASE%20FA%2097818c5191ca4325b502929f4fe1c5fd/Untitled%202.png)
    
    7.3. at "Transformation rules" change the "Schema names" in all 3 rules from HUMAN_RESOURCES to HR
    
    ![Untitled](HELP%20YOUR%20DBA%20WHEN%20ON-PREM%20DATA%20CENTER%20DATABASE%20FA%2097818c5191ca4325b502929f4fe1c5fd/Untitled%203.png)
    
    7.4. press save
    
4. Run the database migration task (Actions -> Restart/Resume)