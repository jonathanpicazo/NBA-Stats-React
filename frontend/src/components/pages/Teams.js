import React from 'react';
import './Pages.css';
import axios from 'axios';



export default class Teams extends React.Component {
  state = {
    bestHomers: {},
    bestHypers:{}
  };

 


  componentDidMount() {
    console.log('Component mounted')
    axios.get(`http://localhost:5000/bestHomeTeam`)
      .then(res => {
        //const bestHomers = res.data;
        console.log(res.data)
        this.setState({
          bestHomers: res.data
       })
      })
      //www
      axios.get(`http://localhost:5000/teamHypeatHome`)
      .then(res => {
        //const bestHomers = res.data;
        console.log(res.data)
        this.setState({
          bestHypers: res.data
       })
      })
  }

  printbestHomers = () => {
    var array = []
    for (let k in this.state.bestHomers) {
      array.push(<div><li>{this.state.bestHomers[k]}</li></div>)
      //console.log(k + ' is ' + this.state.bestHomers[k])
    }
    return array;
 }

 printbestHypers = () => {
  var array = []
  for (let k in this.state.bestHypers) {
    array.push(<div><li>{this.state.bestHypers[k]}</li></div>)
    //console.log(k + ' is ' + this.state.bestHomers[k])
  }
  return array;
}




  render() {
    return(
      <div>
        <h2>Teams Rankings, Top 10</h2>
        <div class = "container">
        <div>
        <b>Best Home Teams (based on PPG in a single game)</b>
          <ol>
            {this.printbestHomers()}
          </ol>
          </div>
        <div>
        <b>Hype Factor</b>
          <ol>
            {this.printbestHypers()}
          </ol>
          </div>
        </div>
      </div>
    );
  }
};
