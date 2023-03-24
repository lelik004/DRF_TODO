import React from 'react';
import './App.css';
import {HashRouter, Route, Routes, Link, BrowserRouter, Switch, Redirect} from "react-router-dom";

import LoginForm from "./components/Auth";
import Menu from "./components/Menu";
import UsersList from "./components/Users";
import ProjectsList from "./components/Projects";
import TodoList from "./components/TodoList";
import Footer from "./components/Footer";
import NotFound404 from "./components/NotFound404";

import axios from "axios";
import Cookies from "universal-cookie";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'token': '',
            'users': [],
            'projects': [],
            'todo_list': [],
            'footer': [],
            'user_detail': [],
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }


    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token' + this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()

        //Users mount
        axios.get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => {
            console.log(error)
            this.setState({users: []})
        })

        // Projects mount
        axios.get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })

        // Todo Mount
        axios.get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                const todo_list = response.data.results
                this.setState(
                    {
                        'todo_list': todo_list
                    }
                )
            }).catch(error => {
            console.log(error)
            this.setState({todo_list: []})
        })
    }

    componentDidMount() {
        this.get_token_from_storage()
        // this.load_data()
    }


    render() {
        return (

            <BrowserRouter>
                <nav>
                    <Menu menu={this.state.menu}/>
                    {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                        <Link to='/login'><button>Login</button></Link>}
                </nav>
                <div>
                    <Switch>
                        <Route path='/users' component={() => <UsersList users={this.state.users}/>}/>
                        {/*<Route exact path='/' component={() => <UsersList users={this.state.users}/>}/>*/}
                        <Route path='/projects' component={() => <ProjectsList projects={this.state.projects}/>}/>
                        <Route path='/todo' component={() => <TodoList todo_list={this.state.todo_list}/>}/>
                        <Route path='/login'
                               component={() => <LoginForm get_token={
                                   (username, password) => this.get_token(username, password)
                               }
                               />}/>
                        <Redirect from='/' to='/todo'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </div>
                <Footer footer={this.state.footer}/>
            </BrowserRouter>


        )
    }
}

export default App;
