import React, { useEffect,useState} from 'react'
import { useParams,useNavigate } from 'react-router-dom';
import '/node_modules/bootstrap/dist/css/bootstrap.min.css'
import Navbar from './Navbar';

const Cico=() => {
    const {id}=useParams();
    const [isloading1,setIsloading1]=useState(true);
    const [enterhwSet1,setenterHwSet1]=useState('');
    const [enterhwSet2,setenterHwSet2]=useState('');
    const [ugh,setUgh]=useState([]);
    const [error_,setError]=useState('success');

    useEffect(()=>{
        const getData= async()=>{
        await fetch(`https://pycharmers-apad.herokuapp.com/api/projects/${id}/gethwdata/`,{
            method:'GET'
        }).then(response=>response.json())
        .then(data=>{
          setUgh(data)
          setIsloading1(false)
        })}
        getData();    
      
      }      
    ,[])

    const requstFrom = {
        mode: ''
      }

  const onSubmit=async(hwset)=>{
        const requestOptions={
      method:'POST'
    }

    const mode=requstFrom['mode']
    fetch(`https://pycharmers-apad.herokuapp.com/projects/${id}/cicodata/`,{ method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers : {
   'Content-Type':'application/json'
    },
  body:JSON.stringify({mode,'hwset':hwset})})
    .then(response => response.json())
      window.location.reload(false)
      
    return false
  
  }

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