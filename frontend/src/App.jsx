import React, { useState } from "react";

export default function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:8000/predict", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div style={{
      background: "#0b0f1a",
      color: "white",
      minHeight: "100vh",
      padding: "30px"
    }}>
      <h1>MedPulse – Burnout Intelligence</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Analyze</button>

      {loading && <p>Processing...</p>}

      {result && (
        <div>
          <h2>Result</h2>
          <p>Level: {result.level}</p>
          <p>Confidence: {result.confidence}%</p>

          <h3>Features</h3>
          {Object.entries(result.features).map(([k, v]) => (
            <p key={k}>{k}: {v}</p>
          ))}

          <h3>Importance</h3>
          {Object.entries(result.importance).map(([k, v]) => (
            <p key={k}>{k}: {v}</p>
          ))}
        </div>
      )}
    </div>
  );
}
