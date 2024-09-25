import React from 'react';
import logo from './logo.svg';
import './App.css';
import DetectOS from './Components/DetectOS/';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <DetectOS/>
      </header>
    </div>
  );
}

export default App;
