import React, { useEffect, useState } from "react";

export default function App() {
  const [socket, setSocket] = useState(null);
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws");

    ws.onmessage = (event) => {
      setMessages((prev) => [...prev, event.data]);
    };

    setSocket(ws);
  }, []);

  const sendMessage = () => {
    socket.send("New burnout update");
  };

  return (
    <div style={{ background: "#0b0f1a", color: "white", minHeight: "100vh", padding: 20 }}>
      <h1>MedPulse Live Dashboard</h1>

      <button onClick={sendMessage}>Trigger Update</button>

      <div>
        {messages.map((msg, i) => (
          <p key={i}>{msg}</p>
        ))}
      </div>
    </div>
  );
}
