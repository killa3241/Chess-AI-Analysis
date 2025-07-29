import React, { useState } from "react";
import PgnDrop from "../components/PgnDrop";
import AdvicePanel from "../components/AdvicePanel";
import BoardViewer from "../components/BoardViewer";

const Home: React.FC = () => {
  const [advice, setAdvice] = useState<string[]>([]);
  const [pgn, setPgn] = useState<string>("");

  const handleUpload = async (file: File) => {
    const text = await file.text();
    setPgn(text);
  };

  return (
    <div>
      <PgnDrop
        onAdvice={(data) => setAdvice(data ?? [])} // Ensure it's never undefined
        onFileUpload={handleUpload}
      />
      {pgn && <BoardViewer pgn={pgn} />}
      {Array.isArray(advice) && advice.length > 0 && <AdvicePanel advice={advice} />}
    </div>
  );
};

export default Home;
