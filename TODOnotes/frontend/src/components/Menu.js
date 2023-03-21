import React from "react";
import {Link} from "react-router-dom";

const Menu = ({menu}) => {
    return (

        <div>
            <nav>
                <a href='/users'>Пользователи</a>

                <a href='/projects'>Проекты</a>

                <a href='/todo'>Задания</a>
                {/*<Link to='/users'>Пользователи</Link>*/}

                {/*<Link to='/projects'>Проекты</Link>*/}

                {/*<Link to='/todo'>Задания</Link>*/}
            </nav>
            <hr></hr>
        </div>
    )
}

export default Menu