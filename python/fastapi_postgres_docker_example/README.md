# 🐳 FastAPI + PostgreSQL Docker Example

This project is part of the [LinkedIn Docker Series](https://www.linkedin.com/in/lavsharmaa/) and shows how to build a **multi-container FastAPI + PostgreSQL application using Docker Compose**.

It is the **natural next step** after a basic Dockerized FastAPI setup — this example demonstrates how to add a database service, connect it with FastAPI using SQLAlchemy, and manage everything via Docker Compose.

## 🔧 What’s Inside?

This mini-project includes:

- A FastAPI app with two endpoints (`/` and `/ping-db`)
- SQLAlchemy-based PostgreSQL database connection
- Dockerfile to build the FastAPI image
- Docker Compose to run both app and DB together
- Persistent storage using Docker Volumes

## 🗂 Folder Structure

```
fastapi_postgres_docker_example/
├── app/
│   ├── main.py          # FastAPI entry point
│   └── database.py      # DB connection setup using SQLAlchemy
├── Dockerfile           # FastAPI container build config
├── requirements.txt     # Python dependencies
└── docker-compose.yml   # Defines both FastAPI and PostgreSQL services
````

## 🚀 How to Run

1. **Clone the repo**

```bash
git clone https://github.com/lavvsharma/linkedin_post_examples
cd linkedin_post_examples/python/fastapi_postgres_docker_example
````

2. **Start services**

```bash
docker-compose up --build
```

3. **Access the app**

* FastAPI running at: [http://localhost:8000](http://localhost:8000)
* Check DB connection: [http://localhost:8000/ping-db](http://localhost:8000/ping-db)

## 🧪 Endpoints

| Method | URL        | Description                        |
| ------ | ---------- | ---------------------------------- |
| GET    | `/`        | Returns a welcome message          |
| GET    | `/ping-db` | Pings the PostgreSQL DB connection |

## ⚙️ Environment Variables

These are set directly inside `docker-compose.yml` for simplicity.

* `DATABASE_URL`: Postgres connection string in the format `postgresql://user:password@db:5432/app_db`

## 🛠 Tech Stack

* 🐍 FastAPI
* 🐘 PostgreSQL
* 🐳 Docker + Docker Compose
* 🔗 SQLAlchemy

## 📌 Related

* Previous Post: [fastapi\_docker\_example](../fastapi_docker_example) – the basic version without DB

## 🙌 Author

Made with ❤️ by [Lav](https://www.linkedin.com/in/lavsharmaa/)
This example is a part of my hands-on Docker tutorial series on LinkedIn and personal blog.

## 📄 License

This project is open source under the MIT License.