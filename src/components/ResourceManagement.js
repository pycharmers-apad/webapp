import {useRef, useState, useEffect} from 'react';
import { useParams,useNavigate } from 'react-router-dom';

const ResourceManagement=()=>{
    const {id}=useParams();
    const navigate=useNavigate();
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
        setProjectName(data['project_name'])
        setresUsageX(data['hwSets']['hwSet1'])
        setresUsageY(data['hwSets']['hwSet2'])
        setHWSetX(data['capacity']['hwSet1'])
        setHWSetY(data['capacity']['hwSet2'])

    }).then(setIsloading(false))
};
    getAllInformation();
},[])


    return (
        <div>
        {isloading? (console.log('loading'))
        :(
        <div>
            <h1 className="display-2">{projectName} : {id} </h1>
      <div className="col-lg-6">
        <hr />
        <p style={{marginLeft: 5}}>{projectName} is currently using:
        </p>
        <ul>
          <li>Project:{id} is using {resUsageX} resources from a capacity of {HWSetX} resources from hwSet1</li>
          <li>Project:{id} is using {resUsageY} resources from a capacity of {HWSetY} resources from hwSet2</li>
        </ul> 
        <p />
      </div>
      <div className="col-lg-6" style={{marginLeft: 5}}>
        <button type="button" className="btn btn-dark" onClick={()=> { navigate(`/projects/${Projectid}/cico`)}}>Check In/Out Resources</button>
      </div>
    </div>)}
</div>)
}
export default ResourceManagement;