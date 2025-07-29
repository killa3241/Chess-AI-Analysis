import chess
import chess.engine
from .engine import get_best_move, STOCKFISH_PATH

def find_missed_best_moves(game):
    """
    Analyzes a PGN game and compares each move with Stockfish's best move.
    Returns feedback on suboptimal moves.
    """
    board = game.board()
    feedback = []

    try:
        with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
            move_number = 1
            for move in game.mainline_moves():
                best_move = get_best_move(engine, board, depth=10)

                if move != best_move:
                    played_san = board.san(move)
                    best_san = board.san(best_move)
                    feedback.append(
                        f"Move {move_number}: You played {played_san}, but the best move was {best_san}."
                    )

                board.push(move)
                move_number += 1
    except Exception as e:
        feedback.append(f"Analysis failed: {str(e)}")

    return feedback


def analyze_game(moves: list):
    """
    Analyzes a list of moves from JSON (non-PGN) using Stockfish.

    Args:
        moves (list): List of dictionaries like:
            [{"move_number": 1, "white_move": "e4", "black_move": "e5"}, ...]

    Returns:
        list: Feedback on suboptimal or invalid moves.
    """
    board = chess.Board()
    advice = []

    try:
        with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
            for move in moves:
                move_number = move.get("move_number", "?")
                user_move = move.get("white_move") if board.turn == chess.WHITE else move.get("black_move")

                if user_move:
                    try:
                        parsed_move = board.parse_san(user_move)
                        best_move = get_best_move(engine, board)

                        if parsed_move != best_move:
                            advice.append(
                                f"Move {move_number}: You played {user_move}, but the best move was {board.san(best_move)}."
                            )
                        board.push(parsed_move)
                    except Exception:
                        advice.append(f"Move {move_number}: Invalid move format: '{user_move}'")
    except Exception as e:
        advice.append(f"Engine setup failed: {str(e)}")

    return advice
