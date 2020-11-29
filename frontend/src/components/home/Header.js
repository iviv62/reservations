import React from 'react'
import "../../static/css/home/Header.css"
import "../../static/css/searchForm.css"
import SearchForm from "../SearchForm"

const Header = () => {
    return (
        <div className="header-body">
            <div className="row">
                <div className="column">
                    <div className="header-title">
                        Намерете най-добрите специалисти и изберете удобно за вас време за преглед  
                    </div>
                    

                </div>
                <div className="column"></div>
            </div>
            <SearchForm/>
        </div>
    )
}

export default Header
