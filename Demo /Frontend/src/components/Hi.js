import React from "react";

const SendText = () => {
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:8000/api/send-text/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: "hi" }), // Sending 'hi' as text
      });

      const data = await response.json(); // Parse JSON response
      if (response.ok) {
        console.log("Server response:", data.message); // Log message to frontend console
      } else {
        console.error("Server error:", data.error); // Log error message to frontend console
      }
    } catch (error) {
      console.error("Fetch error:", error); // Log fetch error to frontend console
    }
  };

  return (
    <div>
      <h1>Send Text</h1>
      <form onSubmit={handleSubmit}>
        <button type="submit">Send 'hi'</button>
      </form>
    </div>
  );
};

export default SendText;
