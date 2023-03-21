import React from "react";


const TodoItem = ({item}) => {
    return (
        <tr>

            <td>{item.id}</td>
            <td>{item.project}</td>
            <td>{item.todo_body}</td>
            <td>{item.created_at}</td>
            <td>{item.update_at}</td>
            <td>{item.created_user}</td>
        </tr>
    )
}

const TodoList = ({todo_list}) => {
    return(
        <table>
            <th>ID</th>
            <th>Название проекта</th>
            <th>todo_body</th>
            <th>created_at</th>
            <th>update_at</th>
            <th>created_user</th>
            {todo_list.map((item) => <TodoItem item={item}/> )}
        </table>
    )
}

export default TodoList