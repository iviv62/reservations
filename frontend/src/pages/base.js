import React from 'react'
import "../static/css/main.css"
import DoctorCard from "../components/DoctorCard"
import Contacts from "../components/Contacts"
import Bio from "../components/Bio"
import Reservation from "../components/Reservation"
import InsurersCard from "../components/InsurersCard"

const base = () => {
    return (
        <div className="row">
        <div className="main column" >
            <DoctorCard/>
            <Contacts/>
            <Bio/>
            <InsurersCard/>
            
        </div>
       <div className="column-30">
       <Reservation/>
       </div>
        </div>
    )
}

export default base
