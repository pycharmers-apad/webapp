import React, { useEffect,useState} from 'react'
import { useParams,useNavigate } from 'react-router-dom';
import '/node_modules/bootstrap/dist/css/bootstrap.min.css'


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

  function onSubmit(){
        const requestOptions={
      method:'POST'
    }
    console.log('Post Data ',requstFrom.mode);
    const mode=requstFrom['mode']
    console.log(hwSet1,hwSet2,mode)
    return false
  }

  return (
    <div>
        {isloading? (console.log('loading'))
        :(
  <div onSubmit={onSubmit}>
    <body>
    <title>Resource Management</title>
  <p>[projectName] · #[projectID]</p>
  <p>Check In/Check Out</p>
  <div className="col-lg-6">
        <hr />
    <form>
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
        <button type="button" onClick={()=>{requstFrom.mode='checkin';onSubmit()}} className="btn btn-dark">Check In</button>
        <button type="button" onClick={()=>{requstFrom.mode='checkout';onSubmit()}} className="btn btn-dark">Check Out</button></li>
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