# <span style="color: #2E86C1; font-size: 32px;">User's Guide - Customer and Product API</span>

## <span style="color: #E74C3C; font-size: 24px;">Overview</span>
This API provides endpoints to manage customers and products in a simple database system.

## <span style="color: #27AE60; font-size: 24px;">Base URL</span>
The API is accessible at: `http://127.0.0.1:8000`

## <span style="color: #8E44AD; font-size: 24px;">Interactive Documentation</span>
- Visit `http://127.0.0.1:8000/docs` for interactive Swagger documentation
- Try out API endpoints directly from your browser

## <span style="color: #D35400; font-size: 24px;">API Endpoints</span>

### <span style="color: #2980B9; font-size: 20px;">Customers</span>

#### <span style="color: #16A085;">Create a Customer</span>
- **Endpoint**: POST `/customers/`
- **Body**:
```json
{
    "name": "John Doe",
    "email": "john@example.com"
}
```
- **Response**: Returns created customer with ID

#### <span style="color: #16A085;">List Customers</span>
- **Endpoint**: GET `/customers/`
- **Query Parameters**:
  - `skip`: Number of records to skip (default: 0)
  - `limit`: Maximum number of records to return (default: 10)
- **Response**: Returns list of customers

### <span style="color: #2980B9; font-size: 20px;">Products</span>

#### <span style="color: #16A085;">Create a Product</span>
- **Endpoint**: POST `/products/`
- **Body**:
```json
{
    "name": "Sample Product",
    "price": 99.99,
    "description": "A great product"
}
```
- **Response**: Returns created product with ID

#### <span style="color: #16A085;">List Products</span>
- **Endpoint**: GET `/products/`
- **Query Parameters**:
  - `skip`: Number of records to skip (default: 0)
  - `limit`: Maximum number of records to return (default: 10)
- **Response**: Returns list of products

## <span style="color: #C0392B; font-size: 24px;">Example API Calls</span>

### <span style="color: #9B59B6;">Using cURL</span>

1. Create a Customer:
```bash
curl -X POST "http://127.0.0.1:8000/customers/" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com"}'
```

2. List Customers:
```bash
curl "http://127.0.0.1:8000/customers/"
```

3. Create a Product:
```bash
curl -X POST "http://127.0.0.1:8000/products/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Sample Product", "price": 99.99, "description": "A great product"}'
```

4. List Products:
```bash
curl "http://127.0.0.1:8000/products/"
```

## <span style="color: #E67E22; font-size: 24px;">Error Handling</span>
- The API returns appropriate HTTP status codes
- Error responses include a message explaining what went wrong
- Common error codes:
  - <span style="color: #E74C3C;">400</span>: Bad Request (invalid input)
  - <span style="color: #E74C3C;">404</span>: Not Found
  - <span style="color: #E74C3C;">422</span>: Validation Error (invalid data format)
  - <span style="color: #E74C3C;">500</span>: Internal Server Error

## <span style="color: #2C3E50; font-size: 24px;">Pagination</span>
- All list endpoints support pagination
- Use `skip` and `limit` query parameters to control the number of records returned
- Example: `GET /customers/?skip=10&limit=5` will skip the first 10 records and return the next 5
