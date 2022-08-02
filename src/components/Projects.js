import { useEffect,useState } from "react"
import { Link, useParams,useNavigate, Navigate } from "react-router-dom"

const Projects=()=>{    
    const [Projectid,setProjectId]=useState(0)
    const navigate=useNavigate()
    const onClick=(e)=>{
        e.preventDefault()
        console.log('click');
        navigate(`/projects/${Projectid}/resources`)
    }
//Projects created by user
    return(
        <div>
        <p>Welcome to Project Management Page</p>
        <div>
        <input type='text' onChange={(e)=>{setProjectId(e.target.value)}} />
        <button onClick={onClick} className="btn btn-dark"/>
        <p>Project Id selected:</p>
        </div>
        </div>
    )

}

export default Projects