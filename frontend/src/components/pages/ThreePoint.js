import React from 'react';
import './Pages.css';
import axios from 'axios';



export default class ThreePoint extends React.Component {
  state = {
    bestShooters:{}
  };

 


  componentDidMount() {
    console.log('Component mounted')
      axios.get(`http://localhost:5000/topTen3Pointers`)
      .then(res => {
        //const bestPlayers = res.data;
        console.log(res.data)
        this.setState({
          bestShooters: res.data
       })
      })
  }


 printBestShooters = () => {
  var array = []
  for (let k in this.state.bestShooters) {
    array.push(<div><li>{this.state.bestShooters[k]}</li></div>)
    //console.log(k + ' is ' + this.state.bestPlayers[k])
  }
  return array;
}


  render() {
    return(
      <div>
        <b>3PT% in a Game (per 10+ attempts)</b>
        <div class = "container">
          <ol>
            {this.printBestShooters()}
          </ol>
            </div>
      </div>
    );
  }
};
