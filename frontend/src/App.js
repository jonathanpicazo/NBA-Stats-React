import React from 'react';
import Navbar from './components/Navbar';
import './App.css';
import Home from './components/pages/Home';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Teams from './components/pages/Teams';
import Players from './components/pages/Players';
import ContactUs from './components/pages/ContactUs';
import Hype from './components/pages/Hype';
import HomeTeam from './components/pages/HomeTeam';
import FieldGoal from './components/pages/FieldGoal';
import BestGame from './components/pages/BestGame';
import ThreePoint from './components/pages/ThreePoint';
import Block from './components/pages/Block';

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path='/' exact component={Home} />
        <Route path='/teams' component={Teams} />
        <Route path='/players' component={Players} />
        <Route path='/contact-us' component={ContactUs} />
        <Route path='/hype' component={Hype} />
        <Route path='/hometeam' component={HomeTeam} />
        <Route path='/fieldgoal' component={FieldGoal} />
        <Route path='/bestgame' component={BestGame} />
        <Route path='/threepoint' component={ThreePoint} />
        <Route path='/block' component={Block} />
      </Switch>
    </Router>
  );
}

export default App;
