# 🤖 Multi-Agent AI Research Assistant

## 📌 Overview

Multi-Agent AI Research Assistant is an AI-powered system that uses multiple autonomous agents to transform a user query into a structured and meaningful report.

Instead of relying on a single AI response, the system divides the task among specialized agents. Each agent performs a specific role, improving organization, reasoning, and output quality.

The system demonstrates an agent-based workflow with planning, information retrieval, analysis, and report generation.

---

# ✨ Features

* 🔹 Multi-agent AI workflow
* 🔹 Task planning and execution
* 🔹 Specialized AI agents for different responsibilities
* 🔹 Real-time streaming response display
* 🔹 Structured final report generation
* 🔹 Agent-wise output visualization
* 🔹 Error handling with fallback responses
* 🔹 Simple web-based interface

---

# 🏗️ System Architecture

```
                User Query
                    |
                    ↓
            Planner Agent
                    |
                    ↓
           Retriever Agent
                    |
                    ↓
           Analyzer Agent
                    |
                    ↓
            Writer Agent
                    |
                    ↓
             Final Report
```

## Agent Responsibilities

### 📋 Planner Agent

* Understands the user requirement
* Breaks the task into smaller steps
* Creates the execution workflow

### 🔍 Retriever Agent

* Collects required information
* Provides relevant facts and data

### 📊 Analyzer Agent

* Processes retrieved information
* Identifies important points
* Creates summaries and insights

### ✍️ Writer Agent

* Converts analysis into a structured report
* Generates final readable output

---

# 🛠️ Technology Stack

## Backend

* Python
* Flask

## Frontend

* HTML
* CSS
* JavaScript

## AI Architecture

* Multi-Agent System
* LLM-based reasoning workflow

---

# 📂 Project Structure

```
AI-Agent-System/

│
├── app.py                  # Flask application
├── executor.py             # Agent execution workflow
├── requirements.txt        # Dependencies
│
├── agents/
│   │
│   ├── planner.py          # Planning agent
│   ├── retriever.py        # Retrieval agent
│   ├── analyzer.py         # Analysis agent
│   └── writer.py           # Writing agent
│
├── templates/
│   └── index.html          # Frontend interface
│
├── docs/
│   ├── system_design.md
│   └── postmortem.md
│
└── README.md
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone <repository-link>
```

## 2. Navigate to Project Folder

```bash
cd AI-Agent-System
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Application

```bash
python app.py
```

## 5. Open in Browser

```
http://127.0.0.1:5000
```

---

# 🚀 How It Works

1. User enters a task/query through the web interface.

2. Flask receives the request.

3. Planner Agent creates the execution plan.

4. Executor runs agents in sequence.

5. Retriever collects information.

6. Analyzer processes the information.

7. Writer generates the final report.

8. The result is displayed in the browser.

---

# 🧪 Example

### Input

```
Predict a future fashion trend in Tokyo after 5 years
```

### Output Flow

```
Planner Agent
        ↓
Retriever Agent
        ↓
Analyzer Agent
        ↓
Writer Agent
        ↓
Final Generated Report
```

---

# 📄 Documentation

Detailed project documentation:

* System Architecture:
  `docs/system_design.md`

* Development Reflection:
  `docs/postmortem.md`

---

# 🔮 Future Improvements

* Parallel agent execution
* Database storage
* Better agent memory
* User authentication
* Cloud deployment
* Advanced monitoring system

---

# 🎯 Project Objective

The goal of this project is to demonstrate how multiple AI agents can collaborate to solve complex tasks by dividing responsibilities and producing better structured outputs compared to a single-agent approach.

---

## Demo Video

System demonstration video:
[Watch Demo Video](https://drive.google.com/file/d/1auKI4sLeLsI_wz2aF9nYdlUezR1J5tqT/view?usp=sharing)

---

# 👩‍💻 Author

Lathashree
