# Exam Seat Planner

A minimal, fast, and feature-rich Exam Seat Planner web application built with Python and Flask. This application helps administrators add classrooms and automatically allocate seats to students based on an optimized logic that prefers lower floors and uses the minimum number of rooms necessary.

---

## 🚀 Features

- **Room Management**: Add classrooms with custom IDs, capacity, floor number, and washroom proximity.
- **Optimized Allocation**: Automatically allocate the best possible rooms for a given number of students. Lower floors and maximum capacities are prioritized.
- **In-Memory Storage**: Runs instantly without out-of-the-box configuration using a Python list as a lightweight in-memory database.
- **Validation & Error Handling**: Robust checking for invalid input, negative values, and duplicate room IDs.
- **Vercel Ready**: Pre-configured with Serverless settings (`vercel.json` and `index.py`) for instantaneous deployment.

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, Vanilla CSS, Jinja Templates
- **Deployment**: Vercel Serverless Functions

---

## 💻 How to Run Locally

### Prerequisites
Make sure you have [Python 3.7+](https://www.python.org/downloads/) installed.

### Setup Instructions

1. **Clone the project** (or download the source):
   ```bash
   cd exam-seat-planner
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

The application will now be running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## 🔗 Deployment

This application comes pre-configured for Vercel. You can easily deploy it using the Vercel CLI:

```bash
vercel deploy
```

**Live Link**: 
> [https://seat-planner-wine.vercel.app/](https://seat-planner-wine.vercel.app/)

---
