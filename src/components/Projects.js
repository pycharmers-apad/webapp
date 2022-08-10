import { useEffect,useState } from "react"
import { Link, useParams,useNavigate } from "react-router-dom"
import Navbar from "./Navbar"

const Projects=()=>{   
    const [Projectid,setProjectId]=useState('')
    const navigate=useNavigate()
    const [setNav,setUsenav]=useState('default')
    const onClick=(e)=>{
        e.preventDefault()
        console.log('click');
        
       fetch(`https://pycharmers-apad.herokuapp.com/api/projects/${Projectid}/`,{method:'GET'})
        .then(response=>response.json())
        .then(data=>setUsenav(data['is_exists']))
    }
    // hooks for projectid, projectname, project description, and api response
    const [projectNameInput, setProjectNameInput] = useState("")
    const [projectDescriptionInput, setDescriptionInput] = useState("")
    // json that returns the response and the error
    const [apiResponse, setApiResponse] = useState({"Response": "Default", "IDError": ""})
    const [projectIdNew,setProjectId_New]=useState("")

    function handleSubmission(event) {
        event.preventDefault();

        // send json and receive json of the response and error code if any
        fetch(`https://pycharmers-apad.herokuapp.com/api/projects/${projectIdNew}/newproject/`,
            {'method': 'POST',headers: {'Content-Type':'application/json','Accept':'application/json'},
            body: JSON.stringify({'ProjectID':Projectid, 'ProjectName':projectNameInput, 'ProjectDescription':projectDescriptionInput})})
        .then(response => response.json())
        .then(api => setApiResponse(api))
    }

    
useEffect(()=>{
    if(setNav==='true')
      {
        console.log("Navigating to Project Management Page")
        navigate(`/projects/${Projectid}/resources`)

    } 
    else if (setNav==='noid')
        {
        alert('No Project iD in database')
    }
    },[setNav])

    // use effect to redirect user if successfully created
    // if not successfully created then send an alert tot he user with the error
    useEffect(()=>{
        if (apiResponse["Response"] == 'Success'){
            console.log("Navigating to Project Management Page")
            navigate(`/projects/${projectIdNew}/resources`)

        } else if (apiResponse["Response"] == "Default"){
            //This is the default option to prevent an alert from showing up
            //Literally do nothing :)
        }
        else {
            console.log('create new user failed')
            alert(apiResponse["IDError"])
        }
    },[apiResponse])

//Projects created by user
    return(
        <div>
            <Navbar />
        <div  style={{marginLeft: 10}}>
            <h1>Welcome to Project Management Page</h1>
            <br></br>
            <h3>Choose existing project:</h3>
            <div>
                <input type='text'style={{'margin-right':5}} onChange={(e)=>{setProjectId(e.target.value)}} />
        <button onClick={onClick} className="btn btn-dark" >Submit</button>
            </div>
            <div className="auth-inner">
            <div>
                <h3>
                    Create New Project
                </h3>
                <form onSubmit={handleSubmission}>
                    <div>
                    <label>
                        Enter Project ID Here:
                        <input type = "text" value = {projectIdNew} onChange = {e => setProjectId_New(e.target.value)}/>
                    </label>
                    </div>
                    <div>
                    <label>
                        Enter Project Name Here:
                        <input type = "text" value = {projectNameInput} onChange = {e => setProjectNameInput(e.target.value)}/>
                    </label>
                    </div>
                    <div>
                    <label>
                        Enter Project Description Here:
                        <input type = "text" value = {projectDescriptionInput} onChange = {e => setDescriptionInput(e.target.value)}/>
                    </label>
                    </div>
                    <input type = "submit" value = "Submit"  className="btn btn-dark"/>
                    
                </form>
                </div>
            </div>
        </div>
        </div>
    )

}

export default Projects;