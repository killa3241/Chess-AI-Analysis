from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import chess.pgn
import io

from app.pgn_parser import parse_pgn
from app.analyzer import find_missed_best_moves

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        content = await file.read()
        decoded = content.decode("utf-8")
        game = chess.pgn.read_game(io.StringIO(decoded))

        if not game:
            return {"error": "Could not parse PGN. Check the format."}

        feedback = find_missed_best_moves(game)
        return {"analysis": feedback}

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}

@app.post("/parse-pgn")
async def parse_pgn_endpoint(file: UploadFile = File(...)):
    try:
        content = await file.read()
        decoded = content.decode("utf-8")
        games = parse_pgn(decoded)
        return {"parsed_games": games}
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}
