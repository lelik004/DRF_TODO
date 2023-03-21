import React from 'react';
import './App.css';
import {HashRouter, Route, Routes, Link, BrowserRouter, Switch} from "react-router-dom";

import Menu from "./components/Menu";
import UsersList from "./components/Users";
import ProjectsList from "./components/Projects";
import TodoList from "./components/TodoList";
import Footer from "./components/Footer";
import NotFound404 from "./components/NotFound404";

import axios from "axios";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todo_list': [],
            'footer': [],
            'user_detail': [],
        }
    }

    componentDidMount() {

        //Users mount
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))

        // Projects mount
        axios.get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))

        // Todo Mount
        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const todo_list = response.data.results
                this.setState(
                    {
                        'todo_list': todo_list
                    }
                )
            }).catch(error => console.log(error))
    }


    render() {
        return (
            <div>
                <Menu menu={this.state.menu}/>
                <BrowserRouter>
                    <Switch>
                        <Route exact path='/users' component={() => <UsersList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectsList projects={this.state.projects}/>}/>
                        <Route exact path='/todo' component={() => <TodoList todo_list={this.state.todo_list}/>}/>
                        {/*<Route component={NotFound404}/>*/}
                    </Switch>
                </BrowserRouter>
                <Footer footer={this.state.footer}/>
            </div>
        )
    }
}

export default App;


// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
