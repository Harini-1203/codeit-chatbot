import React from "react";
import Navbar from "./components/Navbar";
import Landing from "./components/Landing";
import './Home.css';
function Home(){
    return (
        <div className="home">
            <Navbar />
            <Landing /> 
        </div>
    );
}
export default Home