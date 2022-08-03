import React, { useEffect,useState} from 'react'
import { useParams,useNavigate } from 'react-router-dom';
import '/node_modules/bootstrap/dist/css/bootstrap.min.css'


const Cico=() => {
    const {id}=useParams();
    const [isloading,setIsloading]=useState(true);
    const [hwSet1,setHwSet1]=useState('');
    const [hwSet2,setHwSet2]=useState('');

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

  const onSubmit=(event)=>{
    event.preventDefault()
    const requestOptions={
      method:'POST'
    }
    console.log('Post Data ',requstFrom.mode);
  }

  return (
    <div>
        {isloading? (console.log('loading'))
        :(
  <div className="App" onSubmit={onSubmit}>
    <body>
    <title>Resource Management</title>
  <h1 className="display-2">[projectName] · #[projectID]</h1>
  <h1 className="display-3">Check In/Check Out</h1>
  <div className="col-lg-6">
    <hr />
    <form onSubmit={onSubmit}>
    <ul>
      <li>hwSet1</li>
      <ul>
        <li>Availability: [availabilitySetX]</li>
        <li>Capacity: [capacitySetX]</li>
        <li><input className="form-control" type="text" placeholder="Enter HW Quantity" name="inputHW1" 
        onChange={((e)=>setHwSet1(e.target.value))}     aria-label="inputHW1" /></li>
      </ul>
      <br />
      <ul>
      <li>hwSet2</li>
        <li>Availability: [availabilitySetY]</li>
        <li>Capacity: [capacitySetY]</li>
        <li><input className="form-control" type="text" placeholder="Enter HW Quantity" name="inputHW2"
        onChange={((e)=>setHwSet2(e.target.value))} 
        aria-label="inputHW2" />
        <button type="button" onClick={()=>{requstFrom.mode='checkin'}} className="btn btn-dark">Check In</button>
        <button type="button" onClick={()=>{requstFrom.mode='checkout'}} className="btn btn-dark">Check Out</button></li>
      </ul>
      </ul>
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