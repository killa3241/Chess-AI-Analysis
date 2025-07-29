import chess
from app import engine

board = chess.Board()
best = engine.get_best_move(board)
print("Best move:", board.san(best))
