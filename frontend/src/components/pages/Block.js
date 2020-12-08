import React from 'react';
import './Pages.css';
import axios from 'axios';
import Plot from 'react-plotly.js';


export default class Block extends React.Component {
  state = {
    bestBlockers:{},
    xaxis: [],
    yaxis: []
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
    this.state.xaxis.push(this.state.bestBlockers[k][0])
    console.log(this.state.bestBlockers[k][0])
    this.state.yaxis.push(this.state.bestBlockers[k][1])
    console.log(this.state.bestBlockers[k][1])
    }
  return array;
}


  render() {
    return(
      <div className = 'block'>
        <div class = "container">
        <div>
        <Plot
        data={[
          {
            x: this.state.xaxis,
            y: this.state.yaxis,
            type: 'bar',
            marker: {color: 'blue'},
          },
          {x: this.state.xaxis, y: this.state.yaxis},
        ]}
        layout={ {paper_bgcolor: 'grey' ,width: 850, height: 850, title: 'Top 10 best games', plot_bgcolor: 'grey'} }
      />
          
        </div>
        <div>
          <h2>Blocks in a Game</h2>
          <ul className = "title">
            {this.printBestBlockers()}
          </ul>
          </div>
        </div>
        </div>
    );
  }
};
