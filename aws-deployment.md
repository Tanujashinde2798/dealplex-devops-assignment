# AWS Deployment Approach

## 1. Overview

This document explains how the Dockerized DevOps Assignment application could be deployed to AWS.

An actual AWS account is not required for this assignment. The following describes the implementation approach.

For this project, the selected AWS runtime is:

**Amazon EC2 + Docker**

EC2 is selected because it provides a simple way to demonstrate how a Docker image can be pulled from Amazon ECR and run on an AWS virtual machine.

---

# 2. AWS Architecture

```text
                     Developer
                         |
                         v
                       GitHub
                         |
                         v
                  GitHub Actions
                         |
                  Test + Docker Build
                         |
                         v
                  Amazon ECR
                         |
                    Docker Image
                         |
                         v
                 AWS EC2 Instance
                         |
                  Docker Container
                         |
                         v
                 Flask Application
                         |
                         v
              Public IP / Load Balancer
                         |
                         v
                       User
```

---

# 3. Selected AWS Runtime: EC2 + Docker

The application can be deployed to an Amazon EC2 instance.

The basic process would be:

1. Launch an EC2 instance.
2. Install Docker on the EC2 instance.
3. Configure IAM permissions.
4. Authenticate the EC2 instance with Amazon ECR.
5. Pull the Docker image from ECR.
6. Run the Docker container.
7. Configure networking and Security Groups.
8. Access the application through the appropriate public endpoint.

This approach is simple and suitable for demonstrating the basic AWS deployment flow.

---

# 4. GitHub to Amazon ECR

The CI/CD flow would be:

```text
GitHub
   |
   v
GitHub Actions
   |
   v
Run Tests
   |
   v
Build Docker Image
   |
   v
Authenticate to Amazon ECR
   |
   v
Push Docker Image
   |
   v
Amazon ECR
```

GitHub Actions can build the Docker image and push it to an Amazon ECR repository.

Example image:

```text
<account-id>.dkr.ecr.<region>.amazonaws.com/devops-assignment:latest
```

The actual AWS credentials should never be hardcoded in the repository.

GitHub Actions secrets or an appropriate AWS identity federation mechanism should be used for authentication.

---

# 5. Amazon ECR

Amazon Elastic Container Registry (ECR) is used to store Docker container images.

The application image would be pushed to an ECR repository such as:

```text
devops-assignment
```

The EC2 instance can then authenticate to ECR and pull the required image.

Example command:

```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
```

The image can then be pulled using:

```bash
docker pull <account-id>.dkr.ecr.<region>.amazonaws.com/devops-assignment:latest
```

---

# 6. Deploying the Image on EC2

After pulling the image onto EC2, the container can be started using:

```bash
docker run -d \
  -p 5000:5000 \
  -e APP_ENV=production \
  --name devops-app \
  <account-id>.dkr.ecr.<region>.amazonaws.com/devops-assignment:latest
```

The application would then listen on port `5000` inside the container.

A production setup could place a reverse proxy or Load Balancer in front of the application.

---

# 7. IAM

AWS IAM controls access to AWS resources.

For this architecture, IAM can be used to provide the EC2 instance permission to pull container images from ECR.

The principle of least privilege should be followed.

Only the permissions required for the application should be granted.

AWS credentials should not be stored inside the source code.

---

# 8. VPC and Networking

The EC2 instance runs inside an AWS VPC.

A basic architecture could contain:

```text
VPC
 |
 +-- Public Subnet
       |
       +-- EC2 Instance
```

The VPC provides network isolation and routing.

For a production architecture, private subnets, NAT Gateway, Load Balancers, and multiple Availability Zones could be considered.

---

# 9. Security Groups

A Security Group acts as a virtual firewall for the EC2 instance.

Example inbound rules:

```text
SSH   TCP   22    Restricted administrator IP
HTTP  TCP   80    Required application access
HTTPS TCP   443   Required secure application access
```

If the application is accessed directly on port 5000, port 5000 would also need to be allowed.

However, exposing port 5000 directly to the Internet is generally less desirable than using a Load Balancer or reverse proxy on ports 80/443.

Only required ports should be opened.

---

# 10. Application Access

There are two basic options.

### Option 1: EC2 Public IP

The application can be accessed through the EC2 public IP if the Security Group and networking configuration permit access.

Example:

```text
http://<EC2-Public-IP>:5000
```

### Option 2: Load Balancer

A more scalable approach is:

```text
Internet
   |
   v
Application Load Balancer
   |
   v
EC2 Instance
   |
   v
Docker Container
   |
   v
Flask Application
```

The Load Balancer can provide a stable application endpoint and distribute traffic to application instances.

---

# 11. CloudWatch and Logging

Application and infrastructure monitoring can be implemented using Amazon CloudWatch.

CloudWatch can be used for:

* EC2 monitoring
* CPU utilization
* System metrics
* Application logs
* Alerts
* Operational monitoring

Docker logs can be collected and forwarded to an appropriate logging solution.

Example local Docker command:

```bash
docker logs devops-app
```

---

# 12. Complete AWS Deployment Flow

The complete flow is:

```text
Developer
    |
    v
GitHub
    |
    v
GitHub Actions
    |
    +----> Run Tests
    |
    +----> Build Docker Image
    |
    v
Amazon ECR
    |
    v
EC2 Instance
    |
    +----> IAM
    |
    +----> VPC
    |
    +----> Security Group
    |
    v
Docker
    |
    v
Flask Application
    |
    v
Application Access
```

---

# 13. Security Considerations

The following practices should be followed:

* Never commit AWS access keys.
* Never commit passwords or private keys.
* Use IAM with least-privilege permissions.
* Restrict SSH access.
* Open only required ports.
* Use HTTPS for production applications.
* Keep the EC2 operating system and Docker updated.
* Store sensitive configuration in appropriate secret-management services.
* Use CloudWatch for monitoring and logging.

---

# 14. Why EC2 + Docker Was Selected

EC2 + Docker was selected because it provides a straightforward deployment model.

The existing Docker image can be reused without changing the application significantly.

The deployment process is:

```text
Build Image
     |
     v
Push to ECR
     |
     v
Pull Image on EC2
     |
     v
Run Docker Container
```

This makes it easy to understand the relationship between GitHub Actions, Docker, ECR, EC2, networking, IAM, and application access.

---

# 15. Conclusion

Although an actual AWS deployment was not performed for this assignment, the documented approach demonstrates how the existing Dockerized application can be moved to AWS using Amazon ECR and EC2.

The proposed architecture covers CI/CD, container image storage, IAM, VPC networking, Security Groups, application access, and CloudWatch monitoring.

