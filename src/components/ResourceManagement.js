import {useRef, useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';

const ResourceManagement=()=>{
    const {id}=useParams();
return (
    <div>
      <title>Resource Management</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossOrigin="anonymous" />
      <h1 className="display-2">[projectName] · #{id}</h1>
      <h1 className="display-3">Resource Management</h1>
      <div className="col-lg-6">
        <hr />
        <p style={{marginLeft: 5}}>[projectName] is currently using:
        </p><ul>
          <li>[resUsageX] from [HWSetX]</li>
          <li>[resUsageY] from [HWSetY]</li>
          <li>[resUsageZ] from [HWSetZ]</li>
        </ul>
        <p />
      </div>
      <div className="col-lg-6" style={{marginLeft: 5}}>
        <button type="button" className="btn btn-dark">Check In/Out Resources</button>
      </div>
    </div>
  )
}
export default ResourceManagement