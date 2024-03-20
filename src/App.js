import React, { useState, useEffect } from 'react';
import { Button, Form, InputGroup } from 'react-bootstrap';
import { Search } from 'react-bootstrap-icons';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

import logo from './NCS Logo.jpeg';

function App() {
  const [response, setResponse] = useState({ message: '', imageUrl: '' });
  const [displayedMessage, setDisplayedMessage] = useState('');
  const [userInput, setUserInput] = useState('');

  useEffect(() => {
    const animateMessage = (index = 0) => {
      if (index < response.message.length) {
        setDisplayedMessage((prev) => prev + response.message.charAt(index));
        setTimeout(() => animateMessage(index + 1), 50); // Adjust the speed as needed
      }
    };

    if (response.message) {
      setDisplayedMessage(''); // Reset displayed message before starting
      animateMessage(); // Start animating
    }
  }, [response.message]); // This effect depends on the response.message

  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleSubmit = () => {
    fetch('/receive', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: userInput }),
    })
    .then(response => response.json())
    .then(data => {
      const timestamp = new Date().getTime();
      const uncachedImageUrl = data.imageUrl + `?t=${timestamp}`;
      setResponse({ message: data.message, imageUrl: uncachedImageUrl });
    })
    .catch(error => console.error('Error:', error));
  };


  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to OurApp!</h1>
      </header>
      <img src={logo} alt="Logo" className="App-logo" />

      <div className="App-body">
        <InputGroup className="mb-3 input-group">
          <Form.Control 
            type="text" 
            placeholder="Ask anything about traffic at a location" 
            value={userInput} 
            onChange={handleInputChange}
          />
          <Button variant="primary" onClick={handleSubmit}>
            <Search />
          </Button>
        </InputGroup>
        {displayedMessage && <div className="response-message">{displayedMessage}</div>}
        {response.imageUrl && <img src={response.imageUrl} alt="Traffic" className="traffic-image" />}
      </div>
    </div>
  );
}

export default App;