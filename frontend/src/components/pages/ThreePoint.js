import React from 'react';
import './Pages.css';
import axios from 'axios';
import Plot from 'react-plotly.js';



export default class ThreePoint extends React.Component {
  state = {
    bestShooters:{},
    xaxis: [],
    yaxis: []
  };

 


  componentDidMount() {
    console.log('Component mounted')
      axios.get(`http://localhost:5000/Updatethreeptgoal`)
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
  let name = ''
  for (let k in this.state.bestShooters) {
    array.push(<div><li>{this.state.bestShooters[k]}</li></div>)
    name = this.state.bestShooters[k][0]
    name = name.substring(0, name.length - 2);
    this.state.xaxis.push(name)
    console.log(this.state.bestShooters[k][0])
    this.state.yaxis.push(this.state.bestShooters[k][1])
    console.log(this.state.bestShooters[k][1])
    }
  return array;
}


  render() {
    return(
      <div className = 'threept'>
        
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
        layout={ {paper_bgcolor: 'grey' ,width: 850, height: 850, title: 'Top 10 3pt Shooters', plot_bgcolor: 'grey'} }
      />
          </div>
          <div>
          <h2>3PT% in a Game (per 10+ attempts)</h2>
          <ul className = "title">
            {this.printBestShooters()}
          </ul>
          </div>
          </div>
      </div>
    );
  }
};
