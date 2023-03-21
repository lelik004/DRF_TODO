import React from "react";


const Project = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name_of_project}</td>
            <td>{project.link_to_repo}</td>
            <td>{project.group_of_users}</td>
        </tr>
    )
}

const ProjectsList = ({projects}) => {
    return(
        <table>
            <th>ID</th>
            <th>name_of_project</th>
            <th>link_to_repo</th>
            <th>group_of_users</th>
            {projects.map((project) => <Project project={project}/> )}
        </table>
    )
}

export default ProjectsList