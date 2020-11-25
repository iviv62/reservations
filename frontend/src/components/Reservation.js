import React, {useState} from 'react'
import "../static/css/reservations.css"
import moment from "moment"
const hours=[
    "7:00",
    "7:20",
    "7:40",
    "8:00",
    "8:20",
    "8:40",
    "9:00",
    "9:20",
]

const days = {
    1:"Пон",
    2:"Вт",
    3:"Ср",
    4:"Чет",
    5:"Пет",
    6:"Съб",
    0:"Нед"
}


const Reservation = () => {
    let initialDay = moment()
    let [today,setToday] = useState(moment())
    let [tommorow,setTommorow] = useState(moment().add(1,'days'))
    let [afterTommorow,setAfterTommorow] = useState(moment().add(2,'days'))


  

    const incrementDays = () =>{
        setToday(today.clone().add(3,'days'));
        setTommorow(today.clone().add(4,'days'));
        setAfterTommorow ( today.clone().add(5,'days'));
    }


    const decrementDays = () =>{
        if(!initialDay.isSame(today, "d") && !initialDay.isSame(tommorow, 'd') && !initialDay.isSame(afterTommorow, 'd') ){
            setToday(today.clone().subtract(3,'days'));
            setTommorow(today.clone().subtract(2,'days'));
            setAfterTommorow ( today.clone().subtract(1,'days'));
            console.log(initialDay)
            console.log(today)
        }
    }
    

    return (
        <div className="card mt-3 sh-1">
        <div className="header-dark sh-1">
            Запазете Час
        </div>
        <div className="content"></div>
        <div className="title p-3 centre"> МЦ Алфамедикс</div>
        <div className="title2 mt-2 mb-3 centre">София, ж.к. Овча Купел 1, бул. Монтевидео 45</div>


        <div className="row ">
            <div onClick={()=>decrementDays()} className="arrow-btn"><svg  width="16" height="16" viewBox="0 0 16 16" className ><path  d="M6.7.5c.2-.3.5-.5 1-.5s.8.2 1.2.5c.5.6.5 1.4 0 2.2L3.5 8 9 13.5c.6.8.6 1.5 0 2.2-.4.3-.8.4-1.3.4-.4 0-.8 0-1-.3L.4 9C0 9 0 8.6 0 8c0-.4 0-.8.4-1L6.7.5z"></path></svg></div>
                <div className="column centre-items">
                    <div className="day">{days[ today.day() ]}  </div>
                    <div className="date">{today.format("DD.MM.YYYY")}</div>
                    
                    <div className="hours">
                    <div className="column">
                            {hours.map((item) =><div className="dashed">-</div> )}
                        </div></div>
                </div>
                <div className="column centre-items">
                    <div className="day">{days[tommorow.day()]} </div>
                    <div className="date">{tommorow.format("DD.MM.YYYY")}</div>
                    <div className="hours">
                    <div className="column">
                            {hours.map((item) =><div className="hour-badge">{item}</div> )}
                        </div>
                    </div>
                </div>
                <div className="column centre-items">
                    <div className="day">{days[afterTommorow.day()]} </div>
                    <div className="date">{afterTommorow.format("DD.MM.YYYY")}</div>
                    <div className="hours">
                    <div className="column">
                            {hours.map((item) =><div className="hour-badge">{item}</div> )}
                        </div>
                    </div>
                    
                </div>
                
            <div onClick={()=>incrementDays()} className="arrow-btn"><svg width="16" height="16" viewBox="0 0 16 16"  ><path className="arrow"  d="M2.7.5c-.2-.3-.5-.5-1-.5S1 .2.5.5C-.2 1-.2 2 .5 2.7L5.7 8 .5 13.5c-.7.8-.7 1.5 0 2.2.3.3.7.4 1.2.4.4 0 .8 0 1-.3L9 9c.3-.2.4-.5.4-1 0-.4 0-.8-.4-1L2.7.5z"></path></svg></div>
            
        </div>
       

        </div>
    )
}

export default Reservation
