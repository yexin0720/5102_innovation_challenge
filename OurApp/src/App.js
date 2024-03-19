import React, { useState } from 'react';
import { Button, Form, InputGroup } from 'react-bootstrap';
import { Search } from 'react-bootstrap-icons';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

import logo from './NCS Logo.jpeg'; 

function App() {
  const [response, setResponse] = useState({ message: '', imageUrl: '' });
  const [userInput, setUserInput] = useState('');

  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleSubmit = () => {
    // Send the user input to the backend via POST method
    fetch('/receive', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: userInput }),
    })
    .then(response => response.json())
    .then(data => setResponse({ message: data.message, imageUrl: data.imageUrl }))
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
        {response.message && <div className="response-message">The traffic condition is {response.message}</div>}
        {response.imageUrl && <img src={response.imageUrl} alt="Traffic" className="traffic-image" />}
        </div>

    </div>
  );
}

export default App;
