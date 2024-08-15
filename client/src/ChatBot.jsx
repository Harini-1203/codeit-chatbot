// src/ChatBot.js
import React, { useState, useEffect, useRef } from 'react';
import io from 'socket.io-client';
import './ChatBot.css'; // Import your CSS styles

const ChatBot = () => {
    const [message, setMessage] = useState('');
    const [chatHistory, setChatHistory] = useState([]);
    const socketRef = useRef();
    const lastSentMessageRef = useRef('');

    useEffect(() => {
        socketRef.current = io('http://127.0.0.1:5000');

        socketRef.current.on('response', (responseMessage) => {
            setChatHistory((prevHistory) => [
                ...prevHistory,
                {
                    inp: lastSentMessageRef.current,
                    out: responseMessage,
                },
            ]);
        });

        return () => {
            if (socketRef.current) {
                socketRef.current.disconnect();
            }
        };
    }, []);

    const sendMessage = () => {
        const trimmedMessage = message.trim();
        if (trimmedMessage !== '') {

            lastSentMessageRef.current = trimmedMessage;
            socketRef.current.send(trimmedMessage);
            setMessage('');
        }
    };

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    };

    return (
        <div id="chat-page">
            <div id="chat-container">
                <div id="chat">
                    {chatHistory.map((chatEntry, index) => (
                        <div key={index} className="chat-entry">
                            <p className='you single-chat'><strong>You:</strong> {chatEntry.inp}</p>
                            <div className='bot-div single-chat'>
                                <img src="/images/bot.png"/>
                                <span className='bot single-chat'>{chatEntry.out}</span>
                            </div>
                        </div>
                    ))}
                </div>
                <div id="input-container">
                    <input
                        type="text"
                        id="input"
                        placeholder="Type your message..."
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        onKeyPress={handleKeyPress}
                    />
                    <button id="send" onClick={sendMessage}>
                        Send
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ChatBot;
