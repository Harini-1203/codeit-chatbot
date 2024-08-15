import React from "react";
import './Landing.css';
import { Link } from "react-router-dom";

function Landing(){
    return (
        <div className="landing">
            <div className="landing-info">
                <h1>Welcome to CodeIt: Your Interactive HTML/CSS Code Generator</h1>
                <p>CodeIt empowers you to create HTML/CSS code snippets effortlessly. Engage in an interactive chat to generate custom code for various web components, enhancing your development process.</p>
                <Link to='/chatbot'>
                <button class="button-22" role="button">START CHAT</button>
                </Link>
            </div>
            <img src="/images/Landingbot.png" alt="bot"/>

        </div>
    );
}
export default Landing;