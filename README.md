# FastAPI Base Project

A minimal FastAPI project setup for quick start and easy expansion.

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-base-project.git
   cd fastapi-base-project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

Start the server with:

```
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
fastapi-base-project/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── controllers/
│   │       ├── __init__.py
│   │       └── items.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── crud/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── session.py
│   └── tests/
│       ├── __init__.py
│       └── test_items.py
├── .env
├── requirements.txt
└── README.md
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)