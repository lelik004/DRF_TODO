import React from "react";
import {Link} from "react-router-dom";


const User = ({user}) => {
    return (
        <tr>
            <td>{user.pk}</td>
            {/*<td><Link to={`/users/${user.pk}`}> {user.username}</Link> </td>*/}
            <td>{user.username}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>
    )
}

const UsersList = ({users}) => {
    return(
        <table>
            <th>ID</th>
            <th>username</th>
            <th>first_name</th>
            <th>last_name</th>
            <th>email</th>
            {users.map((user) => <User user={user}/> )}
        </table>
    )
}

export default UsersList