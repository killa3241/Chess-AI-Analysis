import React, { useState } from "react";
import BoardViewer from "./components/BoardViewer"; // adjust the path as needed
import "./styles/chessboard.css";

function App() {
  const [pgn, setPgn] = useState<string>("");

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const fileContent = event.target?.result as string;
      setPgn(fileContent.trim());
    };
    reader.readAsText(file);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1>♟️ Chess AI Coach</h1>

      <div style={{ marginBottom: "1rem" }}>
        <label htmlFor="pgnUpload" style={{ marginRight: "1rem" }}>
          Upload PGN File:
        </label>
        <input type="file" accept=".pgn" onChange={handleFileUpload} id="pgnUpload" />
      </div>

      {pgn ? (
        <BoardViewer pgn={pgn} />
      ) : (
        <p style={{ marginTop: "2rem", color: "gray" }}>No PGN file uploaded yet.</p>
      )}
    </div>
  );
}

export default App;
