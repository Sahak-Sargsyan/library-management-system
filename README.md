# Library Management System

Library Management System built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.  
This app provides robust API for managing books and members, borrowing/returning books, and includes custom exception handling, pagination and search.

---

## Architecture: Domain-Driven Design

This project is structured according to **Domain-Driven Design (DDD)**:

- **Domain Layer (`domain/`)**: Contains core business logic and entities (`Book`, `Member`).
- **Application Layer (`application/`)**: Implements use cases and orchestrates domain logic (`BookService`, `MemberService`).
- **Infrastructure Layer (`infrastructure/`)**: Handles database models, repositories, and mappers for persistence.
- **API Layer (`routers/`)**: Exposes RESTful endpoints using FastAPI, handling HTTP requests and responses.
- **Shared Layer (`shared/`)**: Defines common schemas and custom exceptions for consistent error handling.

---

## Features

- **Book Management:** Create, read, update, delete, search, and paginate books.
- **Member Management:** Register, update, and remove library members.
- **Borrow/Return:** Borrow and return books with proper validation.
- **Custom Exceptions:** Clear error responses for not found, already borrowed, and other business rules.
- **PostgreSQL Support:** Uses SQLAlchemy ORM with PostgreSQL.
- **Automatic API docs:** Swagger UI and ReDoc available out of the box.

---

## Project Structure

```
library-management-system/
│
├── domain/
│   └── book.py
│   └── member.py
├── application/
│   └── book_service.py
│   └── member_service.py
├── infrastructure/
│   ├── database.py
│   ├── library_repository.py
│   ├── mappers.py
│   └── models.py
├── routers/
│   ├── book.py
│   └── member.py
├── shared/
│   ├── exceptions.py
│   └── schemas.py
├── main.py
└── requirements.txt
```

---

##  Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL

**a. Start PostgreSQL**  
Make sure PostgreSQL is running on your machine.

**b. Create a new database and user**

```bash
# Enter the PostgreSQL shell (you may need to use 'sudo -u postgres psql' on some systems)
psql -U postgres

# In the psql shell, run:
CREATE DATABASE library_db;
CREATE USER library_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE library_db TO library_user;
\q
```

**c. Configure the database URL in your code**

Open `infrastructure/database.py` and set the connection string directly, for example:

```python
# filepath: infrastructure/database.py

DATABASE_URL = "postgresql+psycopg2://library_user:yourpassword@localhost:5432/library_db"

engine = create_engine(DATABASE_URL)
# ...existing code...
```

Make sure to replace `yourpassword` with the password you set above.

### 5. Run Alembic migrations

The project includes an `migrations/` folder with migration scripts.

1. Open `alembic.ini` and set the `sqlalchemy.url` to match your `DATABASE_URL`:

    ```
    sqlalchemy.url = postgresql+psycopg2://library_user:yourpassword@localhost:5432/library_db
    ```

2. Run the migrations:

    ```bash
    alembic upgrade head
    ```

### 6. Start the application

```bash
uvicorn main:app --reload
```

### 7. Access the API docs

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

**Troubleshooting tips:**
- If you change your models, create a new migration with `alembic revision --autogenerate -m "Describe changes"`, then run `alembic upgrade head`.
- If you get connection errors, double-check your database credentials and that PostgreSQL is running.
- All configuration is set directly in the code and `alembic.ini`—no environment variables are required.

---

## API Endpoints

### Books

- `GET /books/` — List all books (paginated)
- `GET /books/search?title=...&author=...` — Search books by title and/or author
- `GET /books/{book_id}` — Get a book by ID
- `POST /books/` — Create a new book
- `PUT /books/{book_id}` — Update a book
- `DELETE /books/{book_id}` — Delete a book
- `POST /books/borrow/{book_id}/{member_id}` — Borrow a book
- `POST /books/return/{book_id}` — Return a book

### Members

- `GET /members/` — List all members
- `GET /members/search?name=...&email=...` — Search members by name and/or email
- `GET /members/{member_id}` — Get a member by ID
- `POST /members/` — Create a new member
- `PUT /members/{member_id}` — Update a member
- `DELETE /members/{member_id}` — Delete a member
