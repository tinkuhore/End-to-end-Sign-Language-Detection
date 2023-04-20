# End-to-end-Sign-Language-Detection

steps to follow
1. constants
2. entity
3. components
4. pipelines
5. app.py

# CIFAR-10 CLASSIFIER

Create a Web Application using Flask. Use the end user should be able
to upload an image and get results with the prediction score.

## How to Run

1. create virtual environment using following command
	```
	python -m venv <venv_name>
	```
2. Activate virtual environment using following command

	On Windows, run the following command:
	```
	venv\Scripts\activate.bat
	```

	On Linux or macOS, run the following command:
	```
	source venv/bin/activate
	```
3. ```
	pip install -r requirements.txt
	```
4. ```
	python app.py
	```
5. open in browser: http://localhost:8080/


#
#


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

    3. AmazonS3FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 284644521468.dkr.ecr.us-east-1.amazonaws.com/sign-lang

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade 
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 284644521468.dkr.ecr.us-east-1.amazonaws.com

    ECR_REPOSITORY_NAME = sign-lang