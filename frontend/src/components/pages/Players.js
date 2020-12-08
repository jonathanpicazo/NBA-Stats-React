import React from 'react';
import './Pages.css';
import axios from 'axios';



export default class Players extends React.Component {
  state = {
    bestPlayers: {},
    bestShooters:{},
    bestFieldGoalers:{},
    bestBlockers:{}
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
      //www
      axios.get(`http://localhost:5000/topTen3Pointers`)
      .then(res => {
        //const bestPlayers = res.data;
        console.log(res.data)
        this.setState({
          bestShooters: res.data
       })
      })
      axios.get(`http://localhost:5000/bestFieldGoalPercentage`)
      .then(res => {
        //const bestPlayers = res.data;
        console.log(res.data)
        this.setState({
          bestFieldGoalers: res.data
       })
      })
      axios.get(`http://localhost:5000/topTenBlocks`)
      .then(res => {
        //const bestPlayers = res.data;
        console.log(res.data)
        this.setState({
          bestBlockers: res.data
       })
      })
    // //
    // axios.get(`https://localhost:5000/bestFieldGoalPercentage`)
    // .then(res => {
    //   const bestFieldGoalers = res.data;
    //   this.setState({ bestFieldGoalers });
    // })

  }

  printBestPlayers = () => {
    var array = []
    for (let k in this.state.bestPlayers) {
      array.push(<div><li>{this.state.bestPlayers[k]}</li></div>)
      //console.log(k + ' is ' + this.state.bestPlayers[k])
    }
    return array;
 }

 printBestShooters = () => {
  var array = []
  for (let k in this.state.bestShooters) {
    array.push(<div><li>{this.state.bestShooters[k]}</li></div>)
    //console.log(k + ' is ' + this.state.bestPlayers[k])
  }
  return array;
}

printBestFieldGoalers = () => {
  var array = []
  for (let k in this.state.bestFieldGoalers) {
    array.push(<div><li>{this.state.bestFieldGoalers[k]}</li></div>)
    //console.log(k + ' is ' + this.state.bestPlayers[k])
  }
  return array;
}

printBestBlockers = () => {
  var array = []
  for (let k in this.state.bestBlockers) {
    array.push(<div><li>{this.state.bestBlockers[k]}</li></div>)
    //console.log(k + ' is ' + this.state.bestPlayers[k])
  }
  return array;
}


  render() {
    return(
      <div className = 'players'>
        <h2>Player Rankings, Top 10</h2>
        <div class = "container">
        <div>
        <b>Best Individual Performance in a Game</b>
          <ol>
            {this.printBestPlayers()}
          </ol>
          </div>
        <div>
        <b>3PT% in a Game (per 10+ attempts)</b>
          <ol>
            {this.printBestShooters()}
          </ol>
            </div>
        <div>
        <b>FG% in a Game (per 10+ attempts)</b>
        <ol>
          {this.printBestFieldGoalers()}
          </ol>
        </div>
        <div>
          <b>Blocks in a Game</b>
          <ol>
            {this.printBestBlockers()}
          </ol>
        </div>
        </div>
      </div>
    );
  }
};
