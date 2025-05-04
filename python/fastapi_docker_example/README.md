# 🚀 fastapi_docker_example

A minimal and beginner-friendly example of how to containerize a FastAPI application using **Docker** and **Docker Compose**. This repository is part of a 5-part series on Docker basics, and is aimed at developers who want to learn the essentials of containerizing Python web apps.

## 📂 Project Structure

```

fastapi_docker_example/
├── app
│   └── main.py
├── __init__.py
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt

````

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/lavvsharma/linkedin_post_examples.git
cd python/fastapi_docker_example
````

### 2. Run the App with Docker Compose

```bash
docker-compose up --build
```

After the build completes, your app will be available at:

📍 [http://localhost:8000](http://localhost:8000)

You should see:

```json
{"message": "Dockerized FastAPI app is running!"}
```

## 🧪 API Endpoint

| Method | URL | Description               |
| ------ | --- | ------------------------- |
| GET    | `/` | Returns a welcome message |

## 🐳 Key Concepts Covered

* Dockerfile for a Python (FastAPI) project
* Using Docker Compose to simplify setup
* Isolated and reproducible development environment
* Containerized app running on `0.0.0.0:8000`

## 📘 Part of a Series

This repository is part of a 5-part series on Docker:

1. ✅ [What is Docker, and Why You Should Know](#)
2. ✅ [Basic Terminology of Docker](#)
3. ✅ **[Build a Sample FastAPI App with Docker](#)** ← You are here
4. 🔜 Docker Networking & Volumes
5. 🔜 Deploying a Dockerized App to the Cloud

## 🙌 Contribution

Feel free to fork, use, and improve this template. PRs and suggestions are welcome!
