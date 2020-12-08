import React from 'react';
import './Pages.css';
import axios from 'axios';
import Plot from 'react-plotly.js';




export default class Hype extends React.Component {
  state = {
    bestHypers:{},
    xaxis:[],
    yaxis:[]
  };

 
  

  componentDidMount() {
    console.log('Component mounted')
      //www
      axios.get(`http://localhost:5000/teamHypeatHome`)
      .then(res => {
        //const bestHomers = res.data;
        //console.log(res.data)
        this.setState({
          bestHypers: res.data
       })
      })
  }


 printbestHypers = () => {
  var array = []
  for (let k in this.state.bestHypers) {
    array.push(<div><li>{this.state.bestHypers[k]}</li></div>)
    this.state.xaxis.push(this.state.bestHypers[k][0])
    console.log(this.state.bestHypers[k][0])
    this.state.yaxis.push(this.state.bestHypers[k][1])
    console.log(this.state.bestHypers[k][1])
    //console.log(k + ' is ' + this.state.bestHomers[k])
  }
  return array;
}




  render() {
    return(
    <div className = 'hype'>
      <div>
        <h2>Teams Rankings, Top 10</h2>
        <b>Hype Factor</b>
        <div class = "container">
          <ol>
            {this.printbestHypers()}
          </ol>
          </div>
          <div>
          <Plot
        data={[
          {
            x: this.state.xaxis,
            y: this.state.yaxis,
            type: 'scatter',
            mode: 'lines+markers',
            marker: {color: 'red'},
          },
          {type: 'bar', x: this.state.xaxis, y: this.state.yaxis},
        ]}
        layout={ {width: 500, height: 500, title: 'Team Rankings'} }
      />
          </div>
        </div>
      </div>
    );
  }
};
