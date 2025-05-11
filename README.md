# 💼 LinkedIn Post Examples

This repository contains hands-on code examples that accompany my LinkedIn technical posts. The goal is to provide developers with **practical, real-world code snippets and mini-projects** that demonstrate concepts I write about in short form on LinkedIn.

Each folder is dedicated to a specific post or series, with step-by-step code to help you follow along more deeply.

## 📁 Structure

```
linkedin_post_examples/
└── python/
    ├── fastapi_docker_example/
    └── fastapi_postgres_docker_example/
```

## 🚀 Featured Examples

### 🔹 [`fastapi_docker_example`](./python/fastapi_docker_example)

A **minimal Dockerized FastAPI app** demonstrating how to:

- Build a simple FastAPI application
- Containerize it using Docker
- Use Docker Compose to manage the service
- Access the app at `http://localhost:8000`

📌 Part of my **5-part Docker series** — ideal for beginners looking to get hands-on with containerizing Python apps.

### 🔹 [`fastapi_postgres_docker_example`](./python/fastapi_postgres_docker_example)

An extended version of the above app that integrates a **PostgreSQL database using Docker Compose**. This example shows how to:

- Add a database service to your container network
- Connect FastAPI to PostgreSQL using SQLAlchemy
- Use Docker volumes to persist DB data
- Build a real-world, multi-container app setup

🔄 Includes a `/ping-db` endpoint to verify database connection.

## 📌 Why This Repo Exists

I use LinkedIn to share concise technical posts, but sometimes code examples need a bit more space and structure. This repository serves as a home for that **extra context and working code**.

If you're following my posts and want to go deeper—this is the place!

## 🛠️ Upcoming Examples

- Docker Networking & Volumes (already demonstrated in `fastapi_postgres_docker_example`)
- Deploying Docker Apps to the Cloud
- Local LLM setups & Vector DBs
- Python automation utilities
- Microservice-based FastAPI projects

## 🙌 Contributions & Feedback

Spotted something off? Got an idea for another example?  
Feel free to open an issue or a pull request — always open to feedback and collaboration!

## 📄 License

All content in this repository is available under the MIT License.