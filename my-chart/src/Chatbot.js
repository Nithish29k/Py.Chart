import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css"; // Ensure you add proper styles

const Chatbot = () => {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hi! I can help you schedule an appointment. What's your name?" }
  ]);
  const [userInput, setUserInput] = useState("");
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    fetchAppointments();
  }, []);

  const fetchAppointments = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:5000/appointments");
      setAppointments(res.data.appointments);
    } catch (error) {
      console.error("Error fetching appointments:", error);
    }
  };

  const handleSendMessage = async () => {
    if (!userInput.trim()) return;

    const newMessages = [...messages, { sender: "user", text: userInput }];
    setMessages(newMessages);

    try {
      const res = await axios.post("http://127.0.0.1:5000/chat", { message: userInput });
      setMessages([...newMessages, { sender: "bot", text: res.data.reply }]);
      
      // Fetch appointments after scheduling
      fetchAppointments();
    } catch (error) {
      setMessages([...newMessages, { sender: "bot", text: "❌ Error connecting to server." }]);
    }

    setUserInput("");
  };

  return (
    <div className="chat-container">
      <div className="chat-header">📅 Appointment Chatbot</div>
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <div className="chat-input">
        <input
          type="text"
          placeholder="Type your message..."
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
