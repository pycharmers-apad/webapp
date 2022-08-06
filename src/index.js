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
import Projects from './components/Projects';
import ResourceManagement from './components/ResourceManagement';
import Cico from './components/checkincheckout';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
    <Route path='/'element={<Login />} />
    <Route exact path='/login/' element={<Login />} />
    <Route exact path='/signup/'element={<Signup />} />
    <Route exact path='/projects/' element={<Projects />} />
    <Route path='/projects/:id/resources/' element={<ResourceManagement />} />
    <Route path='/projects/:id/cico/' element={<Cico />} />
    </Routes>
  </BrowserRouter>    
);
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
