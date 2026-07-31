# 📚 ShelfShare

## AI-Powered Digital Book Rental and Marketplace Platform

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Bootstrap-UI-7952B3?logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Google%20Gemini-AI-8E75B2?logo=googlegemini&logoColor=white" alt="Google Gemini">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/License-MIT-success" alt="MIT License">
</p>

<p align="center">
  <strong>Buy, sell, rent, reserve, scan, and manage books through one intelligent platform.</strong>
</p>

---

## 📌 Overview

**ShelfShare** is an AI-powered digital textbook marketplace and rental platform designed to simplify the way students access and manage academic books.

The platform allows users to:

* Buy and sell books
* Rent and return books
* Reserve unavailable books
* Maintain a personal wishlist
* Manage book inventory and individual copies
* Make simulated payments
* View real-time analytics
* Scan book covers using AI

ShelfShare integrates the **Google Gemini Vision API** to automatically extract textbook information from cover images. This reduces manual data entry and makes adding books faster, easier, and more accurate.

---

## ✨ Key Features

### 👤 User Authentication

* User registration
* Secure login
* JWT-based authentication
* Password hashing
* OAuth2 Password Bearer authentication
* Protected frontend and backend routes
* User-specific rentals, reservations, and wishlists

### 📖 Book Marketplace

* Add new books
* View available books
* Browse book details
* Buy and sell books
* Rent books
* Update book information
* Delete books
* Search books by title, author, ISBN, or subject
* Filter books by availability and category

### 🤖 AI-Powered Book Scanner

Users can upload a textbook cover image and automatically extract:

* Book title
* Author
* ISBN
* Publisher
* Edition
* Subject
* Description

The extracted information can be reviewed and edited before being stored in the database.

> The AI scanner is powered by the Google Gemini Vision API.

### 📦 Inventory Management

* Add multiple copies of the same book
* Assign rack or storage locations
* Track the availability of every copy
* Monitor copy status
* Update inventory after rentals and returns
* Differentiate between available, rented, reserved, sold, and damaged copies

### ❤️ Wishlist

Users can:

* Save books for later
* View all wishlist items
* Remove books from their wishlist
* Quickly access saved book details

### 📅 Reservation System

When a book is unavailable, users can:

* Reserve the book
* Join a reservation queue
* Track reservation status
* View active and previous reservations

### 📚 Rental Management

* Borrow available books
* Automatically assign a due date
* Return borrowed books
* Track active rentals
* View rental history
* Update book-copy availability after borrowing or returning

### 💳 Payment Module

ShelfShare includes a simulated payment gateway supporting:

* UPI
* Credit card
* Debit card
* Cash

Every successful transaction generates a unique transaction ID for tracking and record management.

> This module is currently intended for demonstration purposes and does not process real payments.

### 📊 Dashboard and Analytics

The dashboard displays real-time platform statistics, including:

* Total registered users
* Total books
* Total book copies
* Available copies
* Active rentals
* Reservations
* Wishlist items
* Recently added books
* Recent platform activity

---

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Backend

* Python
* FastAPI
* SQLAlchemy
* Alembic
* Pydantic
* Uvicorn

### Database

* PostgreSQL

### Authentication

* JWT
* OAuth2 Password Bearer
* Password hashing

### Artificial Intelligence

* Google Gemini API
* Gemini Vision

### Deployment

* Render — Backend
* Vercel — Frontend
* Docker — Backend containerization

---

## 🏗️ System Architecture

```text
                         User
                           │
                           ▼
                Frontend Application
              HTML / CSS / JavaScript
                           │
                    REST API Calls
                           │
                           ▼
                  FastAPI Backend
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
   Authentication     Book Services     AI Scanner
          │                │                │
          ▼                ▼                ▼
      User Data       Inventory and     Gemini Vision
                        Rentals              API
          │                │
          └────────┬───────┘
                   ▼
              PostgreSQL
                   │
                   ▼
         Dashboard and Analytics
```

---

## 🤖 AI Metadata Extraction Flow

```text
Book Cover Image
        │
        ▼
Upload Image
        │
        ▼
FastAPI Backend
        │
        ▼
Gemini Vision API
        │
        ▼
Extract Book Metadata
        │
        ▼
Review and Edit Details
        │
        ▼
Save Book in PostgreSQL
```

---

## 📚 Rental Workflow

```text
Browse Available Books
          │
          ▼
Select a Book
          │
          ▼
Choose Borrow Option
          │
          ▼
Complete Mock Payment
          │
          ▼
Create Rental Record
          │
          ▼
Update Inventory Status
          │
          ▼
Return Book
          │
          ▼
Mark Copy as Available
```

---

## 📂 Project Structure

```text
ShelfShare/
│
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   │   ├── llm.py
│   │   │   ├── parser.py
│   │   │   └── prompt.py
│   │   │
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── database.py
│   │   └── main.py
│   │
│   ├── alembic/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── images/
│   ├── index.html
│   ├── dashboard.html
│   ├── books.html
│   ├── inventory.html
│   ├── wishlist.html
│   ├── reservations.html
│   ├── borrow.html
│   ├── payment.html
│   └── scan.html
│
├── README.md
└── .gitignore
```

---

## 🗄️ Database Modules

ShelfShare uses a relational PostgreSQL database containing the following primary modules:

| Module       | Purpose                                             |
| ------------ | --------------------------------------------------- |
| Users        | Stores user accounts and authentication information |
| Books        | Stores general book metadata                        |
| Book Copies  | Tracks individual physical copies and availability  |
| Rentals      | Manages borrowing, due dates, and returns           |
| Reservations | Stores reservation queues and statuses              |
| Wishlist     | Stores books saved by users                         |
| Payments     | Stores mock payment transactions                    |
| Activities   | Tracks recent actions shown on the dashboard        |

---

## 🔌 REST API Endpoints

### Authentication

| Method | Endpoint         | Description                              |
| ------ | ---------------- | ---------------------------------------- |
| `POST` | `/auth/register` | Register a new user                      |
| `POST` | `/auth/login`    | Authenticate a user and generate a token |

### Books

| Method   | Endpoint             | Description              |
| -------- | -------------------- | ------------------------ |
| `GET`    | `/books`             | Retrieve all books       |
| `POST`   | `/books`             | Add a new book           |
| `GET`    | `/books/{id}`        | Retrieve a specific book |
| `PUT`    | `/books/{id}`        | Update book information  |
| `DELETE` | `/books/{id}`        | Delete a book            |
| `GET`    | `/books/available`   | Retrieve available books |
| `POST`   | `/books/{id}/copies` | Add copies of a book     |

### AI Scanner

| Method | Endpoint | Description                              |
| ------ | -------- | ---------------------------------------- |
| `POST` | `/scan`  | Extract metadata from a book-cover image |

### Rentals

| Method | Endpoint             | Description                      |
| ------ | -------------------- | -------------------------------- |
| `POST` | `/rentals/borrow`    | Borrow an available book         |
| `POST` | `/rentals/return`    | Return a rented book             |
| `GET`  | `/rentals/{user_id}` | Retrieve a user's rental history |

### Reservations

| Method | Endpoint                  | Description                    |
| ------ | ------------------------- | ------------------------------ |
| `POST` | `/reservations`           | Reserve an unavailable book    |
| `GET`  | `/reservations/{user_id}` | Retrieve a user's reservations |

### Wishlist

| Method   | Endpoint              | Description                      |
| -------- | --------------------- | -------------------------------- |
| `POST`   | `/wishlist`           | Add a book to the wishlist       |
| `GET`    | `/wishlist/{user_id}` | Retrieve a user's wishlist       |
| `DELETE` | `/wishlist/{id}`      | Remove an item from the wishlist |

### Payments

| Method | Endpoint    | Description                       |
| ------ | ----------- | --------------------------------- |
| `POST` | `/payments` | Create a mock payment transaction |

### Dashboard

| Method | Endpoint           | Description                   |
| ------ | ------------------ | ----------------------------- |
| `GET`  | `/dashboard/stats` | Retrieve dashboard statistics |

> Endpoint names may be adjusted depending on the final router configuration.

---

## 🚀 Installation and Setup

### Prerequisites

Ensure that the following software is installed:

* Python 3.10 or later
* PostgreSQL
* Git
* A modern web browser
* Google Gemini API key

---

### 1. Clone the Repository

```bash
git clone https://github.com/YASHIKA-ASH/ShelfShare.git
cd ShelfShare
```

---

### 2. Configure the Backend

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

#### Activate on Windows

```bash
venv\Scripts\activate
```

#### Activate on macOS or Linux

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file inside the `backend` directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/shelfshare
SECRET_KEY=your_secure_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
GOOGLE_API_KEY=your_google_gemini_api_key
```

Replace the placeholder values with your actual credentials.

> Never upload the `.env` file or private API keys to GitHub.

---

### 4. Create the PostgreSQL Database

Create a PostgreSQL database named `shelfshare`, or use another name and update the `DATABASE_URL` accordingly.

Example:

```sql
CREATE DATABASE shelfshare;
```

---

### 5. Run Database Migrations

From the `backend` directory, run:

```bash
alembic upgrade head
```

---

### 6. Start the Backend Server

```bash
uvicorn app.main:app --reload
```

The backend will normally be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative API documentation:

```text
http://127.0.0.1:8000/redoc
```

---

### 7. Start the Frontend

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
```

Start a local development server:

```bash
python -m http.server 5500
```

Open the following address in your browser:

```text
http://localhost:5500
```

Opening the HTML files directly may cause problems with API requests or browser CORS rules, so using a local HTTP server is recommended.

---

## 🐳 Run the Backend with Docker

Navigate to the backend directory:

```bash
cd backend
```

Build the Docker image:

```bash
docker build -t shelfshare-backend .
```

Run the container:

```bash
docker run -p 8000:8000 --env-file .env shelfshare-backend
```

The API will be available at:

```text
http://localhost:8000
```

---

## 📖 API Documentation

After starting the backend server, FastAPI automatically generates interactive documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger UI can be used to:

* Test API endpoints
* Send request bodies
* Add JWT authentication tokens
* Inspect response models
* Review validation errors

---

## 🌐 Deployment

The project can be deployed using:

### Backend

* Render
* Docker-compatible cloud platforms

### Frontend

* Vercel
* Netlify
* GitHub Pages

### Database

* Render PostgreSQL
* Neon
* Supabase
* Railway

Before deployment, update the frontend API base URL to point to the deployed backend URL.

Example:

```javascript
const API_BASE_URL = "https://your-backend-url.onrender.com";
```

Environment variables must be added securely through the deployment platform's settings.

---

## 📸 Screenshots

Add project screenshots inside the `frontend/images/screenshots` directory and replace the placeholders below.

### Login Page

```markdown
![Login Page](frontend/images/screenshots/login.png)
```

### Dashboard

```markdown
![Dashboard](frontend/images/screenshots/dashboard.png)
```

### Book Marketplace

```markdown
![Book Marketplace](frontend/images/screenshots/books.png)
```

### AI Book Scanner

```markdown
![AI Book Scanner](frontend/images/screenshots/ai-scanner.png)
```

### Inventory Management

```markdown
![Inventory Management](frontend/images/screenshots/inventory.png)
```

### Wishlist

```markdown
![Wishlist](frontend/images/screenshots/wishlist.png)
```

### Reservations

```markdown
![Reservations](frontend/images/screenshots/reservations.png)
```

### Payment Module

```markdown
![Payment Module](frontend/images/screenshots/payment.png)
```

---

## 🔐 Security Considerations

* Passwords should always be securely hashed.
* JWT tokens should have limited expiration times.
* Secret keys must be stored in environment variables.
* API keys must never be committed to GitHub.
* Protected routes should validate the authenticated user.
* Input data should be validated using Pydantic schemas.
* Production deployments should use HTTPS.
* Database credentials should not be included in source code.

---

## 🧪 Suggested Test Cases

Important workflows that should be tested include:

* Registering with valid and invalid information
* Logging in with correct and incorrect credentials
* Accessing protected routes without a token
* Adding, updating, and deleting books
* Adding multiple copies of a book
* Borrowing an available copy
* Attempting to borrow an unavailable copy
* Returning a rented book
* Reserving an unavailable book
* Adding and removing wishlist items
* Uploading valid and invalid cover images
* Reviewing AI-generated metadata
* Completing mock payments
* Checking dashboard statistics after transactions

---

## 🗺️ Future Improvements

* Razorpay or Stripe payment integration
* Email and SMS notifications
* QR-code-based borrowing
* Barcode and ISBN scanner
* Personalized book recommendation system
* Late-return fine management
* Dedicated admin panel
* Role-based access control
* Mobile application
* User reviews and ratings
* Real-time reservation notifications
* Advanced search and sorting
* Docker Compose configuration
* Automated testing
* CI/CD pipeline
* Cloud image storage
* Book-demand and rental analytics

---

## ⭐ Project Highlights

* AI-powered textbook metadata extraction using Google Gemini Vision
* Complete buy, sell, rent, reserve, and wishlist workflow
* Secure JWT-based authentication and authorization
* Book-level and copy-level inventory management
* Automated inventory updates after rentals and returns
* Mock payment workflow with unique transaction tracking
* Real-time analytics dashboard
* Modular FastAPI backend architecture
* PostgreSQL database with SQLAlchemy ORM
* RESTful API design
* Docker-supported backend deployment
* Render and Vercel deployment compatibility

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add your feature description"
```

5. Push the branch.

```bash
git push origin feature/your-feature-name
```

6. Open a pull request.

---

## 👩‍💻 Author

**Yashika Sharma**

B.E. Electronics and Computer Engineering
Thapar Institute of Engineering and Technology

GitHub: [YASHIKA-ASH](https://github.com/YASHIKA-ASH)

---

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for complete license information.

---

<p align="center">
  Made with ❤️ for students and book lovers
</p>

<p align="center">
  ⭐ Star the repository if you found this project useful!
</p>
