import React from 'react';
import './Pages.css';
import axios from 'axios';
import Plot from 'react-plotly.js';


export default class Teams extends React.Component {
  state = {
    bestHomers: {},
    xaxis:[],
    yaxis:[]
  };

 


  componentDidMount() {
    console.log('Component mounted')
    axios.get(`http://localhost:5000/bestHomeTeam`)
      .then(res => {
        //const bestHomers = res.data;
        console.log(res.data)
        this.setState({
          bestHomers: res.data
       })
      })
  }

  printbestHomers = () => {
    var array = []
    for (let k in this.state.bestHomers) {
      array.push(<div><li>{this.state.bestHomers[k]}</li></div>)
      this.state.xaxis.push(this.state.bestHomers[k][0])
      console.log(this.state.bestHomers[k][0])
      this.state.yaxis.push(this.state.bestHomers[k][1])
      console.log(this.state.bestHomers[k][1])
    }
    return array;
 }






  render() {
    return(
      <div className = 'homewin'>
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
        layout={ {paper_bgcolor: 'grey' ,width: 850, height: 850, title: 'Top 10 Scoring Home Teams', plot_bgcolor: 'grey'} }
      />
          </div>
          <div>
          <h2>Best Home Teams (based on PPG in a single game)</h2>
          <ul className = "title">
            {this.printbestHomers()}
          </ul>
          </div>
        </div>
      </div>
          
      
    );
  }
};
