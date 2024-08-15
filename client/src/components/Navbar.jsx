import React from "react";
import './Navbar.css';

function Navbar(){
    return (
        <div className="nav">
        <img src="/images/codeit-logo.png" alt="logo"/>
        <nav>
            <a href>about</a>
            <a href>contanct</a>
        </nav>
        </div>
    );
}
export default Navbar;