# 🚀 Fullstack Todo App

A production-style full-stack Todo application built using modern web technologies.

This project demonstrates:

- Backend API development with FastAPI  
- Database integration with PostgreSQL  
- ORM usage with SQLAlchemy  
- Frontend development with React (Vite)  
- RESTful architecture  
- Full CRUD operations  
- Proper Git workflow and project structuring  

---

## 🛠 Tech Stack

### Backend
- FastAPI  
- SQLAlchemy  
- PostgreSQL  
- Uvicorn  

### Frontend
- React  
- Vite  
- Axios  

---

## ✨ Features

- Create tasks  
- View all tasks  
- Mark tasks as completed  
- Delete tasks  
- Persistent database storage  
- RESTful API endpoints  
- Full frontend-backend integration  

---

## 🏗 Architecture Overview

Frontend (React + Axios)
        ↓
FastAPI Backend (REST API)
        ↓
SQLAlchemy ORM
        ↓
PostgreSQL Database

- React communicates with FastAPI via HTTP requests.  
- FastAPI handles business logic.  
- SQLAlchemy manages database interactions.  
- PostgreSQL stores persistent data.  

---

## 📂 Project Structure

back/       → FastAPI backend  
frontend/   → React frontend  
.gitignore  
README.md  

---

## 🔗 API Endpoints

| Method | Endpoint        | Description              |
|--------|----------------|--------------------------|
| POST   | /todo          | Create a new task        |
| GET    | /todo          | Get all tasks            |
| PUT    | /todo/{id}     | Mark task as completed   |
| DELETE | /todo/{id}     | Delete a task            |

Interactive API docs available at:

http://127.0.0.1:8000/docs

---

## ▶️ How To Run Locally

### Backend Setup

cd back  
python -m venv .venv  
.venv\Scripts\Activate.ps1  
pip install -r requirements.txt  
uvicorn main:app --reload  

Backend runs on:

http://127.0.0.1:8000

---

### Frontend Setup

cd frontend  
npm install  
npm run dev  

Frontend runs on:

http://localhost:5173

---

## 🧪 Environment Requirements

- Python 3.10+  
- Node.js (LTS)  
- PostgreSQL (running on port 5432)  

---

## 📈 What This Project Demonstrates

- Full-stack integration  
- REST API design  
- Database modeling  
- State management in React  
- CORS handling  
- Clean Git workflow  
- Real-world development setup  

---

## 🚀 Future Improvements

- Authentication (JWT-based login system)  
- User-specific tasks  
- UI improvements (Tailwind CSS)  
- Docker containerization  
- Deployment (Render / Railway / Vercel)  
- CI/CD pipeline  

---

## 📌 Author
Built as a learning-focused full-stack project to demonstrate backend and frontend integration using modern web technologies.