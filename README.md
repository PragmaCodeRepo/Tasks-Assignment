# 🧩 Personal Task Manager (Django + REST + GraphQL)

### 📘 Overview
This is a **lightweight backend service** built using **Django** and **Django REST Framework**, designed to manage personal tasks.  
Each task is linked to a specific user and visible **only to that user**.  
The project provides both **REST APIs** and a **GraphQL endpoint** for flexible task management.

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | Django (latest) |
| **API Framework** | Django REST Framework |
| **GraphQL** | Graphene-Django |
| **Database** | SQLite (can be replaced with PostgreSQL) |
| **Authentication** | Custom Token Authentication |
| **Testing Tool** | Postman |

---

## 🧠 Features

### 🔐 Authentication
- Basic username/password login (admin-created users).
- Simple token-based authentication mechanism (custom model).
- Each request must include `Authorization: Token <your_token>` in headers.

### 📝 Task Management (CRUD)
- **Create Task** – Authenticated users can create new tasks.
- **List Tasks** – Each user can see only their own tasks.
- **Update Task** – Only if the task belongs to the current user.
- **Delete Task** – Only if the task belongs to the current user.

### 🧭 GraphQL Endpoint
- Built using `graphene-django`.
- Authenticated users can list all their tasks with a simple GraphQL query.

---

## 🔐 Authentication Choice

Due to **very limited time for implementation**, I used a **simple custom token-based authentication** instead of JWT.  
This helped me quickly set up authentication and focus on completing the core functionality (task management, permissions, and GraphQL integration).

✅ **Reasoning:**
- Fast to implement using Django models.
- No need for third-party setup.
- Perfect for quick proof-of-concept or assignment work.

🚀 **Future Plan:**
For production or enterprise-grade systems, I would use **JWT authentication** with:
- [`djangorestframework-simplejwt`](https://github.com/jazzband/djangorestframework-simplejwt), or  
- [`django-rest-knox`](https://github.com/James1345/django-rest-knox)

to ensure better scalability, token expiry/refresh, and improved security.

---

## 🚀 How to Run

### 1️⃣ Install dependencies
```bash
pip install django djangorestframework graphene-django
