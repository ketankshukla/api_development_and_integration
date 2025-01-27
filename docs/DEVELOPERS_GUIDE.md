# <span style="color: #2E86C1; font-size: 32px;">Developer's Guide - FastAPI Customer and Product API</span>

## <span style="color: #E74C3C; font-size: 24px;">Project Structure</span>
```
app/
├── __init__.py
├── main.py             # Main FastAPI application
├── database.py         # Database configuration
├── models/
│   ├── __init__.py
│   └── models.py       # SQLAlchemy models
└── schemas/
    └── schemas.py      # Pydantic schemas
tests/
└── test_main.py       # API tests
```

## <span style="color: #27AE60; font-size: 24px;">Setup Development Environment</span>

1. Create a virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

## <span style="color: #8E44AD; font-size: 24px;">Database</span>
- SQLite database is used for simplicity
- Database file: `sql_app.db` (automatically created on first run)
- Models are defined in `app/models/models.py`
- Database connection is configured in `app/database.py`

## <span style="color: #D35400; font-size: 24px;">Models</span>
### <span style="color: #2980B9;">Customer</span>
- id: Integer (Primary Key)
- name: String
- email: String (Unique)

### <span style="color: #2980B9;">Product</span>
- id: Integer (Primary Key)
- name: String
- price: Float
- description: String

## <span style="color: #C0392B; font-size: 24px;">API Endpoints</span>
### <span style="color: #2980B9;">Customers</span>
- POST `/customers/`: Create new customer
- GET `/customers/`: List customers (with pagination)

### <span style="color: #2980B9;">Products</span>
- POST `/products/`: Create new product
- GET `/products/`: List products (with pagination)

## <span style="color: #16A085; font-size: 24px;">Running Tests</span>
```powershell
pytest tests/test_main.py -v
```

## <span style="color: #2C3E50; font-size: 24px;">Development Server</span>
```powershell
uvicorn app.main:app --reload
```

## <span style="color: #E67E22; font-size: 24px;">API Documentation</span>
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## <span style="color: #9B59B6; font-size: 24px;">Adding New Features</span>
1. Add new models in `app/models/models.py`
2. Create corresponding Pydantic schemas in `app/schemas/schemas.py`
3. Add new endpoints in `app/main.py`
4. Write tests in `tests/test_main.py`

## <span style="color: #1ABC9C; font-size: 24px;">Best Practices</span>
- Always validate input data using Pydantic schemas
- Write tests for new endpoints
- Use type hints
- Follow PEP 8 style guidelines
- Keep the database session handling consistent using dependency injection
