import React from 'react';
import Navbar from './components/Navbar';
import './App.css';
import Home from './components/pages/Home';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Teams from './components/pages/Teams';
import Players from './components/pages/Players';
import ContactUs from './components/pages/ContactUs';
import Marketing from './components/pages/Marketing';
import Consulting from './components/pages/Consulting';

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path='/' exact component={Home} />
        <Route path='/teams' component={Teams} />
        <Route path='/players' component={Players} />
        <Route path='/contact-us' component={ContactUs} />
        <Route path='/marketing' component={Marketing} />
        <Route path='/consulting' component={Consulting} />
      </Switch>
    </Router>
  );
}

export default App;
