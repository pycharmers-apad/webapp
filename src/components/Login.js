import {useRef, useState, useEffect} from 'react';
import { useNavigate } from "react-router-dom";
import '../index.css'
import '/node_modules/bootstrap/dist/css/bootstrap.min.css'


const Login=()=>{
const [username, setusername] = useState('');
const [password,setPassword]=useState('')
const [userAuth,setuserAuth]=useState('default')
const navigate=useNavigate()


  const onSubmit = async (event) => { //Submit the event, and send the username and password to Flask
    event.preventDefault()
    console.log({username,password})
    setuserAuth('default')
	  
	  await fetch('https://pycharmers-apad.herokuapp.com/api/login/auth/', {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
             headers : {
            'Content-Type':'application/json'
             },
      body:JSON.stringify({username,password})}).then(response => response.json())
      .then(api =>setuserAuth(api["authentication"]))
//then(response => response.json()).then(api =>setOutput(api[‘APIresponse’]))
      

      //await (fetch('http://localhost:5000/api/login/auth/',
      //{method: 'GET',
      //headers: {
        //'Access-Control-Allow-Origin':'*'
      //}})
      //.then(response=>response.json())
      //.then(data=>setuserAuth(data['authetication'])))
        
}
useEffect(()=>{
  if(userAuth!='default' && userAuth!='1'){
    if(userAuth=='great success')
    {
    console.log('success')
    setuserAuth('default')
    navigate('/projects')
	
  } 
  else{
    if(userAuth=='fail')
    {
      alert('Username or Password incorrect')

    }
    else if(userAuth=='nouser')
    {
      alert('No Username in database')
    }
    setuserAuth('default')
  }
  }
},[userAuth])

return(  //Create a form and send it
<div className="auth-wrapper">
<div className="auth-inner">
        <div onSubmit={onSubmit}>
        <form>
        <h3>Login- Pycharmers HaaS</h3>
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
        id='password'
        className="form-control"
        name='password'
        onChange={(e)=> setPassword(e.target.value)} 
        value={password} />
        </div>
        <div className="d-grid">
        <input type='submit' value='Login'  className="btn btn-primary"/>
        </div>
        <p className="forgot-password text-right">
               New user? <a href="http://localhost:5000/signup/">Sign Up</a>
               </p>
    </form>
    </div>
    </div>
    </div>
    )
}
export default Login