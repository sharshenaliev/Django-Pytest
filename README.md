# Usage

An overview of the project.

## Env configuration

Create `.env` file and fill data:

```shell
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=*
CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1
POSTGRES_DB=test
POSTGRES_USER=test
POSTGRES_PASSWORD=test
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

## Instructions on how to build and run your application using Docker Compose

1. Run Docker Compose command:

    ```
    docker-compose up -d --build
    ```
   
2. Run Unit tests:

    ```
    docker-compose exec app pytest
    ```

## Work with app

1. Swagger UI `http://localhost:8000/docs`.

2. ReDoc `http://localhost:8000/redoc`.

3. Admin panel Jazzmin `http://localhost:8000/admin`.

## How to use the API

To use API I set IsAuthenticatedOrReadOnly permission, which means you must 
be authenticated to Create, Edit or Delete in Database.

To create user follow instructions in swagger:

- Send email, password and password2 to `/register/` endpoint
- Send email and password to `/login/` endpoint to obtain token and to `/logout/` endpoint to delete token



# Filter

To List API I set query params:

- Fields `genre` and `author` must contain ids
- Field `date` must match with DateField of Book use format "%Y-%M-%D" and should be `2024-05-09`
- Fields `date_range_after` and `date_range_before` can filter in date range, use format "%Y-%M-%D" and should be `2024-05-09`

