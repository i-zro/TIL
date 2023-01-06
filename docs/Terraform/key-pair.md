# Key pair 생성

1. aws configure
	1. terraform용 IAM 사용자 생성 후 configure

2. 리눅스 ssh-keygen 명령어를 이용해서 Key Pair 생성 후 AWS Import
	1. 현재 폴더에 tf-key-pair 라는 이름으로 만들기 => ssh-keygen -t rsa -b 4096 -C "" -f"./tf-key-pair" -N ""
		
3. Terraform Code를 작성 후 실행하여 AWS로 Key-Pair 전송
	1. terraform code 작성 (Terraform 레포지토리 terraform 23.01.05.aws-key-pair 브랜치)
	2. terraform init - terraform plan - terraform apply

#### terrafrom 코드

```bash
# aws provider 설정
provider "aws" {
  region = "ap-northeast-2"
}

# aws_key_pair resource 설정
resource "aws_key_pair" "terraform-key-pair" {
  # 위(terraform-key-pair)는 terraform이 인식하는 name, 
  # 아래(tf-key-pair)는 aws에등록할 key pair의 name
  key_name   = "tf-key-pair"
  
  # public_key = .pub파일 경로
  public_key = file("./keys/tf-key-pair.pub")
  
  tags = {
  	description = "terraform key pair import"
  }
}
```

#### 결과 확인

```bash
$ terraform init

Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/aws...
- Installing hashicorp/aws v4.49.0...
- Installed hashicorp/aws v4.49.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

```bash
$ terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions
are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_key_pair.terraform-key-pair will be created
  + resource "aws_key_pair" "terraform-key-pair" {
      + arn             = (known after apply)
      + fingerprint     = (known after apply)
      + id              = (known after apply)
      + key_name        = "tf-key-pair"
      + key_name_prefix = (known after apply)
      + key_pair_id     = (known after apply)
      + key_type        = (known after apply)
      + public_key      = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMacksku1OXpLErjjTS7N11jtt0Wf/+dHo21OcwJ3YTOQ9wlcnKFPphUQgu8G7SZL+73NjG/fhxShBbAY3MVn8sj2mMIB0vZOXWEpRMzNLOOMuOkvcSOR675b6qRVEm8LG/oYIeC45+H2TgbY78BKoPGqhhgwUEDd9/qcgtUHN/pLK2fe1Io1WKLI/aQ8sYEGBN1La6F1CG5z1wpTKioGSKjYsx1PCbWnauJEwzVCLAmYjUisKiLC7Bjcjw/yfnOL6BKXKygTCxE6jzCs1V5uIcRG397cjR/Y2F84g8YJk77l6FzuiB6DbBw4b7prBuI35yi6pSWAnkHrkq8FIpWfbDNJF+FIK63M39tmk3eDeRb/yZs8mCSNJgtvP2Yx7ipCDJLhmBbApNiZ+L/YYV3P838pwAu+KZ4CHJNnlqLyA1Rx3b53BP2QYWn0DdLHB7cJ08sKJE1X0Vop+yvo1KCu8xU1BwSMJewLhq1yKsVIx3D6FWF93THhhJyRlQ1l+FrREzpwNcfTwf8H624/7AMgbZVKZzrnDS9R9DtfjvITsEU0FuoMEKt/A421B2vlcFgfIsyJiDof5HhEFLZoTWmfWqSLEHy27oGxD0945s4RQt5Dr/SsP1GDkKFJsViiukcfRz/nBbBXAIHwjKgTT1DVZ4u2ckQGZi6So8bhXqXPoTw=="
      + tags            = {
          + "description" = "terraform key pair import"
        }
      + tags_all        = {
          + "description" = "terraform key pair import"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take
exactly these actions if you run "terraform apply" now.
```

```bash
$ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions
are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_key_pair.terraform-key-pair will be created
  + resource "aws_key_pair" "terraform-key-pair" {
      + arn             = (known after apply)
      + fingerprint     = (known after apply)
      + id              = (known after apply)
      + key_name        = "tf-key-pair"
      + key_name_prefix = (known after apply)
      + key_pair_id     = (known after apply)
      + key_type        = (known after apply)
      + public_key      = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMacksku1OXpLErjjTS7N11jtt0Wf/+dHo21OcwJ3YTOQ9wlcnKFPphUQgu8G7SZL+73NjG/fhxShBbAY3MVn8sj2mMIB0vZOXWEpRMzNLOOMuOkvcSOR675b6qRVEm8LG/oYIeC45+H2TgbY78BKoPGqhhgwUEDd9/qcgtUHN/pLK2fe1Io1WKLI/aQ8sYEGBN1La6F1CG5z1wpTKioGSKjYsx1PCbWnauJEwzVCLAmYjUisKiLC7Bjcjw/yfnOL6BKXKygTCxE6jzCs1V5uIcRG397cjR/Y2F84g8YJk77l6FzuiB6DbBw4b7prBuI35yi6pSWAnkHrkq8FIpWfbDNJF+FIK63M39tmk3eDeRb/yZs8mCSNJgtvP2Yx7ipCDJLhmBbApNiZ+L/YYV3P838pwAu+KZ4CHJNnlqLyA1Rx3b53BP2QYWn0DdLHB7cJ08sKJE1X0Vop+yvo1KCu8xU1BwSMJewLhq1yKsVIx3D6FWF93THhhJyRlQ1l+FrREzpwNcfTwf8H624/7AMgbZVKZzrnDS9R9DtfjvITsEU0FuoMEKt/A421B2vlcFgfIsyJiDof5HhEFLZoTWmfWqSLEHy27oGxD0945s4RQt5Dr/SsP1GDkKFJsViiukcfRz/nBbBXAIHwjKgTT1DVZ4u2ckQGZi6So8bhXqXPoTw=="
      + tags            = {
          + "description" = "terraform key pair import"
        }
      + tags_all        = {
          + "description" = "terraform key pair import"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_key_pair.terraform-key-pair: Creating...
aws_key_pair.terraform-key-pair: Creation complete after 0s [id=tf-key-pair]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

- aws EC2 쪽에서 생성 확인 가능

![Image](https://i.imgur.com/dZzOLiw.png)
