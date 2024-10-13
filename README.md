# Ledger API

The **Ledger API** is a RESTful API built with Django and Django REST Framework for managing data related to products, suppliers, and buyers. It supports CRUD operations, filtering, and token-based authentication using Knox.

---

## Table of Contents

1. **Features**
2. **Technology Stack**
3. **Getting Started**
   - Installation
   - Environment Variables
4. **API Usage**
5. **Endpoints**
   - User Management
   - Product Management
   - Supplier Management
   - Customer Management
6. **Static and Media Files**
7. **CORS Configuration**
8. **Contributing**
9. **License**

---

## Features

- User registration, login, and token-based authentication
- Product, supplier, and customer management with detailed CRUD functionality
- Filtering capabilities for products, suppliers, and orders
- Static and media file management
- CORS handling for secure cross-origin requests

---

## Technology Stack

- **Python**: 3.8+
- **Django**: 4.2
- **Django REST Framework**
- **Knox**: for token-based authentication
- **SQLite**: default database
- **django-filter**: for filtering API data
- **django-cors-headers**: for managing CORS

---

## Getting Started

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ledgerApi.git
   cd ledgerApi
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

### Environment Variables

Create a `.env` file in the root directory of your project and add the following environment variables:

```
SECRET_KEY=your-secret-key
DEBUG=True
```

Replace `your-secret-key` with your actual Django secret key.

---

## API Usage

You can interact with the Ledger API using tools like Postman, Insomnia, or `curl` commands from the terminal. The base URL for the API endpoints is:

```
http://localhost:8000
```

---

## Endpoints

### User Management

| Endpoint                  | Method | Description               |
|---------------------------|--------|---------------------------|
| `/user/register/`         | POST   | Register a new user       |
| `/user/login/`            | POST   | Log in an existing user   |
| `/user/logout/`           | POST   | Log out a user            |
| `/user/get-user/`         | GET    | Retrieve logged-in user's info |
| `/user/change-password/`  | POST   | Change user's password    |

### Product Management

| Endpoint                     | Method | Description                      |
|------------------------------|--------|----------------------------------|
| `/product/product-list/`     | GET    | List all products               |
| `/product/product-create/`   | POST   | Create a new product            |
| `/product/product-detail/<id>/` | GET | Retrieve product details by ID  |
| `/product/product-update/<id>/` | PUT | Update product details by ID    |
| `/product/product-delete/<id>/` | DELETE | Delete a product by ID      |

### Supplier Management

| Endpoint                        | Method | Description                      |
|---------------------------------|--------|----------------------------------|
| `/supplier/supplier-list/`      | GET    | List all suppliers               |
| `/supplier/supplier-create/`    | POST   | Create a new supplier            |
| `/supplier/supplier-detail/<id>/` | GET | Retrieve supplier details by ID  |
| `/supplier/supplier-update/<id>/` | PUT | Update supplier details by ID    |
| `/supplier/supplier-delete/<id>/` | DELETE | Delete a supplier by ID      |

### Customer Management

| Endpoint                        | Method | Description                      |
|---------------------------------|--------|----------------------------------|
| `/customer/customer-list/`      | GET    | List all customers               |
| `/customer/customer-create/`    | POST   | Create a new customer            |
| `/customer/customer-detail/<id>/` | GET | Retrieve customer details by ID  |
| `/customer/customer-update/<id>/` | PUT | Update customer details by ID    |
| `/customer/customer-delete/<id>/` | DELETE | Delete a customer by ID      |

---

## Static and Media Files

This project uses the following configuration for static and media files:

- **Static Files**: Collected to the `staticfiles` directory during production using `STATIC_ROOT`.
- **Media Files**: Uploaded files are stored in the `media` directory, which can be accessed via `MEDIA_URL`.

---

## CORS Configuration

To allow the API to handle cross-origin requests, `django-cors-headers` is installed and configured to allow all origins. This can be customized as needed by modifying the `CORS_ALLOWED_ORIGINS` in `settings.py`.

---

## Contributing

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.
