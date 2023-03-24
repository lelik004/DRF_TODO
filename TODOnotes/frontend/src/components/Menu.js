import React from "react";
import {Link} from "react-router-dom";

const Menu = ({menu}) => {
    return (

        <div>
            <nav>
                <Link to='/users'>Пользователи </Link>

                <Link to='/projects'>Проекты</Link>

                <Link to='/todo'>Задания</Link>
            </nav>
            <hr></hr>
        </div>
    )
}

export default Menu