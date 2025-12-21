# enterprise-transaction-platform
A full-stack enterprise-transaction-platform
   designed for teams to track, organize, and manage customer efficiently. Built with a React frontend, FastAPI backend, and PostgreSQL database, this application supports complete CRUD operations, authentication, and role-based access.

Problem statement (transaction + risk)
Architecture diagram
Tech stack
Failure handling
Security considerations

Step 1️ Domain Model
Entities:
Transaction
Account
AuditLog
RiskFlag

Step 2️ API Design
Endpoints like:
POST /transactions
GET /transactions/{id}
POST /transactions/{id}/retry

Step 3️ Database Transactions
ACID
Rollback
Isolation levels
Idempotency keys

User Authentication
JWT-based login & signup
Password hashing using Passlib
Secure protected routes

 Management
Create new user, transactions, account 
Update user information,  transactions 
Assign transactions to users,  account 
Track user source, status, and priority
Delete or archive user

REST API (FastAPI)
Modular router-based architecture
Pydantic models (FastAPI v2 compatible)
Input validation & schema generation
Auto-generated docs via Swagger & ReDoc

Frontend (React)
User-friendly dashboard
Add/Edit user forms
Table view with sorting & filtering
Axios API integration
Toast notifications

Database (PostgreSQL + SQLAlchemy)
Relational schema with foreign keys
account, Users, Auth tokens
Optimized queries

Tech Stack
Frontend

React, TypeScript
Axios, React Router
TailwindCSS / Material UI (optional)
Backend

Python FastAPI
SQLAlchemy ORM
PostgreSQL
Uvicorn
Passlib
python-jose (JWT)

DevOps

AWS, Docker & Docker Compose
Environment variables for secrets
Hot reload for both frontend and backend

API Endpoints
Auth

Method	Endpoint	Description
POST	/auth/login	Login user
POST	/auth/signup	Register new user
Leads

Method	Endpoint	Description
GET	/users/	Get all users
POST	/users/	Create a user
PUT	/users/{id}	Update a user
DELETE	/users/{id}	Delete a user

How to Run Locally
Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
Runs at: http://127.0.0.1:8000
API Docs: http://127.0.0.1:8000/docs

Frontend
cd frontend
npm install
npm start
Runs at: http://localhost:3000
Docker Setup
docker-compose up --build
This starts:

React app
FastAPI backend
PostgreSQL database

Why I Built This Project
Production-ready full-stack system
Real authentication
Secure API development
SQL database modeling
React frontend architecture
Full CRUD implementation
API integration & state management
Clean code & scalability

Ideal for:

SaaS CRM tools
Small business lead tracking
Sales team workflow automation

Author
Manibala Sinha — Full Stack Developer (React, Node.js, Python) Vaughan, ON, Canada GitHub: https://github.com/ManibalaSinha
