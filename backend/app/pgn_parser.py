import re

class ParsedGame:
    def __init__(self):
        self.players = {"white": {}, "black": {}}
        self.tournament = {}
        self.game = {}
        self.moves = []
    # Add to ParsedGame class
    def to_dict(self):
        return {
            "players": self.players,
            "tournament": self.tournament,
            "game": self.game,
            "moves": self.moves,
        }

 

def parse_pgn(pgn_content):
    print("🔍 Full PGN content received:")
    print(pgn_content)

    games = []
    # Split by [Event to identify multiple games
    game_strings = re.split(r'(?=\[Event)', pgn_content.strip())
    print(f"📦 Total game blocks: {len(game_strings)}")

    for game_index, game_string in enumerate(game_strings):
        if not game_string.strip():
            continue

        print(f"\n🎯 Processing Game {game_index + 1}")

        # Split headers and moves by one or more blank lines
        parts = re.split(r'\n\s*\n', game_string.strip(), maxsplit=1)

        if len(parts) < 2:
            print("⚠️ Skipping game: Could not split headers and moves")
            continue

        header, moves_text = parts
        parsed_game = ParsedGame()

        # Extract headers
        headers = re.findall(r'\[(\w+)\s+"([^"]+)"\]', header)
        headers_dict = {key: value for key, value in headers}
        print(f"🧠 Extracted headers: {headers_dict}")

        parsed_game.players["white"]["name"] = headers_dict.get("White", "Unknown")
        parsed_game.players["black"]["name"] = headers_dict.get("Black", "Unknown")
        parsed_game.tournament["name"] = headers_dict.get("Event", "Unknown")
        parsed_game.tournament["site"] = headers_dict.get("Site", "Unknown")
        parsed_game.tournament["date"] = headers_dict.get("Date", "0000.00.00")

        # Handle ELO values safely
        white_elo = headers_dict.get("WhiteElo", "0")
        black_elo = headers_dict.get("BlackElo", "0")

        parsed_game.game["white_elo"] = int(white_elo) if white_elo.isdigit() else None
        parsed_game.game["black_elo"] = int(black_elo) if black_elo.isdigit() else None
        parsed_game.game["site"] = parsed_game.tournament["site"]
        parsed_game.game["result"] = headers_dict.get("Result", "*")
        parsed_game.game["termination"] = headers_dict.get("Termination", "Unknown")
        parsed_game.game["eco"] = headers_dict.get("ECO", "N/A")
        parsed_game.game["time_control"] = headers_dict.get("TimeControl", "Classical")
        parsed_game.game["link"] = headers_dict.get("Link", None)

        # Clean moves text: remove comments, annotations, result tokens
        cleaned_moves = re.sub(r'\{[^}]*\}', '', moves_text)  # Remove comments
        cleaned_moves = re.sub(r'\d+\.\.\.', '', cleaned_moves)  # Remove ... in notation
        cleaned_moves = re.sub(r'(1-0|0-1|1/2-1/2|\*)', '', cleaned_moves)  # Remove results
        cleaned_moves = re.sub(r'\s+', ' ', cleaned_moves).strip()  # Normalize whitespace

        moves = re.findall(r'(\d+)\.\s*([^\s]+)(?:\s+([^\s]+))?', cleaned_moves)
        print(f"♟️ Parsed moves: {moves}")

        for move_number, white_move, black_move in moves:
            parsed_game.moves.append({
                "move_number": int(move_number),
                "white_move": white_move.strip(),
                "black_move": black_move.strip() if black_move else None
            })

        games.append(parsed_game)

    return [game.to_dict() for game in games]
