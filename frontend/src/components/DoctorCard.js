import React from 'react';
import '../static/css/doctorCard.css';
import doctorImage from '../static/images/doctor.jpg' 
import DoctorBadge from "./DoctorBadge"

const badges = [
    "работи с нзок",
    "Работи с деца",
    "с обявена цена",
]

const DoctorCard = () => {
    return (
        <div className="card-container">
            <div className="image-container">
                <img src={doctorImage} alt="doctor" className="profile-pic centre"/>
                <div className="font-weight-bold__main centre title mt-3">Д-р Иван Петков</div>
                <div className=" centre title2 mt-3">Кардиолог</div>
                <div className="badge-container mt-3">
                    {
                       badges.map((item)=>
                        <DoctorBadge data={item}/>
                       ) 
                    }

                </div>

            </div>
        </div>
    );
}

export default DoctorCard;

