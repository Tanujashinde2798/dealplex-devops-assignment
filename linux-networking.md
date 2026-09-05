# Linux and Networking Documentation

## 1. Overview

This document explains the basic Linux and networking commands and concepts used when operating the DevOps Assignment application.

The application runs on port `5000` and can run locally, inside Docker, and inside Kubernetes.

---

## 2. CPU Usage

To check CPU information:

```bash
lscpu
```

To monitor CPU and running processes:

```bash
top
```

A more detailed interactive process monitor can be used with:

```bash
htop
```

if it is installed.

These commands help identify high CPU usage and resource-consuming processes.

---

## 3. Memory Usage

To check memory usage:

```bash
free -h
```

Example information includes:

* Total memory
* Used memory
* Available memory
* Swap memory

The `-h` option displays the values in a human-readable format.

---

## 4. Disk Usage

To check available disk space:

```bash
df -h
```

To check the size of files and directories:

```bash
du -sh <directory>
```

These commands help identify disk-space problems.

---

## 5. Running Processes

To display running processes:

```bash
ps aux
```

To find a specific process:

```bash
ps aux | grep python
```

For continuously monitoring processes:

```bash
top
```

---

## 6. Listening Ports

To check listening network ports:

```bash
ss -tuln
```

To check which process is using a particular port:

```bash
sudo ss -tulpn
```

For this application, port `5000` is the application port.

---

## 7. Network Interfaces

To display network interfaces and IP addresses:

```bash
ip addr
```

A shorter command is:

```bash
ip a
```

These commands show interfaces such as Ethernet, Wi-Fi, loopback, and their assigned IP addresses.

---

## 8. Network Routes

To view the routing table:

```bash
ip route
```

The routing table shows how traffic is routed from the system to different networks.

---

## 9. Application Logs

For a Flask application running directly from the terminal, application logs are displayed in the terminal.

For Docker:

```bash
docker logs devops-app
```

To follow logs continuously:

```bash
docker logs -f devops-app
```

For Kubernetes:

```bash
kubectl logs <pod-name>
```

To follow Kubernetes logs:

```bash
kubectl logs -f <pod-name>
```

Logs are useful for troubleshooting application errors and connectivity problems.

---

## 10. 127.0.0.1 vs 0.0.0.0

### 127.0.0.1

`127.0.0.1` is the loopback address.

An application listening only on:

```text
127.0.0.1
```

accepts connections from the same machine.

It generally cannot be accessed through the machine's external network interface.

### 0.0.0.0

`0.0.0.0` means the application listens on all available network interfaces.

This project uses:

```python
app.run(host="0.0.0.0", port=5000)
```

This is important when running the application inside Docker or Kubernetes because the application must accept connections coming through the container or pod network.

---

## 11. Public IP vs Private IP

### Private IP

A private IP is used inside a private network.

Common private IPv4 ranges include:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Private IP addresses are commonly used for communication between systems inside a VPC or local network.

### Public IP

A public IP can be reachable over the Internet when the appropriate routing and security rules allow it.

For an AWS EC2 application, a public IP can be used for Internet access if the EC2 instance is placed in an appropriate network configuration and its Security Group permits the required traffic.

---

## 12. Host Port vs Container Port

Docker can map a host port to a container port.

Example:

```bash
docker run -d -p 5000:5000 devops-assignment
```

The format is:

```text
HOST_PORT:CONTAINER_PORT
```

Therefore:

```text
5000:5000
```

means:

```text
Host port 5000
        |
        v
Container port 5000
```

The Flask application listens on container port `5000`.

---

## 13. Basic TCP Concepts

TCP is a connection-oriented transport protocol.

It provides:

* Reliable data delivery
* Ordered data transmission
* Error checking
* Connection management

Applications commonly use TCP for protocols such as HTTP and HTTPS.

---

## 14. Basic HTTP Concepts

HTTP is an application-layer protocol used for communication between clients and web servers.

This project uses HTTP endpoints:

```text
GET /
GET /health
```

The browser acts as the client and sends an HTTP request to the Flask application.

The application sends an HTTP response.

For example:

```text
GET /health
```

returns:

```text
Healthy
```

with a successful HTTP status code.

---

## 15. AWS Security Groups

An AWS Security Group acts as a virtual firewall for AWS resources such as EC2 instances.

Security Groups control inbound and outbound traffic.

For example, an EC2-based deployment could allow:

```text
SSH    TCP 22
HTTP   TCP 80
HTTPS  TCP 443
```

Only required ports should be opened.

SSH should preferably be restricted to trusted IP addresses instead of allowing access from everywhere.

---

## 16. Application Networking Flow

For this project, the basic networking flow is:

```text
Browser
   |
   v
Host Port
   |
   v
Docker / Kubernetes
   |
   v
Application Port 5000
   |
   v
Flask Application
```

For AWS EC2, the flow could be:

```text
Internet
   |
   v
Public IP / Load Balancer
   |
   v
Security Group
   |
   v
EC2 Instance
   |
   v
Docker Container
   |
   v
Flask Application :5000
```

---

## 17. Useful Troubleshooting Commands

Check the local IP:

```bash
ip addr
```

Check routes:

```bash
ip route
```

Check listening ports:

```bash
ss -tuln
```

Test HTTP connectivity:

```bash
curl http://localhost:5000
```

Check Docker containers:

```bash
docker ps
```

Check Docker logs:

```bash
docker logs devops-app
```

Check Kubernetes pods:

```bash
kubectl get pods
```

Check Kubernetes services:

```bash
kubectl get services
```

Check Kubernetes logs:

```bash
kubectl logs <pod-name>
```

---

## 18. Conclusion

These Linux and networking commands provide the basic operational knowledge required to monitor resources, inspect processes, troubleshoot ports and networking, and investigate application logs.

