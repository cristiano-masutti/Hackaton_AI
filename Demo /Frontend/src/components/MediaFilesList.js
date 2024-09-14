import React, { useState, useEffect } from 'react';
import './MediaFilesList.css'; // Import your CSS file

const MediaFilesList = () => {
    const [files, setFiles] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchFiles = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/media-files/');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                setFiles(data.files);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchFiles();
    }, []);

    if (loading) return <div className="loading">Loading...</div>;
    if (error) return <div className="error">Error: {error}</div>;

    return (
        <div className="media-files-list">
            <h1 className="header">Media Files</h1>
            <div className="files-container">
                {files.map((file, index) => (
                    <div key={index} className="file-card">
                        <div className="file-info">
                            <h3 className="file-name">{file.name}</h3>
                            <audio controls>
                                <source src={`data:audio/wav;base64,${file.data}`} type="audio/wav" />
                                Your browser does not support the audio element.
                            </audio>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default MediaFilesList;
