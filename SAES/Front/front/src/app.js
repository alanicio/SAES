import React, { Component } from 'react';
import NavBar from './componentes/navbar';
import {BrowserRouter,Route,Switch} from 'react-router-dom';
import Login from './componentes/login.js';
import Personas from './componentes/Personas.js'
// import Home from './components/Home';
// import About from './components/About';
// import Contact from './components/Contact';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
      <div className="App">
        <NavBar/>
        <Switch>
          <Route exact path="/" component={Login}/>
          <Route path="/personas" component={Personas}/>
        </Switch>
      </div>
      </BrowserRouter>
    );
  }
}
export default App;