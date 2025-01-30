# 🚀 FastAPI Authentication

A robust and scalable authentication system built with FastAPI, including user registration, login, JWT-based authentication, and password management.

## ✨ Features

- 🔐 User Authentication (JWT tokens)
- 📝 User Registration with validation
- 🔄 Password Hashing & Verification
- 🔑 OAuth2 Password Flow
- 📅 User Last Login Traking
- 📧 Email-Based Password Reset

## 🛠️ Technologies Used

- **FastAPI**: Framework for building fast and efficient APIs.
- **SQLModel**: Library for managing the database with SQLAlchemy and Pydantic.
- **SQLite**: Lightweight database for local development.
- **JWT**: Token-based authentication.
- **FastAPI Mail**: Sending emails for password reset.

## ✅ Prerequisites

Before getting started, make sure you have the following installed:
- **Python 3.9 or higher**
- **Pip** (Python package manager)
- **Git** (optional, for cloning the repository)

## 🖥️ Project Setup

### 1. Clone the Repository
f you have Git installed, you can clone the repository by running:
```bash
git clone https://github.com/anmamebo/fastapi-authentication.git
```
```bash
cd fastapi-authentication
```

### 2. Create a Virtual Environment
It is recommended to create a virtual environment to isolate the project dependencies:
```bash
python -m venv venv
```
**Activate the Virtual Environment**
- Windows:
```bash
venv\Scripts\activate
```
- Linux/MacOS:
 ```bash
source venv/bin/activate
```

### 3. Install Dependencies
Install the project dependencies using `pip`:
 ```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy the `.env.example`, rename it to `.env` and complete the following variables:
 ```bash
# Password Secret Key
SECRET_KEY=your_secret_key_here

# Reset Password Secret Key
RESET_PASSWORD_SECRET_KEY=your_reset_password_secret_key_here

# Database sqlite
DB_DATABASE=your_database_name_here

# Email Configuration
EMAIL_USERNAME=your_email_username_here
EMAIL_PASSWORD=your_email_password_here
EMAIL_FROM=your_email_here@example.com
EMAIL_PORT=your_email_port_here
EMAIL_SERVER=your_email_server_here
```

## ▶️ Running the Project
To start the development server, run:
 ```bash
fastapi dev app/main.py
```
The server will be available at `http://127.0.0.1:8000`.

### API Documentation
Once the server is running, you can access the interactive API documentation:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## 📂 Project Structure

 ```bash
fastapi-authentication/
├── app/
│   ├── crud/              # CRUD operations for the database
│   ├── database/          # Database configuration
│   ├── models/            # SQLModel models
│   ├── routes/            # API routes
│   ├── schemas/           # Pydantic schemas
│   ├── utils/             # Utilities (security, email, etc.)
│   └── main.py            # Application entry point
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables
└── README.md              # This file
```

## 🤝 Contributing

If you would like to contribute to this project, follow these steps:
1. **Fork** the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a **Pull Request** on GitHub.

## 📜 Licence

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## 📬 Contact

* Developer: Antonio Manuel
* GitHub: @anmamebo
* Email: anmamebo2001@gmail.com
