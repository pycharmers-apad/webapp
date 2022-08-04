import { useNavigate } from "react-router-dom";

const Navbar=()=>{
    const navigate=useNavigate()

    return(
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
    <a className="navbar-brand" href="/">PyCharmers HaaS</a>
    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon" />      
    </button>
    <div>
    <div className="collapse navbar-collapse" id="navbarNav">
      <ul className="navbar-nav">
        <li className="nav-item active">
          <a className="nav-link" href='/projects/'>Home</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/">Log Out</a>
        </li>
      </ul>
      </div>
    </div>
  </nav>
  )
}
export default Navbar;