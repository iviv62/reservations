import React from 'react'
import '../static/css/doctorBadge.css';

const DoctorBadge = ({data}) => {
    return (
        <div className="badge ml-2 ml-2 sh-1">
           {data}
        </div>
    )
}

export default DoctorBadge
