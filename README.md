# ☕ Cafe Project

A complete REST API for cafe management built with Django and Django REST Framework.

## Features

- Manage categories, products, tables, and orders
- Create orders with multiple items in a single request
- JWT authentication
- Filtering, searching, ordering, and pagination
- Product image upload
- Django admin panel

## Tech Stack

- Python 3.12
- Django 6.1
- Django REST Framework
- PostgreSQL (configurable)
- JWT (djangorestframework-simplejwt)

## Installation & Setup

`bash

# Clone the repository

git clone https://github.com/MinaMohanna/cafe-api.git
cd cafeproject

# Create virtual environment

python3 -m venv venv
source .venv/bin/activate # Linux/macOS

# or

venv\Scripts\activate # Windows

# Install dependencies

pip install -r requirements.txt

# Run migrations

python manage.py migrate

# Create superuser

python manage.py createsuperuser

# Run the server

python manage.py runserver


## Cofe Project Structure
```text
cafeproject/
├── cafeproject/      # Project configuration
├── menu/             # Menu and orders app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── admin.py
├── manage.py
└── requirements.txt
```


## API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | /api/token/ | Obtain JWT access & refresh tokens | ❌ |
| POST | /api/token/refresh/ | Refresh access token | ❌ |

### Menu

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | /api/categories/ | List all categories | ❌ |
| POST | /api/categories/ | Create a new category | ✅ |
| GET | /api/categories/{id}/ | Retrieve a category | ❌ |
| PUT | /api/categories/{id}/ | Update a category | ✅ |
| DELETE | /api/categories/{id}/ | Delete a category | ✅ |
| GET | /api/products/ | List all products | ❌ |
| POST | /api/products/ | Create a new product | ✅ |
| GET | /api/products/{id}/ | Retrieve a product | ❌ |
| PUT | /api/products/{id}/ | Update a product | ✅ |
| DELETE | /api/products/{id}/ | Delete a product | ✅ |

### Orders & Tables

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | /api/tables/ | List all tables | ✅ |
| POST | /api/tables/ | Create a new table | ✅ |
| GET | /api/tables/{id}/ | Retrieve a table | ✅ |
| PUT | /api/tables/{id}/ | Update a table | ✅ |
| DELETE | /api/tables/{id}/ | Delete a table | ✅ |
| GET | /api/orders/ | List all orders | ✅ |
| POST | /api/orders/ | Create a new order with items | ✅ |
| GET | /api/orders/{id}/ | Retrieve an order | ✅ |
| PUT | /api/orders/{id}/ | Update an order | ✅ |
| DELETE | /api/orders/{id}/ | Delete an order | ✅ |
| GET | /api/order-items/ | List all order items | ✅ |
| POST | /api/order-items/ | Create a new order item | ✅ |

### Filtering & Search

| Query Param | Applies To | Example |
|-------------|------------|---------|
| ?category={id} | Products | /api/products/?category=1 |
| ?is_available=true | Products | /api/products/?is_available=true |
| ?search={term} | Products | /api/products/?search=coffee |
| ?ordering={field} | Products, Orders | /api/products/?ordering=price |
| ?status={status} | Orders | /api/orders/?status=pending |
| ?table={id} | Orders | /api/orders/?table=1 |
| ?page={number} | All | /api/products/?page=2 |

### Example: Creating an Order

POST /api/orders/

```json
{
    "table": 1,
    "status": "pending",
    "is_paid": false,
    "items": [
        {
            "product": 1,
            "quantity": 2,
            "price": "125000.00"
        },
        {
            "product": 2,
            "quantity": 1,
            "price": "80000.00"
        }
    ]
}
```
