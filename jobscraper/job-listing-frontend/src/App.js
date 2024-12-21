import logo from './logo.svg';
import './App.css';
import React,{useEffect, useState} from 'react';
import axios from 'axios';

function App() {
  const [jobs, setJobs]=useState([]);

  useEffect(()=>{
    axios.get('http://127.0.0.1:8000/api/jobs/')
    .then(response=> setJobs(response.data))
    .catch(error=>console.error(error)
    );
  },[]);
  return (
    <div className="p-4">
      <h1 className="text-3x1 font-bold mb-4">Job Listings</h1>
      {jobs.map(job=>(
        <div key={job.id} className='border p-4 rounded mb-4 shadow'>
          <h2 className='text-2x1'>{job.job_title}</h2>
          <p><strong>Company:</strong>{job.company}</p>
          <p><strong>Location:</strong>{job.location}</p>
          <p><strong>Skills:</strong>{job.skills}</p>
        </div>
      ))}
       
    </div>
  );
}

export default App;
