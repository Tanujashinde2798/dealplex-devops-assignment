# DevOps Candidate Assignment

## 1. Project Overview

This project demonstrates a basic DevOps workflow using a Python Flask web application.

The application is containerized using Docker, tested using Pytest, integrated with GitHub, automatically tested and Docker-built using GitHub Actions, and deployed locally on Kubernetes using Kind.

### DevOps Workflow

```text
Developer
    |
    v
Python Flask Application
    |
    v
Git
    |
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +----> Install Dependencies
    |
    +----> Run Pytest
    |
    +----> Build Docker Image
    |
    v
Docker
    |
    v
Kubernetes / Kind
    |
    +----> Deployment
    |
    +----> 2 Pods
    |
    +----> Service
    |
    v
Running Web Application
```

---

# 2. Technologies Used

* Python 3.12
* Flask
* Pytest
* Git
* GitHub
* GitHub Actions
* Docker
* Kubernetes
* Kind
* kubectl
* WSL2 Ubuntu
* Windows PowerShell

---

# 3. Project Structure

```text
devops-assignment/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   └── requirements.txt
│
├── tests/
│   └── test_app.py
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

---

# 4. Application

The application is a simple Flask web application.

## Application Endpoints

### Home

```text
GET /
```

Response:

```text
DevOps Assignment App is running
```

### Health Check

```text
GET /health
```

Response:

```text
Healthy
```

The `/health` endpoint can be used to check whether the application is running correctly.

---

# 5. Run the Application Locally

## Step 1: Go to the project directory

```bash
cd /mnt/c/Users/acer/Desktop/devops-assignment
```

## Step 2: Activate the Python virtual environment

```bash
source ~/devops-venv/bin/activate
```

## Step 3: Install dependencies

```bash
pip install -r app/requirements.txt
```

Install Pytest:

```bash
pip install pytest
```

## Step 4: Start the Flask application

```bash
python app/app.py
```

The application runs on:

```text
http://localhost:5000
```

Test the application in a browser:

```text
http://localhost:5000
```

Test the health endpoint:

```text
http://localhost:5000/health
```

Press:

```text
Ctrl + C
```

to stop the Flask server.

---

# 6. Run Tests

From the project root:

```bash
pytest
```

Expected result:

```text
2 passed
```

The tests verify:

* Home endpoint returns HTTP 200
* Health endpoint returns HTTP 200

---

# 7. Docker

## Dockerfile

The Dockerfile uses the Python 3.12 slim image.

It:

1. Creates a working directory
2. Copies the application files
3. Installs Flask
4. Exposes port 5000
5. Starts the Flask application

## Check Docker

```bash
docker --version
```

Check that Docker is running:

```bash
docker info
```

---

# 8. Build Docker Image

From the project root:

```bash
docker build -t devops-assignment:latest .
```

Check the image:

```bash
docker images
```

You should see:

```text
devops-assignment
```

---

# 9. Run Docker Container

Run the container:

```bash
docker run -d -p 5000:5000 -e APP_ENV=production --name devops-app devops-assignment
```

Explanation:

* `-d` = run container in background
* `-p 5000:5000` = map host port 5000 to container port 5000
* `-e APP_ENV=production` = set environment variable
* `--name devops-app` = give the container a name
* `devops-assignment` = Docker image name

Check running containers:

```bash
docker ps
```

Test the application:

```text
http://localhost:5000
```

Test health:

```text
http://localhost:5000/health
```

---

# 10. Check Environment Variable

The application uses the `APP_ENV` environment variable.

Check it inside the container:

```bash
docker exec devops-app printenv APP_ENV
```

Expected:

```text
production
```

---

# 11. Docker Container Management Commands

Stop the container:

```bash
docker stop devops-app
```

Start it again:

```bash
docker start devops-app
```

Remove the container:

```bash
docker rm -f devops-app
```

List all containers:

```bash
docker ps -a
```

List Docker images:

```bash
docker images
```

---

# 12. Git Configuration

Check Git version:

```bash
git --version
```

Configure username:

```bash
git config --global user.name "Tanujashinde2798"
```

Configure email:

```bash
git config --global user.email "tanujashinde127@gmail.com"
```

Check configuration:

```bash
git config --global --list
```

---

# 13. Git Repository

Initialize Git if required:

```bash
git init
```

Check repository status:

```bash
git status
```

Add all project files:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Initial DevOps assignment setup"
```

Check commit history:

```bash
git log --oneline
```

Show the latest five commits:

```bash
git log --oneline -5
```

---

# 14. GitHub Remote Repository

Check the configured remote:

```bash
git remote -v
```

Expected repository:

```text
https://github.com/Tanujashinde2798/dealplex-devops-assignment.git
```

If the remote does not exist:

```bash
git remote add origin https://github.com/Tanujashinde2798/dealplex-devops-assignment.git
```

Rename the branch to main:

```bash
git branch -M main
```

Push the project:

```bash
git push -u origin main
```

For future changes:

```bash
git add .
git commit -m "Update project"
git push origin main
```

---

# 15. GitHub Actions CI Pipeline

The project contains:

```text
.github/workflows/ci.yml
```

The CI pipeline automatically runs when code is pushed to the `main` branch or when a pull request is created.

## CI Pipeline Steps

```text
GitHub Push
     |
     v
Checkout Code
     |
     v
Setup Python 3.12
     |
     v
Install Dependencies
     |
     v
Run Pytest
     |
     v
Build Docker Image
```

## Pipeline Commands

Install Python dependencies:

```bash
pip install -r app/requirements.txt
```

Install Pytest:

```bash
pip install pytest
```

Run tests:

```bash
pytest
```

Build Docker image:

```bash
docker build -t devops-assignment:latest .
```

These commands are automatically executed by GitHub Actions.

---

# 16. Kubernetes

Kubernetes is used to deploy and manage the Dockerized application.

Kind is used to create a local Kubernetes cluster.

## Check kubectl

```bash
kubectl version --client
```

## Check Kind

```bash
kind version
```

---

# 17. Create Kind Kubernetes Cluster

Create the cluster:

```bash
kind create cluster --name devops-cluster
```

Check the cluster:

```bash
kubectl get nodes
```

Expected result:

```text
devops-cluster-control-plane   Ready
```

Check the current Kubernetes context:

```bash
kubectl config current-context
```

Expected:

```text
kind-devops-cluster
```

---

# 18. Load Docker Image into Kind

The Docker image must be available inside the Kind cluster.

Load the image:

```bash
kind load docker-image devops-assignment:latest --name devops-cluster
```

---

# 19. Kubernetes Deployment

The deployment file is:

```text
k8s/deployment.yaml
```

Apply the deployment:

```bash
kubectl apply -f k8s/deployment.yaml
```

Check deployments:

```bash
kubectl get deployments
```

Expected:

```text
devops-app   2/2
```

The deployment is configured with:

```text
replicas: 2
```

Therefore, Kubernetes runs two application pods.

---

# 20. Check Kubernetes Pods

Run:

```bash
kubectl get pods
```

Expected:

```text
devops-app-xxxxx   1/1   Running
devops-app-yyyyy   1/1   Running
```

The two pods provide application instances managed by Kubernetes.

For more detailed information:

```bash
kubectl get pods -o wide
```

---

# 21. Kubernetes Service

The service file is:

```text
k8s/service.yaml
```

Apply the service:

```bash
kubectl apply -f k8s/service.yaml
```

Check services:

```bash
kubectl get services
```

The application service is:

```text
devops-app-service
```

The service exposes port:

```text
5000
```

The service type is:

```text
NodePort
```

---

# 22. Access Kubernetes Application

Port forwarding can be used to access the Kubernetes service from the local computer.

Run:

```bash
kubectl port-forward service/devops-app-service 8080:5000
```

Keep this terminal running.

Open the application in the browser:

```text
http://localhost:8080
```

Health endpoint:

```text
http://localhost:8080/health
```

Expected responses:

```text
DevOps Assignment App is running
```

and:

```text
Healthy
```

Stop port forwarding with:

```text
Ctrl + C
```

---

# 23. Kubernetes Troubleshooting Commands

Check pods:

```bash
kubectl get pods
```

Check deployments:

```bash
kubectl get deployments
```

Check services:

```bash
kubectl get services
```

Check pod details:

```bash
kubectl describe pod <pod-name>
```

Check application logs:

```bash
kubectl logs <pod-name>
```

Check deployment details:

```bash
kubectl describe deployment devops-app
```

---

# 24. Kubernetes Cleanup

Delete the application deployment:

```bash
kubectl delete -f k8s/deployment.yaml
```

Delete the service:

```bash
kubectl delete -f k8s/service.yaml
```

Delete the complete Kind cluster:

```bash
kind delete cluster --name devops-cluster
```

---

# 25. Complete DevOps Command Flow

The main workflow used in this project is:

## Application

```bash
cd /mnt/c/Users/acer/Desktop/devops-assignment
source ~/devops-venv/bin/activate
pip install -r app/requirements.txt
pip install pytest
pytest
```

## Docker

```bash
docker build -t devops-assignment:latest .
docker run -d -p 5000:5000 -e APP_ENV=production --name devops-app devops-assignment
docker ps
```

## Git

```bash
git status
git add .
git commit -m "Update project"
git push origin main
```

## Kubernetes

```bash
kind create cluster --name devops-cluster
kind load docker-image devops-assignment:latest --name devops-cluster
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get deployments
kubectl get pods
kubectl get services
kubectl port-forward service/devops-app-service 8080:5000
```

---

# 26. Final DevOps Architecture

```text
                Developer
                    |
                    v
             Python Flask App
                    |
                    v
                  Git
                    |
                    v
                 GitHub
                    |
                    v
          GitHub Actions CI
                    |
          +---------+---------+
          |                   |
          v                   v
       Pytest           Docker Build
                              |
                              v
                       Docker Image
                              |
                              v
                       Kind Cluster
                              |
                     Kubernetes Deployment
                              |
                  +-----------+-----------+
                  |                       |
                  v                       v
                Pod 1                   Pod 2
                  |                       |
                  +-----------+-----------+
                              |
                              v
                     Kubernetes Service
                              |
                              v
                     Flask Application
```

---

# 27. What This Project Demonstrates

This project demonstrates practical knowledge of:

* Python Flask application development
* Linux/WSL environment
* Git version control
* GitHub repository management
* Automated CI using GitHub Actions
* Automated testing using Pytest
* Docker image creation
* Docker container execution
* Environment variables
* Kubernetes Deployment
* Kubernetes Pods
* Kubernetes Services
* Local Kubernetes using Kind
* Application health checking
* Basic DevOps automation workflow

---

# 28. Conclusion

The project demonstrates a basic end-to-end DevOps workflow where application code is developed, tested, version-controlled, automatically tested through GitHub Actions, containerized using Docker, and deployed on Kubernetes using Kind.

The implementation focuses on demonstrating the core DevOps concepts in a simple and practical way.

AWS deployment was not included in the final implementation because it was optional for this assignment. The Kubernetes deployment was performed locally using Kind.
