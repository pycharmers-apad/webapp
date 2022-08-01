import {useRef, useState, useEffect} from 'react';
import { useNavigate } from "react-router-dom";
import '../index.css'
import '/node_modules/bootstrap/dist/css/bootstrap.min.css'

const Signup=()=>{
const [username, setusername] = useState('');
const [password,setPassword]=useState('')
const [output,setOutput]=useState('')
const navigate=useNavigate()


const onSubmit = async (event) => { //Submit the event, and send the username and password to Flask
  event.preventDefault()
  console.log({username,password})  
  
  fetch('https://pycharmers-apad.herokuapp.com/api/signup/validate/', {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
           headers : {
          'Content-Type':'application/json'
           },
    body:JSON.stringify({username,password})}).then(response => response.json())
    .then(api =>setOutput(api["API-Signup-Response"]))
      

}
useEffect(()=>{
  if(output!==''){
  console.log(output)}
},[output])

return(  //Create a form and send it
<div className="auth-wrapper">
<div className="auth-inner">
        <div onSubmit={onSubmit}>
        <form>
          <h3>Signup- Pycharmers HaaS</h3>
        <div className="mb-3">
        <label>Username            </label>
        <input type='text'
        id='username'
        className="form-control"
        name='username'
        onChange={(e)=>setusername(e.target.value)}
        value={username} />
        </div>
        <div className="mb-3">
        <label>Password</label>
        <input type='password'
        className="form-control"
        id='password'
        name='password'
        onChange={(e)=> setPassword(e.target.value)} 
        value={password} />
        </div>
        <div className="d-grid">
        <input type='submit' value='Login'  className="btn btn-primary"/>
        </div>
        <br></br>
        <p className="forgot-password text-right">
               Existing user? <a href='http://localhost:5000/login/'>Sign In</a>
               </p>
    </form>
    </div>
    </div>
    </div>
    )
}
export default Signup