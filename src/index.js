import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Login from './components/Login';
import Signup from './components/Signup';
import { BrowserRouter,
  Routes,
  Route} from "react-router-dom";
import Welcome from './components/Welcome';
import ProtectedRoute from './ProtectedRoute';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
    <Route path='/'element={<App />} />
    <Route exact path='/Login/' element={<Login />} />
    <Route exact path='/Signup/'element={<Signup />} />
    <Route exact path='/welcome/' element={<Welcome/>} />
    </Routes>
  </BrowserRouter>    
);
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
