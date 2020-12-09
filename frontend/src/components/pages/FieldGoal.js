import React from 'react';
import './Pages.css';
import axios from 'axios';
import Plot from 'react-plotly.js';



export default class FieldGoal extends React.Component {
  state = {
    bestFieldGoalers:{},
    xaxis: [],
    yaxis: []
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
    this.state.xaxis.push(this.state.bestFieldGoalers[k][0])
    console.log(this.state.bestFieldGoalers[k][0])
    this.state.yaxis.push(this.state.bestFieldGoalers[k][1])
    console.log(this.state.bestFieldGoalers[k][1])
    }
  return array;
}




  render() {
    return(
      <div className = 'fg'>
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
        layout={ {paper_bgcolor: 'grey' ,width: 850, height: 850, title: 'Top 10 Field Goal %', plot_bgcolor: 'grey'} }
      />
          </div>
          <div>
          <h2>FG% in a Game (per 10+ attempts)</h2>
          <ul className = "title">
          {this.printBestFieldGoalers()}
          </ul>
          </div>
        </div>
      </div>
    );
  }
};
