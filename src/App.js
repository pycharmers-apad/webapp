import './App.css';
import React,{useState} from 'react';
 

function App(){

  // Returns the sing page as the home page
  return (
    <div className="container">
                    <nav className="navbar navbar-expand-lg navbar-light fixed-top">
          <div className="container">
            <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
              <ol className="navbar-nav ml-auto">
              <li><a href="./signup" >Sign Up   </a>   </li>
              <br></br>
              <li></li>
              <li><a style={{marginLeft: 5}} href="./login">  Login</a> </li>
              </ol>
            </div>
          </div>
        </nav>
  </div>
  )
}

export default App;
