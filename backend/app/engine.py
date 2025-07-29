import chess
import chess.engine
import os

# Update this path to where Stockfish is located on your machine
STOCKFISH_PATH = r"D:\Coding\stockfish\stockfish-windows-x86-64-avx2.exe"

def load_engine():
    if not os.path.exists(STOCKFISH_PATH):
        raise FileNotFoundError(f"⚠️ Stockfish not found at path: {STOCKFISH_PATH}")
    
    return chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

def get_best_move(engine, board: chess.Board, depth=10):
    """
    Analyze the given board and return the best move according to Stockfish.
    
    :param engine: A running chess.engine.SimpleEngine instance
    :param board: A chess.Board object
    :param depth: Search depth (default 10)
    :return: chess.Move object representing the best move
    """
    result = engine.analyse(board, chess.engine.Limit(depth=depth))
    return result["pv"][0]
