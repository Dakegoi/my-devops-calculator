# 🧮 DevOps Calculator

This is a simple calculator app built using Python (Flask), HTML, JavaScript, Docker, and Nginx.

## Features
- Supports addition, subtraction, multiplication, and division operations.
- Frontend built with HTML and JavaScript.
- Backend using Flask (Python).
- Containerized using Docker.
- Nginx configured as a reverse proxy.

This is a simple web-based calculator built with **Python (Flask)** for the backend, **HTML/CSS/JavaScript** for the frontend, and **Nginx** as a reverse proxy. The project is containerized using Docker and orchestrated via Docker Compose.

---

## 🗂️ Tech Stack

- Python 3.9
- Flask
- HTML + JavaScript
- Nginx
- Docker & Docker Compose

---

## 📁 Project Structure

my-devops-calculator/
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend HTML
├── static/
│ └── script.js # Frontend JS
├── requirements.txt # Python dependencies
├── Dockerfile # Flask app container
├── nginx/
│ └── default.conf # Nginx reverse proxy config
├── docker-compose.yml # Multi-container definition


---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Dakegoi/my-devops-calculator.git
cd my-devops-calculator

       Build and run the containers:
docker-compose up --build
This command will build and start two connected containers:

calculator_app — Flask backend (internal port 5006)
nginx — Nginx reverse proxy (external port 81)
Nginx will forward all HTTP requests from localhost:81 to the Flask app.

![Screenshot](https://github.com/Dakegoi/my-devops-calculator/blob/main/Снимок%20экрана%202025-05-09%20в%2019.15.27.png)





