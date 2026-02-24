# 🤖 -Chat-with-database-

An AI-powered natural language to SQL application built with:

* 🧠 Google Gemini
* 🗄️ PostgreSQL
* ⚡ Streamlit
* 📊 Automatic Data Analysis
* 🧾 Schema-Aware Prompting

This project converts user questions into SQL queries, executes them securely, and generates intelligent summaries of the results.

---

## 📌 Overview

**Smart SQL Analyst Pro** allows users to interact with their database using natural language.

The system:

1. Extracts the database schema dynamically
2. Generates SQL queries using an LLM
3. Executes the query safely
4. Summarizes the results
5. Maintains chat history in session state

This is the **baseline version** that later evolved into a more advanced RAG-based system.

---

## 🏗️ Architecture

```id="a1b2c3"
User Question
      ↓
Schema Extraction
      ↓
LLM SQL Generation (Gemini)
      ↓
SQL Execution (PostgreSQL)
      ↓
Result Analysis by LLM
      ↓
Display Table + Summary
```

---

## ✨ Features

### 🔹 1. Schema-Aware SQL Generation

* Automatically reads database structure from `information_schema`
* Injects schema into prompt
* Ensures accurate table/column references

### 🔹 2. Dual LLM Calls

* First call → Generate SQL
* Second call → Summarize results

### 🔹 3. Secure Query Execution

* Uses SQLAlchemy
* Read-only style interaction
* Error handling included

### 🔹 4. Chat Memory

* Session-based conversation history
* Stores both text and data results

### 🔹 5. Clean Streamlit UI

* Interactive chat interface
* Automatic table rendering
* Professional layout

---

## 🛠️ Tech Stack

* Python
* Streamlit
* PostgreSQL
* SQLAlchemy
* Google Gemini (`gemini-2.5-flash`)
* Pandas
* Regex

---

## ⚙️ How It Works

### 1️⃣ Schema Extraction

The system queries:

```sql
SELECT table_name, column_name 
FROM information_schema.columns 
WHERE table_schema = 'public';
```

This ensures the LLM understands the database structure.

---

### 2️⃣ SQL Generation Prompting

The model is instructed to:

* Use double quotes
* Match exact column names
* Return SQL only
* Use proper JOIN logic

---

### 3️⃣ Execution & Analysis

After generating SQL:

* The query is executed
* Results are displayed
* The LLM summarizes insights
* Both are stored in session history

---

## 🚀 Example Use Cases

* Business analytics dashboards
* Sales reporting
* Customer insights
* Financial analysis
* Data exploration tools

---

## 🔐 Limitations (Baseline Version)

* No RAG enhancement
* No structured JSON output
* No intent classification
* No built-in security violation detection
* Uses prompt-only control

These improvements were later introduced in **Ultra SQL Agent**.

---

## 🔮 Future Improvements (Upgraded Version Includes)

* RAG with FAISS
* Structured output validation (Pydantic)
* Unified pipeline
* Security guardrails
* Persistent database memory
* Advanced session management

---

## 📁 Project Structure

```id="x9y8z7"
smart-sql-analyst/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🎯 Project Evolution

This project represents the **first generation** of an AI database assistant.

It served as the foundation for building a more advanced architecture with:

* Retrieval-Augmented Generation
* Structured JSON outputs
* Security layers
* Single-call unified processing
