import React, { useState } from "react";

export default function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const upload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);

    const res = await fetch("http://localhost:8000/predict", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div style={{ background: "#0b0f1a", color: "white", minHeight: "100vh", padding: 30 }}>
      <h1>MedPulse – AI Burnout System</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={upload}>Analyze</button>

      {loading && <p>Extracting features...</p>}

      {result && (
        <div>
          <h2>{result.level}</h2>
          <p>Confidence: {result.confidence}%</p>

          <h3>Explainability</h3>
          {Object.entries(result.importance).map(([k, v]) => (
            <p key={k}>{k}: {v}</p>
          ))}
        </div>
      )}
    </div>
  );
}
