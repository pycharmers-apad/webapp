import { useEffect,useState } from "react"
import { Link, useParams,useNavigate, Navigate } from "react-router-dom"

const Projects=()=>{    
    const [Projectid,setProjectId]=useState(0)
    const navigate=useNavigate()
    const [setNav,setUsenav]=useState('false')
    const onClick=(e)=>{
        e.preventDefault()
        console.log('click');
        
        fetch(`https://pycharmers-apad.herokuapp.com/api/projects/${Projectid}/`,{method:'GET'})
        .then(response=>response.json())
        .then(data=>setUsenav(data['is_exists']))
    }

    
useEffect(()=>{
    if(setNav==='true')
      {
        console.log("Navigating to Project Management Page")
        navigate(`/projects/${Projectid}/resources`)

    } 
    else{
      console.log('fail')
    }
    },[setNav])

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