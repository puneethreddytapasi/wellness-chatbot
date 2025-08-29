# 🧘 Wellness Chatbot  

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white)  
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)  
![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)  

## 📌 Project Overview  
The **Wellness Chatbot** is a secure and user-friendly web application built with **Streamlit** and **SQLite**.  
It allows users to:  
✅ Register with personal details  
✅ Log in securely with authentication  
✅ Manage and update their profiles  
✅ Select preferred language (**English/Hindi**)  
✅ Change password after login  

This project demonstrates how Streamlit can be used to build not just dashboards but **full-fledged web apps with authentication and database integration**.  

---

## 🎯 Features  
- 🔐 **User Authentication** – Secure registration & login with password hashing  
- 👤 **Profile Management** – Update personal details (name, age, gender, language)  
- 🌐 **Multilingual Support** – English and Hindi interface  
- 🔑 **Password Management** – Change password securely  
- 🗄 **SQLite Database** – Persistent data storage  
- 🎨 **Modern UI/UX** – Clean, card-style design using Streamlit  

---

## 🛠 Tech Stack  
- **Frontend** → [Streamlit](https://streamlit.io/)  
- **Backend** → Python  
- **Database** → SQLite  
- **Authentication** → Passlib (SHA256 hashing)  

---

## 📂 Project Structure  

```bash
Wellness Chatbot/
│── backend/
│   └── auth.py          # Authentication & DB functions
│── database/
│   └── wellness.db      # SQLite database (auto-created)
│── frontend/
│   └── app.py           # Streamlit main application
│── venv/                # Virtual environment (ignored in GitHub)
│── README.md            # Project documentation
```

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/puneethreddytapasi/wellness-chatbot.git
```
### 2️⃣ Navigate to Project Folder
```bash
cd wellness-chatbot
```
### 3️⃣Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Mac/Linux
```
### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 5️⃣ Run the App
```bash
streamlit run frontend/app.py
```
## 👨‍💻 Author  
**Puneeth Reddy Tapasi**  
📌 [GitHub Profile](https://github.com/puneethreddytapasi)  

---

✨ *Feel free to fork, star ⭐, and contribute to improve this project!*  


