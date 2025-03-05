import React, { useState } from "react";
import axios from "axios";
import { FaEdit, FaSave, FaDownload } from "react-icons/fa";
import "./styles.css";

function App() {
    const [file, setFile] = useState(null);
    const [transcription, setTranscription] = useState("");
    const [editableTranscription, setEditableTranscription] = useState("");
    const [loading, setLoading] = useState(false);
    const [isEditing, setIsEditing] = useState(false);

    const handleFileUpload = async (e) => {
        const uploadedFile = e.target.files[0];
        setFile(uploadedFile);

        const formData = new FormData();
        formData.append("file", uploadedFile);

        setLoading(true);
        try {
        const response = await axios.post("http://localhost:8000/transcribe", formData, {
            headers: {
            "Content-Type": "multipart/form-data",
            },
        });
        setTranscription(response.data.transcription);
        setEditableTranscription(response.data.transcription);
        } catch (error) {
        console.error("Error transcribing audio:", error);
        } finally {
        setLoading(false);
        }
    };

    const handleEdit = () => {
        setIsEditing(true);
    };

    const handleSave = () => {
        setIsEditing(false);
        setTranscription(editableTranscription);
    };

    const handleDownload = () => {
        const blob = new Blob([transcription], { type: "text/plain" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "transcription.txt";
        a.click();
        URL.revokeObjectURL(url);
    };

    return (
        <div className="container">
        <h1>AI Scribe</h1>
        <input type="file" accept="audio/mp3" onChange={handleFileUpload} disabled={loading} />
        {loading && <p>Processing...</p>}
        {transcription && (
            <div className="transcription-container">
            <h2>Transcription:</h2>
            <div className="transcription-box">
                {isEditing ? (
                <textarea
                    value={editableTranscription}
                    onChange={(e) => setEditableTranscription(e.target.value)}
                    className="editable-textarea"
                />
                ) : (
                <p className="transcription-text">{transcription}</p>
                )}
            </div>
            <div className="button-container">
                {isEditing ? (
                <button onClick={handleSave} className="action-button">
                    <FaSave /> Save
                </button>
                ) : (
                <button onClick={handleEdit} className="action-button">
                    <FaEdit /> Edit
                </button>
                )}
                <button onClick={handleDownload} className="action-button">
                <FaDownload /> Download
                </button>
            </div>
            </div>
        )}
        </div>
    );
}

export default App;