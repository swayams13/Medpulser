import { useState } from "react";

export default function App() {
  const [result, setResult] = useState(null);

  const testAPI = async () => {
    const res = await fetch(import.meta.env.VITE_API_URL + "/");
    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ background: "#0b0f1a", color: "white", height: "100vh", padding: 30 }}>
      <h1>MedPulse Live</h1>

      <button onClick={testAPI}>Test Backend</button>

      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}
