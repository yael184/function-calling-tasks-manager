# 🚀 Function Calling Task Manager (Gemini 2.5 Flash)

A sophisticated AI-powered task management system that allows you to manage your schedule using **Natural Language**. Built with **FastAPI**, **FullCalendar**, and **Google Gemini 2.5 Flash**.

## ✨ Key Features
- **AI Agentic Workflow**: Uses Gemini's Function Calling to bridge human language and structured data.
- **Data Persistence**: Automatically saves and loads tasks from a local tasks.json database.
- **Modern Dashboard**: Features a real-time interactive calendar and a sleek chat interface.
- **Smart Date Parsing**: Understands relative dates like "next Sunday" or "tomorrow morning".

## 🛠️ Tech Stack
- **Backend**: Python, FastAPI, Uvicorn
- **AI Engine**: Google GenAI SDK (Gemini 2.5 Flash)
- **Frontend**: Tailwind CSS, FullCalendar JS
- **Storage**: Local JSON Persistence

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
git clone https://github.com/yael184/function-calling-tasks-manager.git
cd function-calling-tasks-manager

### 2. Set Up Virtual Environment (venv)
It is recommended to run this project in a virtual environment:

**Windows:**
python -m venv venv
.\venv\Scripts\activate

**Mac/Linux:**
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
Once the environment is active, install the required packages:
pip install -r requirements.txt

### 4. Configuration
The project requires a Gemini API Key. 

1. Copy the example environment file:
cp .env.example .env

2. Open the .env file and paste your API key:
GEMINI_API_KEY=your_actual_api_key_here

### 5. Run the Project
Start the FastAPI server:
python main.py

Then, open your browser at: http://localhost:8000

---

## 📁 Project Overview
- main.py: The entry point. Handles routing and serves the frontend.
- agent_service.py: The "Brain". Orchestrates Gemini 2.5 and manages function execution.
- todo_service.py: The "Data Layer". Handles all CRUD operations on the tasks.json file.
- index.html: The interactive UI.
- requirements.txt: List of Python libraries needed.
- .env.example: Template for environment variables.

## 🤖 How it works
The agent follows a Manual Tool-Calling Loop:
1. User Request: "Remind me to call the bank this Tuesday."
2. Analysis: Gemini 2.5 Flash recognizes the create_new_task tool.
3. Execution: The backend calculates the date and writes to tasks.json.
4. Natural Response: The AI confirms: "Sure! I've scheduled your call for March 3rd."

---
Created with ❤️ by YAEL