import React, { useState } from 'react';
import './App.css'; // Import your CSS file
import MediaFilesList from './components/MediaFilesList'; // Import your MediaFilesList component

const App = () => {
    const [isSidebarOpen, setSidebarOpen] = useState(false);

    const toggleSidebar = () => {
        setSidebarOpen(!isSidebarOpen);
    };

    return (
        <div className="app">
            <button className="menu-button" onClick={toggleSidebar}>
                {isSidebarOpen ? 'Close Menu' : 'Open Menu'}
            </button>
            <div className={`sidebar ${isSidebarOpen ? 'open' : ''}`}>
                <nav className="sidebar-nav">
                    <ul>
                        <li><a href="#home">Home</a></li>
                        <li><a href="#files">Files</a></li>
                        <li><a href="#settings">Settings</a></li>
                        <li><a href="#about">About</a></li>
                    </ul>
                </nav>
            </div>
            <div className={`main-content ${isSidebarOpen ? 'shifted' : ''}`}>
                <MediaFilesList />
            </div>
        </div>
    );
};

export default App;
