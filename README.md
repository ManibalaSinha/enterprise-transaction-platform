# enterprise-transaction-platform
A full-stack enterprise-transaction-platform
   designed for teams to track, organize, and manage customer efficiently. Built with a React frontend, FastAPI backend, and PostgreSQL database, this application supports complete CRUD operations, authentication, and role-based access.

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

Project Structure

Watch Demo