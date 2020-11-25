import React from 'react'
import DoctorBadge from "./DoctorBadge"
import { FaShieldAlt } from "react-icons/fa";

const insurers=[
"ДЗИ",
"Доверие",
"България Иншурънс",
"Булстрад Живот",
"Дженерали",
"Медико-21",

]

const InsurersCard = () => {
    return (
        <div className="card mt-3">
            <div className="header">
            <FaShieldAlt
            size={30}
            
            />
          Застрахователни компании, с които работя</div>
            <div className="content row mt-3">
                {insurers.map((item=>
                    <DoctorBadge data={item}/>
                ))}
            </div> 
        </div>
    )
}

export default InsurersCard
