import React from 'react';
import './Pages.css';
import axios from 'axios';



export default class BestGame extends React.Component {
  state = {
    bestPlayers: {}
  };

 


  componentDidMount() {
    console.log('Component mounted')
    axios.get(`http://localhost:5000/playersBestGame`)
      .then(res => {
        //const bestPlayers = res.data;
        console.log(res.data)
        this.setState({
          bestPlayers: res.data
       })
      })

  }

  printBestPlayers = () => {
    var array = []
    for (let k in this.state.bestPlayers) {
      array.push(<div><li>{this.state.bestPlayers[k]}</li></div>)
      //console.log(k + ' is ' + this.state.bestPlayers[k])
    }
    return array;
 }


  render() {
    return(
      <div className = 'bestgame'>
        <h2>Player Rankings, Top 10</h2>
        <div class = "container">
        <div>
        <b>Best Individual Performance in a Game</b>
          <ol>
            {this.printBestPlayers()}
          </ol>
          </div>
        </div>
      </div>
    );
  }
};
