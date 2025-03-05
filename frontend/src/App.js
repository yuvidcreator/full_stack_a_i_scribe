import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [inputText, setInputText] = useState("");
  const [outputText, setOutputText] = useState("");

  const handleTextSubmit = async () => {
    const response = await axios.post("http://localhost:8000/process-text", { text: inputText });
    setOutputText(response.data.output);
  };

  const handleVoiceSubmit = async (audioFile) => {
    const formData = new FormData();
    formData.append("file", audioFile);
    const response = await axios.post("http://localhost:8000/process-voice", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    setOutputText(response.data.output);
  };

  return (
    <div>
      <h1>AI Scribe</h1>
      <textarea value={inputText} onChange={(e) => setInputText(e.target.value)} />
      <button onClick={handleTextSubmit}>Submit Text</button>
      <input type="file" accept="audio/*" onChange={(e) => handleVoiceSubmit(e.target.files[0])} />
      <div>
        <h2>Output:</h2>
        <p>{outputText}</p>
      </div>
    </div>
  );
};

export default App;