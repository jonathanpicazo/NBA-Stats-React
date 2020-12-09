import React from 'react';
import './Pages.css';
import axios from 'axios';
import Plot from 'react-plotly.js';



export default class BestGame extends React.Component {
  state = {
    bestPlayers: {},
    xaxis: [],
    yaxis: []
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
      this.state.xaxis.push(this.state.bestPlayers[k][0])
      console.log(this.state.bestPlayers[k][0])
      this.state.yaxis.push(this.state.bestPlayers[k][1])
      console.log(this.state.bestPlayers[k][1])
    }
    return array;
 }


  render() {
    return(
      <div className = 'bestgame'>
        <div class = "container">
        <div>
        <Plot
        data={[
          {
            x: this.state.xaxis,
            y: this.state.yaxis,
            type: 'bar',
            marker: {color: 'light-blue'},
          },
          {x: this.state.xaxis, y: this.state.yaxis},
        ]}
        layout={ {paper_bgcolor: 'grey' ,width: 850, height: 850, title: 'Top 10 Best Games', plot_bgcolor: 'grey'} }
      />
          </div>
          <div>
          <h2>Best Individual Performance in a Game</h2>
          <ul className = "title">
            {this.printBestPlayers()}
          </ul>
          </div>
          </div>
        </div>
    );
  }
};
