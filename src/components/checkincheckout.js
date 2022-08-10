import React, { useEffect,useState} from 'react'
import { useParams,useNavigate } from 'react-router-dom';
// import bootstrap for UI 
import '/node_modules/bootstrap/dist/css/bootstrap.min.css'
import Navbar from './Navbar';

/*
TODO: Implement scalable solution for when there are multiple harware sets that
      show on the check in check out view

Possible frontend solution: retreieve a json that contains all the hardware sets
  Have function to render each HWSet as a flexbox for each key in the json
  v Implementation demo using an array of items rather than a json of items
  https://stackoverflow.com/questions/38028960/react-flexbox-grid-build-dynamically
*/

const Cico=() => {
  // Constant that stores the passed in projected id in the URL
  const {id}=useParams();

  /* React hooks for check in check out
    isloading1 -> tracks that the hardware set data is loading
    enterhwset1 -> The amount that the user inputs for HWSet 1 ci or co
    enterhwset2 -> The amount that the user inputs for HWSet 2 ci or co

    TODO: rename variable to something more readable
    ugh -> variable that gets the newly 

    error_ -> the error message response from the api backend
  */
  const [isloading1,setIsloading1]=useState(true);
  const [enterhwSet1,setenterHwSet1]=useState('');
  const [enterhwSet2,setenterHwSet2]=useState('');
  const [ugh,setUgh]=useState([]);
  const [error_,setError]=useState('');

  // Use effect to update the project hardware set data from the backend
  useEffect(()=>{
    // Get data of the hardware sets data with get method that 
      const getData= async()=>{
      await fetch(`https://pycharmers-apad.herokuapp.com/api/projects/${id}/gethwdata/`,{method:'GET' })
      .then(response=>response.json())
      .then(data=>{
        setUgh(data)
        setIsloading1(false)
      })
    }
      getData();
  },[])

  // constant that indicates whether or not the user chose check in or checkout
  const requstFrom = {
    mode: ''
  }
 
  // Sends POST request to check in or check out based on the requstFrom mode
  const onSubmit=async(hwset)=>{
    // Get whether or not the submit was for check in or check out
    const mode=requstFrom['mode']

    // Post Request that sends in a json of the hwset that is being acted on
    //    Backend updates the database after checking in and checking out
    //    Sends in the mode (check in / check out) and the HWSet chosen by the user
    // Receives json of the error message
    fetch(`https://pycharmers-apad.herokuapp.com/api/projects/${id}/cicodata/`,{ method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers : {
    'Content-Type':'application/json'
    },
    body:JSON.stringify({mode,'hwset':hwset})})
    .then(response=>response.json())
    .then(data=>setError(data['error_msg']))
    
    return false
  }

  // use effect for error_ to update the error code coming from backend
  //   if success then reload the window that holds HWSet information and get the updated 
  //   capacity and availability 
  useEffect(()=>{
    if(error_==='Success'){
      window.location.reload(false)
    }
    
    // alert the user if the error message code is not a success with the error_ code
    else if(error_!==''){
      alert(error_)
      setError('')
    }
  },[error_])

  return (
    <div>
        {isloading1 ? (console.log('loading'))
        :( 

  <div onSubmit={onSubmit}>
    <Navbar />     
    <body>
      <div >
    <title>Resource Management</title>
  <h2 style={{"margin-left":10}}>{ugh['project_name']}. #{id}</h2>
  <h3 style={{"margin-left":10}}>Check In Check Out resources from shared hardware set</h3>        
  <br></br>
    <form>
    <div className="auth-wrapper"style={{"width":"300px","float":"left","margin-left":'50px'}}>
    <div className="auth-inner">
        <h3>Hardware Set 1</h3>
        <p>Availability: {ugh['availability_hwset1']}</p>
        <p>Capacity: {ugh['capacity_hwset1']}</p>
        <p>Enter Quantity to CheckIn, Checkout</p>
        <input className="form-control" type="text" placeholder="Enter quantity" name="inputHW1"
        onChange={((e)=>setenterHwSet1(e.target.value))}     aria-label="inputHW1" />
        <button type="button" style={{'margin-left':10,'margin-top':10}}onClick={()=>{requstFrom.mode='checkin';onSubmit({'hwSet1':enterhwSet1})}} className="btn btn-dark" >Check In</button>
        <button type="button" style={{'margin-left':10,'margin-top':10}}onClick={()=>{requstFrom.mode='checkout';onSubmit({'hwSet1':enterhwSet1})}} className="btn btn-dark">Check Out</button>
          </div>
    </div>
    <div className="auth-wrapper" style={{"width":"300px","margin-left":'600px'}}>
    <div className="auth-inner">
    
        <h3>Hardware Set 2</h3>
        <p>Availability: {ugh['availability_hwset2']}</p>
        <p>Capacity: {ugh['capacity_hwset2']}</p>
        <p>Enter Quantity to CheckIn, Checkout</p>
        <input className="form-control" type="text" placeholder="Enter quantity " name="inputHW2"
        onChange={((e)=>setenterHwSet2(e.target.value))} 
        aria-label="inputHW2" />
        <button type="button" style={{'margin-left':10,'margin-top':10}} onClick={()=>{requstFrom.mode='checkin';onSubmit({'hwSet2':enterhwSet2})}} className="btn btn-dark" >Check In</button>
        <button type="button" style={{'margin-left':10,'margin-top':10}} onClick={()=>{requstFrom.mode='checkout';onSubmit({'hwSet2':enterhwSet2})}} className="btn btn-dark">Check Out</button>
</div>
</div>
    <p />
    
    </form>
    </div>
    
    </body>
    </div>
        )}
        </div>
)
}

export default Cico