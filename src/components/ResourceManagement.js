import {useRef, useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';

const ResourceManagement=()=>{
    const {id}=useParams();
    const [isloading,setIsloading]=useState(true)
    const [projectName,setProjectName]=useState('')
    const [resUsageX,setresUsageX]=useState('')
    const [resUsageY,setresUsageY]=useState('')
    const [HWSetX,setHWSetX]=useState('')
    const [HWSetY,setHWSetY]=useState('')

useEffect(() => {
    const getAllInformation = async () => {
    fetch(`https://pycharmers-apad.herokuapp.com/api/projects/${id}/existingresources/`,{method:'GET'})
    .then(response=>response.json())
    .then(data=>{
        setProjectName(data[1])
        setresUsageX(data[3])
        setresUsageY(data[4])
        setHWSetX(data[5])
        setHWSetY(data[6])
    }).then(setIsloading(false))
};
    getAllInformation();
},[])


    return (
        <div>
        {isloading? (console.log('loading'))
        :(
        <div>
      <title>Resource Management</title>
      <h1 className="display-2">{projectName}Project ID: {id}</h1>
      <h1 className="display-3">Resource Management</h1>
      <div className="col-lg-6">
        <hr />
        <p style={{marginLeft: 5}}>{projectName} is currently using:
        </p>
        <ul>
          <li>{resUsageX} from {HWSetX}</li>
          <li>{resUsageY} from {HWSetY}</li>
        </ul>
        <p />
      </div>
      <div className="col-lg-6" style={{marginLeft: 5}}>
        <button type="button" className="btn btn-dark">Check In/Out Resources</button>
      </div>
    </div>)}
</div>)
}
export default ResourceManagement;