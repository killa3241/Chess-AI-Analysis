import React, { useState, useEffect } from "react";
import { Chess } from "chess.js";
import { Chessboard } from "react-chessboard";

interface BoardViewerProps {
  pgn: string;
}

const BoardViewer: React.FC<BoardViewerProps> = ({ pgn }) => {
  const [game, setGame] = useState(new Chess());
  const [fen, setFen] = useState(game.fen());
  const [moveIndex, setMoveIndex] = useState(0);
  const [moves, setMoves] = useState<string[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    try {
      const newGame = new Chess();
      newGame.loadPgn(pgn); // will throw if invalid PGN

      const history = newGame.history();
      newGame.reset();

      setGame(newGame);
      setMoves(history);
      setMoveIndex(0);
      setFen(newGame.fen());
      setError(null);
    } catch (err) {
      console.error("Failed to load PGN:", err);
      setGame(new Chess());
      setFen(new Chess().fen());
      setMoves([]);
      setMoveIndex(0);
      setError("⚠️ Invalid PGN file. Please upload a valid game.");
    }
  }, [pgn]);

  const goToMove = (index: number) => {
    const tempGame = new Chess();
    for (let i = 0; i < index; i++) {
      tempGame.move(moves[i]);
    }
    setFen(tempGame.fen());
    setMoveIndex(index);
  };

  const nextMove = () => {
    if (moveIndex < moves.length) {
      goToMove(moveIndex + 1);
    }
  };

  const prevMove = () => {
    if (moveIndex > 0) {
      goToMove(moveIndex - 1);
    }
  };

  if (error) {
    return (
      <div style={{ marginTop: "2rem", color: "red", textAlign: "center", fontWeight: "bold" }}>
        {error}
      </div>
    );
  }

  if (moves.length === 0) {
    return (
      <div style={{ marginTop: "2rem", color: "gray", textAlign: "center" }}>
        No moves to display.
      </div>
    );
  }

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", marginTop: "2rem" }}>
      <div style={{ width: "100%", maxWidth: "500px", aspectRatio: "1 / 1" }}>
        <Chessboard position={fen} arePiecesDraggable={false} boardWidth={500} />
      </div>

      <div style={{ marginTop: "1rem", textAlign: "center" }}>
        <button onClick={prevMove} disabled={moveIndex === 0} style={{ marginRight: "1rem" }}>
          ◀️ Previous
        </button>
        <button onClick={nextMove} disabled={moveIndex >= moves.length}>
          ▶️ Next
        </button>
        <p style={{ marginTop: "0.5rem" }}>
          Move {moveIndex}/{moves.length}
        </p>
      </div>
    </div>
  );
};

export default BoardViewer;
