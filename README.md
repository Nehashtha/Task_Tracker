# Task Tracker

A Python-based Task Tracker application that evolved from a command-line task manager into a REST API using FastAPI, SQLite, and Docker.

The project demonstrates object-oriented programming, database integration, REST API development, and application containerization.

## Project Evolution

This project was developed incrementally:

1. **JSON-based version:** Started with a command-line Task Manager using Python and OOP, with JSON for saving and loading tasks.
2. **SQLite integration:** Upgraded persistence from JSON files to an SQLite database and implemented database CRUD operations.
3. **FastAPI integration:** Developed REST API endpoints to manage tasks.
4. **Docker integration:** Containerized the FastAPI application and configured Docker Compose with persistent SQLite database storage.

## Features

### Task Management
- Create and manage tasks
- View all tasks
- Update task information and status
- Filter tasks by ID and category
- Search tasks by keyword
- Remove tasks
- Validate task inputs, priority, category, and due dates

### Database
- SQLite database integration
- Persistent task storage
- Database CRUD operations

### REST API
- Built using FastAPI
- CRUD operations for task management
- HTTP status codes and error handling
- Interactive API documentation using Swagger UI

### Docker
- Custom Dockerfile
- Docker image creation and container execution
- Docker Compose for application management
- SQLite database persistence using a host bind mount

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- SQLite
- FastAPI
- Pydantic
- Pytest
- Docker
- Docker Compose
- Git and GitHub

## Project Structure

```text
Task_Tracker/
│
├── main.py                 # OOP-based CLI entry point
├── app.py                  # Basic CLI application
├── Task.py                 # Task model
├── Task_manager.py         # Task management and database operations
├── validation.py           # Input validation
│
├── api.py                  # FastAPI application and endpoints
├── api_module.py           # API request model
│
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image configuration
├── compose.yaml            # Docker Compose configuration
├── .dockerignore           # Files excluded from Docker build
├── .gitignore              # Files excluded from Git
│
└── README.md
```

## Running the Application Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the FastAPI application

```bash
uvicorn api:app --reload
```

### 3. Open the API documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides an interactive interface to explore and test the API endpoints.

## Running with Docker Compose

Build and start the application:

```bash
docker compose up --build
```

To view running containers:

```bash
docker compose ps
```

To view application logs:

```bash
docker compose logs
```

To stop and remove the containers:

```bash
docker compose down
```

The SQLite database is mounted from the host machine into the container so database data can persist beyond the container lifecycle.

## Testing

Pytest is used to practice and test the task management functionality, including database-related operations and validation.

API-specific automated tests are a planned improvement.

## Future Improvements

- Add automated API tests using Pytest
- Integrate GitHub Actions for CI/CD
- Deploy the containerized application to AWS EC2
- Improve application configuration and environment management

---

This project is an ongoing learning and portfolio project focused on Python development, API automation concepts, database operations, and DevOps fundamentals.
