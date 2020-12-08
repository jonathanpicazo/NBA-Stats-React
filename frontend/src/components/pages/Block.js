import React from 'react';
import './Pages.css';
import axios from 'axios';



export default class Block extends React.Component {
  state = {
    bestBlockers:{}
  };

 


  componentDidMount() {
    console.log('Component mounted')
      axios.get(`http://localhost:5000/topTenBlocks`)
      .then(res => {
        //const bestPlayers = res.data;
        console.log(res.data)
        this.setState({
          bestBlockers: res.data
       })
      })
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
      <div>
        <b>Blocks in a Game</b>
        <div class = "container">
          <ol>
            {this.printBestBlockers()}
          </ol>
        </div>
        </div>
    );
  }
};
