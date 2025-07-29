# ♟️ Chess AI Coach

**Chess AI Coach** is a full-stack web application designed to help players improve their chess skills using real-time move analysis, PGN parsing, and Stockfish engine evaluation. The app provides a user-friendly interface for visualizing games and receiving coaching insights move-by-move.

---

## 🗂️ Project Structure

```

chess-ai-coach/
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI entry
│   │   ├── pgn_parser.py      # Cleans / validates PGN
│   │   ├── engine.py          # Stockfish wrapper
│   │   ├── analyzer.py        # Detect “missed best” moves
│   │   ├── explain.py         # Turn evals into friendly advice
│   │   └── models.py          # Pydantic schemas
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── components/
│   │   │   ├── PgnDrop.tsx
│   │   │   ├── Board.tsx        # chessboard.js viewer
│   │   │   └── AdvicePanel.tsx
│   │   ├── pages/
│   │   │   └── Home.tsx
│   │   └── services/
│   │       └── api.ts
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── package.json
└── README.md


````

---

## ⚙️ Features

- ✅ Upload PGN files and view game replay
- ✅ Move-by-move Stockfish evaluation and tips
- ✅ Beautiful interactive chessboard using React
- ✅ FastAPI backend for PGN parsing and engine analysis
- ✅ Modular, scalable TypeScript + Python architecture

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/chess-ai-coach.git
cd chess-ai-coach
````

---

### 2. Setup Backend (FastAPI)

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/macOS

pip install -r requirements.txt

# Run the FastAPI server
uvicorn app.main:app --reload
```

---

### 3. Setup Frontend (React + Vite)

```bash
cd ../frontend
npm install
npm run dev
```

Frontend will be available at `http://localhost:5173`
Backend will be running at `http://127.0.0.1:8000`

---

## 🧠 How It Works

* **Frontend** lets users upload and replay PGN games and sends moves to the backend.
* **Backend** uses Stockfish to evaluate each move and returns feedback.
* Built using `python-chess`, `FastAPI`, `Stockfish`, `React`, and `TypeScript`.

---

## 📦 Dependencies

### Backend

* `fastapi`
* `uvicorn`
* `python-chess`
* `stockfish` (as a subprocess)

### Frontend

* `react`
* `typescript`
* `vite`
* `chessboardjsx` or `react-chessboard` (for the board UI)

---

## 🛠️ Future Improvements

* 🔐 User authentication
* 💾 Save game history and analysis
* 📈 Analytics and performance tracking
* 🧠 Adaptive training routines

---

## 📃 License

This project is licensed under the MIT License.

---

## 🤝 Contributions

PRs and issues are welcome! If you’re interested in contributing, feel free to fork the repo and create a pull request.

---

## 🙋‍♂️ Author

Made with ❤️ by [MrMan](https://github.com/killa3241)

```

---

Let me know if you'd like to auto-fill your GitHub username, add usage screenshots, or deployment instructions!
```
