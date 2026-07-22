# 📝 Todo App - Docker + Flask + AWS

A simple, beautiful Todo application built with Flask and Docker, ready to deploy on AWS EC2.

## 🎯 Project Overview

This is a **full-stack todo application** that demonstrates:
- ✅ Docker containerization
- ✅ Flask backend (Python)
- ✅ Modern HTML/CSS frontend
- ✅ AWS EC2 deployment
- ✅ Responsive design

**Skills Demonstrated:**
- Docker (containerization)
- Flask (Python web framework)
- AWS EC2 (cloud deployment)
- Frontend development (HTML, CSS, JavaScript)
- REST API design

---

## 📁 Project Structure

```
todo-app/
├── app.py                 # Flask application (backend)
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose for local testing
├── templates/
│   └── index.html       # Frontend (HTML/CSS/JS)
└── README.md            # This file
```

---

## 🚀 Quick Start (Local Testing)

### Option 1: Run with Docker Compose (EASIEST)

```bash
# Clone or download this project
cd todo-app

# Build and run with Docker Compose
docker-compose up

# Open browser and go to: http://localhost:5000
# That's it!

# Stop the app
docker-compose down
```

### Option 2: Run with Docker

```bash
# Build the Docker image
docker build -t todo-app:latest .

# Run the container
docker run -p 5000:5000 todo-app:latest

# Open browser: http://localhost:5000

# Stop the container
docker stop <container_id>
```

### Option 3: Run Without Docker (Python Only)

```bash
# Install dependencies
pip install -r requirements.txt

# Create templates folder and move index.html there
mkdir templates
mv index.html templates/

# Run the app
python app.py

# Open browser: http://localhost:5000
```

---

## ✨ Features

- ✅ **Add Todos** - Add new tasks with a single click
- ✅ **Complete Todos** - Mark tasks as done
- ✅ **Delete Todos** - Remove completed tasks
- ✅ **Stats Dashboard** - See total, completed, and remaining tasks
- ✅ **Persistent Storage** - Data saved to JSON file
- ✅ **Beautiful UI** - Modern gradient design
- ✅ **Responsive** - Works on mobile, tablet, desktop
- ✅ **Error Handling** - User-friendly error messages

---

## 🔧 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | View all todos |
| GET | `/api/todos` | Get todos as JSON |
| POST | `/add` | Add new todo |
| DELETE | `/delete/<id>` | Delete a todo |
| PUT | `/toggle/<id>` | Mark todo as complete/incomplete |
| GET | `/health` | Health check (for load balancers) |

---

## 🌐 Deploy to AWS EC2

### Step 1: Create an EC2 Instance

1. Go to [AWS Console](https://console.aws.amazon.com)
2. Search for **EC2** and click **Launch Instance**
3. Choose:
   - **AMI**: Ubuntu 22.04 LTS (Free tier eligible)
   - **Instance Type**: t2.micro (Free tier)
   - **Storage**: 20 GB (Free tier)
4. **Security Group**: Allow traffic on:
   - Port 22 (SSH)
   - Port 5000 (Our app)
   - Port 80 (HTTP)
5. Create/use a **key pair** (download .pem file)
6. Click **Launch Instance**

### Step 2: Connect to EC2 via SSH

```bash
# Change permission on your key file
chmod 400 your-key.pem

# SSH into your instance
ssh -i your-key.pem ubuntu@your-ec2-public-ip

# Example: ssh -i my-key.pem ubuntu@54.123.45.67
```

### Step 3: Install Docker on EC2

```bash
# Update system
sudo apt update
sudo apt upgrade -y

# Install Docker
sudo apt install docker.io -y

# Add ubuntu user to docker group (so you don't need sudo)
sudo usermod -aG docker ubuntu

# Logout and login again to apply group changes
exit
# SSH back in
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

### Step 4: Clone Your Project

```bash
# Clone your GitHub repository (or upload files manually)
git clone https://github.com/YOUR_USERNAME/todo-app.git
cd todo-app
```

**If you don't have a GitHub repo yet**, upload files via SCP:
```bash
# From your local machine
scp -i your-key.pem -r /path/to/todo-app ubuntu@your-ec2-ip:/home/ubuntu/
```

### Step 5: Push Docker Image to DockerHub (Optional but Recommended)

```bash
# Build your Docker image
docker build -t YOUR_DOCKERHUB_USERNAME/todo-app:latest .

# Login to DockerHub
docker login

# Push image to DockerHub
docker push YOUR_DOCKERHUB_USERNAME/todo-app:latest
```

### Step 6: Run the App on EC2

```bash
# Pull from DockerHub (if you pushed)
docker pull YOUR_DOCKERHUB_USERNAME/todo-app:latest

# OR build locally
docker build -t todo-app:latest .

# Run the container
docker run -d -p 5000:5000 --name todo-app todo-app:latest

# Verify it's running
docker ps

# Check logs
docker logs todo-app
```

### Step 7: Access Your App

Open your browser and go to:
```
http://your-ec2-public-ip:5000
```

Example: `http://54.123.45.67:5000`

---

## 🛠️ Useful Commands

### Docker Commands

```bash
# Build image
docker build -t todo-app:latest .

# Run container
docker run -p 5000:5000 todo-app:latest

# Run in background
docker run -d -p 5000:5000 --name todo-app todo-app:latest

# View running containers
docker ps

# View all containers
docker ps -a

# Stop container
docker stop <container_id>

# View logs
docker logs <container_id>

# Remove container
docker rm <container_id>

# Remove image
docker rmi todo-app:latest
```

### EC2 Commands

```bash
# Check if app is running
curl http://localhost:5000/health

# View running processes
ps aux | grep python

# Stop the app
docker stop todo-app

# Restart the app
docker restart todo-app
```

## 🎓 What You Learned

By building this project, you've learned:

1. **Docker Basics**
   - Creating Dockerfile
   - Building images
   - Running containers
   - Port mapping

2. **Flask Backend**
   - Route handling
   - JSON API endpoints
   - File-based storage
   - Request/Response handling

3. **Frontend Development**
   - HTML structure
   - CSS styling and gradients
   - JavaScript fetch API
   - DOM manipulation
   - Responsive design

4. **AWS EC2**
   - Instance creation
   - Security groups
   - SSH connection
   - Deploying containerized apps

5. **DevOps Concepts**
   - Containerization
   - Infrastructure
   - Deployment
   - Monitoring (health checks)

---

## 🐛 Troubleshooting

### App not accessible from browser

```bash
# Check if container is running
docker ps

# Check logs for errors
docker logs todo-app

# Make sure port 5000 is open in AWS Security Group
```

### Docker connection refused

```bash
# Restart Docker
sudo service docker restart

# Or use these commands on your container
docker stop todo-app
docker rm todo-app
docker run -d -p 5000:5000 --name todo-app todo-app:latest
```

### Can't SSH into EC2

```bash
# Check key permission (should be 400)
ls -l your-key.pem

# Fix if needed
chmod 400 your-key.pem

# Check security group allows SSH on port 22
```

### Data lost when container restarts

```bash
# Add volume to persist data
docker run -d -p 5000:5000 -v /home/ubuntu/data:/app/data --name todo-app todo-app:latest
```

---

## 📈 Next Steps / Enhancements

Want to make this project more advanced?

1. **Add Database** (MySQL/PostgreSQL) instead of JSON
2. **User Authentication** - Login/signup
3. **Categories/Tags** - Organize todos
4. **Notifications** - Email reminders
5. **CI/CD Pipeline** - GitHub Actions for auto-deployment
6. **Load Balancer** - Multiple EC2 instances
7. **AWS RDS** - Managed database
8. **AWS S3** - Store data in S3 bucket