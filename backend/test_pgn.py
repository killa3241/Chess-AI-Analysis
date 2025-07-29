from app import pgn_parser
from app import analyzer
from app import explain

sample_pgn = """
[Event "Live Chess"]
[Site "Chess.com"]
[Date "2025.07.27"]
[Round "-"]
[White "mrman69429"]
[Black "Cornwallite"]
[Result "0-1"]
[CurrentPosition "5rk1/pb3pb1/1p2p1pp/8/3P4/1P4P1/PB1Q1PqP/4R1K1 w - - 6 25"]
[Timezone "UTC"]
[ECO "A00"]
[ECOUrl "https://www.chess.com/openings/Kings-Fianchetto-Opening-Sicilian-Invitation-2.Bg2"]
[UTCDate "2025.07.27"]
[UTCTime "11:27:25"]
[WhiteElo "1815"]
[BlackElo "1808"]
[TimeControl "60"]
[Termination "Cornwallite won by checkmate"]
[StartTime "11:27:25"]
[EndDate "2025.07.27"]
[EndTime "11:28:35"]
[Link "https://www.chess.com/analysis/game/live/141164265468/analysis"]
[WhiteUrl "https://images.chesscomfiles.com/uploads/v1/user/209222672.05213291.50x50o.04ca9f28bd10.jpg"]
[WhiteCountry "69"]
[WhiteTitle ""]
[BlackUrl "https://images.chesscomfiles.com/uploads/v1/user/62979170.fa3c9f66.50x50o.d649dbe8e15b.jpeg"]
[BlackCountry "2"]
[BlackTitle "NM"]

1. g3 c5 2. Bg2 d5 3. c3 Nf6 4. d4 cxd4 5. cxd4 Nc6 6. Nf3 g6 7. Nc3 Bg7 8. O-O
O-O 9. Re1 Bf5 10. Nh4 Be6 11. Nf3 h6 12. b3 Rc8 13. Bb2 b6 14. Rc1 Qd7 15. e4 $2
dxe4 16. Nxe4 Nxe4 17. Rxe4 Bd5 18. Re1 e6 $2 19. Ne5 Nxe5 20. Rxe5 $2 Rxc1 $1 21.
Bxc1 Bxg2 22. Re1 Bb7 23. Qd2 Qd5 24. Bb2 $2 Qg2# 0-1
"""

try:
    game = pgn_parser.parse_pgn(sample_pgn)
    print("PGN parsed successfully!")
    print("White player:", game.headers["White"])

    board = game.board()
    for move in game.mainline_moves():
        print("Move played:", board.san(move))
        board.push(move)

except Exception as e:
    print("Parsing failed:", e)

feedback = analyzer.find_missed_best_moves(game)
for f in feedback:
    print(f)


explained = explain.generate_advice(feedback)
print("\n--- Advice ---")
for line in explained:
    print(line)
