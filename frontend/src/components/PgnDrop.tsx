import React, { useState } from "react";
import { analyzePGN } from "../services/api";

interface PgnDropProps {
  onAdvice: (advice: string[]) => void;
  onFileUpload: (file: File) => void;
}

const PgnDrop: React.FC<PgnDropProps> = ({ onAdvice, onFileUpload }) => {
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    // Only accept .pgn files
    if (!file.name.toLowerCase().endsWith(".pgn")) {
      setError("Please upload a valid PGN (.pgn) file.");
      return;
    }

    setError(null);
    setUploading(true);

    try {
      const advice = await analyzePGN(file);
      console.log("Advice:", advice);

      if (Array.isArray(advice)) {
        onAdvice(advice);
      } else {
        onAdvice([]);
        setError("Invalid response format from server.");
      }

      onFileUpload(file);
    } catch (err) {
      console.error("PGN analysis failed:", err);
      setError("Failed to analyze PGN. Please try again.");
      onAdvice([]);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div style={{ marginTop: "1rem" }}>
      <h2>Upload PGN File</h2>
      <input
        type="file"
        accept=".pgn"
        onChange={handleFileChange}
        style={{ marginBottom: "1rem" }}
      />

      {uploading && <p style={{ color: "blue" }}>Analyzing your game...</p>}

      {error && (
        <p style={{ color: "red", fontWeight: "bold" }}>
          ⚠️ {error}
        </p>
      )}
    </div>
  );
};

export default PgnDrop;
