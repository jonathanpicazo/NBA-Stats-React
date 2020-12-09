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
      axios.get(`http://localhost:5000/UpdateBlocks`)
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
  let name = ''
  for (let k in this.state.bestBlockers) {
    array.push(<div><li>{this.state.bestBlockers[k]}</li></div>)
    name = this.state.bestBlockers[k][0]
    name = name.substring(0, name.length - 2);
    this.state.xaxis.push(name)
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
            marker: {color: 'light-blue'},
          },
          {x: this.state.xaxis, y: this.state.yaxis},
        ]}
        layout={ {paper_bgcolor: 'grey' ,width: 850, height: 850, title: 'Top 10 Blocks', plot_bgcolor: 'grey'} }
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
