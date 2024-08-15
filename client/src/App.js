
import './App.css';
import ChatBot from './ChatBot';
import Home from './Home';
import { BrowserRouter,Route,Routes } from 'react-router-dom';
import React, { useRef } from 'react';

function App() {
  return (
<BrowserRouter>
    <Routes>
      <Route path='/' element={<Home />}></Route>
      <Route path='/chatbot' element={<ChatBot />}></Route>
    </Routes>
  </BrowserRouter>
  );
}

export default App;
