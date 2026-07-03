<div align="center">

# 🚀 ResearchFlow AI

### 📚 **AI-Powered Research Paper Analysis, Summarization & Comparison Platform**

Transform lengthy research papers into **clear insights**, **structured summaries**, **comparative analysis**, and an **interactive AI-powered research assistant**.

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)
![Firecrawl](https://img.shields.io/badge/Firecrawl-Web%20Scraping-orange?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-red?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge\&logo=google)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

**✨ Analyze • Summarize • Compare • Discover**

</div>

---

# 📑 Table of Contents

* 🌟 Overview
* ✨ Features
* ⚙️ Tech Stack
* 🏗️ Project Structure
* 🚀 Installation
* 🔐 Environment Variables
* 💻 Usage
* 🌐 Deployment
* 🛣️ Future Improvements
* 📄 License
* 👨‍💻 Developer

---

# 🌟 Overview

ResearchFlow AI is a **high-performance AI-powered research assistant** designed for **students, researchers, engineers, and professionals**.

Instead of spending hours reading lengthy research papers, simply provide the **URL of a research paper**, and ResearchFlow AI intelligently extracts the content, summarizes the paper, identifies its key contributions, compares multiple papers, and even lets you chat with the research using AI.

Powered by **Firecrawl**, **Groq Llama-3.3-70B**, and **Google Gemini Flash**, the application dramatically accelerates literature reviews by automatically identifying:

* 📌 Problem Statements
* 🧠 Methodology
* 📊 Results
* 💡 Key Contributions
* 📈 Evolution of Research
* 🔍 Research Gaps

---

# ✨ Features

## 🔐 Secure Authentication

* ✅ Passwordless Email Authentication
* ✅ Secure OTP Verification
* ✅ Simple and seamless login experience

---

## 📄 Automated Research Scraping

Paste any supported research paper URL and let **Firecrawl** extract clean markdown automatically.

✔ Academic Articles

✔ Research Papers

✔ Technical Documentation

---

## 🤖 AI-Powered Research Synthesis

Every paper is automatically analyzed into structured sections:

### 📝 Summary

* Main problem statement
* Research objectives

### 🧠 Methodology

* Algorithms
* Frameworks
* Models
* Datasets

### 📊 Results

* Key findings
* Benchmarks
* Experimental outcomes

### 💡 Contributions

* Novel ideas
* Major innovations
* Important takeaways

### 📈 Evolutionary Context

Understand how the paper compares with previous research and how the field has evolved.

### 🔍 Research Gaps

Discover:

* Current limitations
* Weaknesses
* Potential future work

---

## 📊 Comparative Analysis

Compare multiple research papers side-by-side to quickly identify differences in:

* Methodology
* Results
* Contributions
* Evolution
* Research Direction

---

## 💬 Interactive AI Chatbot

Ask natural language questions directly about the selected paper.

Examples:

> "What dataset was used?"

> "Explain the methodology."

> "What are the limitations?"

The chatbot answers using the paper's extracted content as context.

---

## 📈 Analytics Dashboard

Monitor your research activity through:

* 📚 Total Papers
* 📅 Reading Timeline
* 📝 Total Word Count
* 🆕 Latest Discovery

---

# ⚙️ Tech Stack

| Category         | Technology                     |
| ---------------- | ------------------------------ |
| 🖥 Backend       | FastAPI (Python 3.10+)         |
| 💾 Database      | SQLite + SQLAlchemy            |
| 🌐 Web Scraping  | Firecrawl Python SDK           |
| 🤖 Primary LLM   | Groq (Llama-3.3-70B-Versatile) |
| ✨ Fallback LLM   | Google Gemini Flash            |
| 🎨 Frontend      | HTML5, CSS3, JavaScript (ES6+) |
| 📧 Email Service | SMTP (`smtplib`)               |

---

# 🏗️ Project Structure

<details>

<summary><strong>📂 Click to Expand</strong></summary>

```text
.
├── backend/
│   ├── database.py
│   ├── email_service.py
│   ├── firecrawl_service.py
│   ├── llm_service.py
│   ├── main.py
│   └── models.py
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   ├── login.html
│   ├── login.js
│   └── style.css
│
├── requirements.txt
└── memento.db
```

</details>

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

> **⚠️ Important**
>
> Create a `.env` file in the project root and configure the following variables.

```env
# LLM API Keys
GROQ_API_KEY=gsk_your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here

# Firecrawl
FIRECRAWL_API_KEY=fc-your_firecrawl_api_key_here

# SMTP Configuration
EMAIL_HOST=smtp.yourprovider.com
EMAIL_PORT=465
EMAIL_USER=your_email@domain.com
EMAIL_PASS=your_secure_email_app_password
SENDER_EMAIL=your_email@domain.com
```

> 🚫 Never commit your actual `.env` file or API keys to GitHub.

---

# 💻 Usage

## ▶ Start the Server

```bash
uvicorn backend.main:app --reload
```

Open:

```text
http://localhost:8000
```

### Workflow

1. 📧 Verify your email using OTP.
2. 🌐 Paste a research paper URL.
3. 🤖 Click **Analyze**.
4. 📚 Read the AI-generated summary.
5. 📊 Compare multiple papers.
6. 💬 Chat with the paper using the built-in AI assistant.

---

# 🌐 Deployment

ResearchFlow AI can be deployed on platforms such as:

* 🚀 Render
* ☁️ AWS Elastic Beanstalk
* 🐳 Docker
* 🌍 Any FastAPI-compatible cloud service

### Notes

* SQLite (`memento.db`) is suitable for local development.
* For production, consider using a persistent database.
* Configure all environment variables through your cloud provider before deployment.
* The frontend is served directly by FastAPI on the same port.

---

# 🛣️ Future Improvements

* ⬜ PDF & DOCX Upload Support
* ⬜ Multiple LLM Selection
* ⬜ Citation Network Visualization
* ⬜ Keyword Trend Analytics
* ⬜ Research Folder Management
* ⬜ Multi-User Collaboration
* ⬜ Bookmark Collections
* ⬜ Enhanced Dashboard Analytics

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Developer

**Balaiah Dongala**

📧 **Email:** [balaiah_dongala@srmap.edu.in](mailto:balaiah_dongala@srmap.edu.in)

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

**Built with ❤️ using FastAPI, Firecrawl, Groq & Google Gemini**

</div>
