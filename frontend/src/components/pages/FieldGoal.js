import React from 'react';
import './Pages.css';
import axios from 'axios';



export default class FieldGoal extends React.Component {
  state = {
    bestFieldGoalers:{}
  };

 


  componentDidMount() {
    console.log('Component mounted')
      axios.get(`http://localhost:5000/bestFieldGoalPercentage`)
      .then(res => {
        //const bestPlayers = res.data;
        console.log(res.data)
        this.setState({
          bestFieldGoalers: res.data
       })
      })

  }


printBestFieldGoalers = () => {
  var array = []
  for (let k in this.state.bestFieldGoalers) {
    array.push(<div><li>{this.state.bestFieldGoalers[k]}</li></div>)
    //console.log(k + ' is ' + this.state.bestPlayers[k])
  }
  return array;
}




  render() {
    return(
      <div className = 'fg'>
        <h2>Player Rankings, Top 10</h2>
        <b>FG% in a Game (per 10+ attempts)</b>
        <div class = "container">
        <ol>
          {this.printBestFieldGoalers()}
          </ol>
        </div>
      </div>
    );
  }
};
