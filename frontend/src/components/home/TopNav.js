import React, {useState} from 'react'
import '../../static/css/home/TopNav.css'
import { FaTimes,FaBars } from "react-icons/fa";

const MenuItems = [
    {
        title: 'Home',
        url: '#',
        cName: 'nav-links'
    },
    {
        title: 'Services',
        url: '#',
        cName: 'nav-links'
    },
    {
        title: 'Products',
        url: '#',
        cName: 'nav-links'
    },
    {
        title: 'Contact Us',
        url: '#',
        cName: 'nav-links'
    },
   

]


const TopNav = () => {

    const [clicked,setClicked] = useState(false)

    const handleClick = () => {
        setClicked(!clicked)
    }

    return (
        <nav className="NavbarItems">
                <h1 className="navbar-logo">Logo</h1>
                <div className="menu-icon" onClick={()=>handleClick()}>
                    {clicked?(<FaTimes size={30} color={"white"}/> ) : (<FaBars size={30} color={"white"}/> ) }
                </div>
                <ul className={clicked ? 'nav-menu active' : 'nav-menu'}>
                    {MenuItems.map((item, index) => {
                        return (
                            <li className="mt-3 mb-3" key={index}>
                                <a className={item.cName} href={item.url}>
                                {item.title}
                                </a>
                            </li>
                        )
                    })}
                </ul>
            </nav>
    )
}

export default TopNav
