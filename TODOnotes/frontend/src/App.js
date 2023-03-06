import React from 'react';
import './App.css';
import UsersList from "./components/Users";
import Footer from "./components/Footer";
import Menu from "./components/Menu";
import axios from "axios";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'footer': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
    }


    render() {
        return (
            <div>
                <Menu menu={this.state.menu}/>
                <UsersList users={this.state.users}/>
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
