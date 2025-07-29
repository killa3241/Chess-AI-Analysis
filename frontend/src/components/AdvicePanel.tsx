import React from "react";

interface AdvicePanelProps {
  advice: string[];
}

const AdvicePanel: React.FC<AdvicePanelProps> = ({ advice }) => {
  return (
    <div>
      <h2>Coaching Advice</h2>
      <ul>
        {advice.map((line, idx) => (
          <li key={idx}>{line}</li>
        ))}
      </ul>
    </div>
  );
};

export default AdvicePanel;
