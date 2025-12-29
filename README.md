#  Enterprise Transaction Platform
<<<<<<< HEAD

A **full-stack, enterprise-grade transaction management system** designed to handle secure financial transactions, account management, and audit-ready workflows.
Built with **FastAPI, PostgreSQL, React, and Docker**, the platform follows clean architecture, REST best practices, and strong transactional integrity.

---

##  Features

*  Secure authentication using **JWT**
*  Account & transaction management with **ACID compliance**
*  High-performance REST APIs using **FastAPI**
*  Structured domain models for accounts, transactions, and logs
*  Modular backend architecture (scalable & testable)
*  Dockerized setup for consistent local & cloud deployment
*  Ready for enterprise extensions (audit logs, fraud detection, limits)

---

##  Tech Stack

###  Frontend

* **React** – Component-based UI
* **TypeScript** – Strong typing for maintainability
* **Axios** – API communication
* **React Router** – Client-side routing
* **Modern UI styling** (Tailwind / Material UI)

###  Backend

* **Python (FastAPI)** – High-performance async REST APIs
* **SQLAlchemy ORM** – Database modeling & queries
* **Pydantic** – Request/response validation
* **Uvicorn** – ASGI server

###  Database

* **PostgreSQL**

  * Transaction-safe (ACID)
  * Referential integrity
  * Optimized for financial data

###  Security

* **JWT Authentication**
* **Password hashing** with Passlib
* **Role-based access control (RBAC)** ready

###  DevOps & Tooling

* **Docker & Docker Compose**
* **Environment-based configuration**
* **Hot reload** for development

---

=======
This platform enables enterprises to manage financial transactions securely and efficiently, supporting audit-ready workflows, high concurrency, and real-time account management.

<p align="center">
  <a href="https://youtu.be/VEWHFmKNO2c?si=j_6FUYbjBTVRr4xe"> Watch Demo</a>
</p>
<p align="center">
   <img src="https://raw.githubusercontent.com/ManibalaSinha/Management/main/backend/app/assets/userDetails.png" width="600" />
  <img src="https://raw.githubusercontent.com/ManibalaSinha/Management/main/backend/app/assets/RetrievedData.png" width="600" />
  <img src="https://raw.githubusercontent.com/ManibalaSinha/Management/main/backend/app/assets/RetrievingUrl.png" width="600" />

</p>

A **full-stack, enterprise-grade transaction management system** designed to handle secure financial transactions, account management, and audit-ready workflows.
Built with **FastAPI, PostgreSQL, React, and Docker**, the platform follows clean architecture, REST best practices, and strong transactional integrity.
---

##  Features

*  Secure authentication using **JWT**
*  Account & transaction management with **ACID compliance**
*  High-performance REST APIs using **FastAPI**
*  Structured domain models for accounts, transactions, and logs
*  Modular backend architecture (scalable & testable)
*  Dockerized setup for consistent local & cloud deployment
*  Ready for enterprise extensions (audit logs, fraud detection, limits)

---

##  Tech Stack

###  Frontend

* **React** – Component-based UI
* **TypeScript** – Strong typing for maintainability
* **Axios** – API communication
* **React Router** – Client-side routing
* **Modern UI styling** (Tailwind / Material UI)

###  Backend

* **Python (FastAPI)** – High-performance async REST APIs
* **SQLAlchemy ORM** – Database modeling & queries
* **Pydantic** – Request/response validation
* **Uvicorn** – ASGI server

###  Database

* **PostgreSQL**

  * Transaction-safe (ACID)
  * Referential integrity
  * Optimized for financial data

###  Security

* **JWT Authentication**
* **Password hashing** with Passlib
* **Role-based access control (RBAC)** ready

###  DevOps & Tooling

* **Docker & Docker Compose**
* **Environment-based configuration**
* **Hot reload** for development

---

>>>>>>> 99f9e79 (Assets)
##  Project Structure

```
enterprise-transaction-platform/
│
├── backend/
│   ├── app/
│   │   ├── api/            # Route handlers
│   │   ├── core/           # Config, security, JWT
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # Business logic
│   │   ├── db/             # DB session & engine
│   │   └── main.py         # FastAPI entry point
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

##  Setup & Installation

### 1️ Clone the Repository

```bash
git clone https://github.com/ManibalaSinha/enterprise-transaction-platform.git
cd enterprise-transaction-platform
```

### 2️ Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/transactions
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 3️ Run with Docker

```bash
docker-compose up --build
```

* Backend → `http://localhost:8000`
* API Docs → `http://localhost:8000/docs`
* Frontend → `http://localhost:3000`

---

##  API Documentation

FastAPI automatically generates interactive API documentation:

* **Swagger UI** → `/docs`
* **ReDoc** → `/redoc`

Includes:

* Auth endpoints
* Account CRUD
* Transaction creation & retrieval
* Validation & error handling

---

##  Testing (Planned / Extendable)

* Unit testing with **pytest**
* API tests with **HTTPX**
* Database isolation using test containers

---

##  Architecture Highlights

<<<<<<< HEAD
=======
- Handles 10,000+ transactions per minute with ACID compliance
- Reduced transaction API latency by 30% with query optimization
>>>>>>> 99f9e79 (Assets)
* **Separation of concerns** (API, services, models)
* **Stateless APIs** (JWT-based auth)
* **Transaction-safe DB operations**
* **Scalable service layer**
* **Cloud-ready** (GCP / AWS / Azure compatible)

---

##  Future Enhancements

*  Audit logs & transaction history
*  Fraud detection rules
*  Rate limiting & API throttling
*  Admin dashboard
*  Event-driven processing (Kafka / PubSub)
*  CI/CD pipelines

---

##  Author

**Manibala Sinha**
<<<<<<< HEAD
Senior Full Stack / Python Engineer
=======
- Designed and implemented backend REST APIs with FastAPI and PostgreSQL
- Built React dashboards with TypeScript for transaction management
- Optimized database queries and improved API performance by 30–40%
- Managed Docker-based deployment and CI/CD pipelines

>>>>>>> 99f9e79 (Assets)
 Canada
 GitHub: [https://github.com/ManibalaSinha](https://github.com/ManibalaSinha)

---

##  Why This Project Matters
* **Enterprise backend design**
* **Financial transaction handling**
* **Strong Python & FastAPI expertise**
* **Production-ready architecture**
* **Docker & database mastery**


