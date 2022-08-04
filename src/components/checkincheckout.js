import React, { useEffect,useState} from 'react'
import { useParams,useNavigate } from 'react-router-dom';
import '/node_modules/bootstrap/dist/css/bootstrap.min.css'
import Navbar from './Navbar';

const Cico=() => {
    const {id}=useParams();
    const [isloading,setIsloading]=useState(true);
    const [hwSet1,setHwSet1]=useState(0);
    const [hwSet2,setHwSet2]=useState(0);

    useEffect(()=>{
        const getData= async()=>{
        fetch(`https://pycharmers-apad.herokuapp.com/api/projects/${id}/gethwdata/`,{
            method:'GET'
        }).then(response=>response.json())
        .then(data=>console.log(data))
        .then(setIsloading(false)
    )};
        getData();
    }  ,[])

    const requstFrom = {
        mode: ''
      }

  function onSubmit(hwset){
        const requestOptions={
      method:'POST'
    }

    const mode=requstFrom['mode']
    console.log(mode,hwset)
    return false
  }

  return (
    <div>
        {isloading? (console.log('loading'))
        :(
  <div onSubmit={onSubmit}>
    <Navbar />     
    <body>
      <div >
    <title>Resource Management</title>
  <h2 style={{"margin-left":10}}>[projectName]· #[projectID]</h2>
  <h3 style={{"margin-left":10}}>Check In Check Out resources from shared hardware set</h3>        
  <br></br>
    <form>
    <div className="auth-wrapper"style={{"width":"300px","float":"left","margin-left":'50px'}}>
    <div className="auth-inner">
        <h3>Hardware Set 1</h3>
        <p>Availability: [availabilitySetX]</p>
        <p>Capacity: [capacitySetX]</p>
        <p>Enter Quantity to CheckIn, Checkout</p>
        <input className="form-control" type="text" placeholder="Enter quantity" name="inputHW1"
        onChange={((e)=>setHwSet1(e.target.value))}     aria-label="inputHW1" />
        <button type="button" style={{'margin-left':10,'margin-top':10}}onClick={()=>{requstFrom.mode='checkin';onSubmit({'hwSet1':hwSet1})}} className="btn btn-dark" >Check In</button>
        <button type="button" style={{'margin-left':10,'margin-top':10}}onClick={()=>{requstFrom.mode='checkout';onSubmit({'hwSet1':hwSet1})}} className="btn btn-dark">Check Out</button>
          </div>
    </div>
    <div className="auth-wrapper" style={{"width":"300px","margin-left":'600px'}}>
    <div className="auth-inner">
    
        <h3>Hardware Set 2</h3>
        <p>Availability: [availabilitySetY]</p>
        <p>Capacity: [capacitySetY]</p>
        <p>Enter Quantity to CheckIn, Checkout</p>
        <input className="form-control" type="text" placeholder="Enter quantity " name="inputHW2"
        onChange={((e)=>setHwSet2(e.target.value))} 
        aria-label="inputHW2" />
        <button type="button" style={{'margin-left':10,'margin-top':10}} onClick={()=>{requstFrom.mode='checkin';onSubmit({'hwSet2':hwSet2})}} className="btn btn-dark" >Check In</button>
        <button type="button" style={{'margin-left':10,'margin-top':10}} onClick={()=>{requstFrom.mode='checkout';onSubmit({'hwSet2':hwSet2})}} className="btn btn-dark">Check Out</button>
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