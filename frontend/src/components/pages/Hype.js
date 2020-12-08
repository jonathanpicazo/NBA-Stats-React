import React from 'react';
import './Pages.css';
import axios from 'axios';



export default class Hype extends React.Component {
  state = {
    bestHypers:{}
  };

 


  componentDidMount() {
    console.log('Component mounted')
      //www
      axios.get(`http://localhost:5000/teamHypeatHome`)
      .then(res => {
        //const bestHomers = res.data;
        console.log(res.data)
        this.setState({
          bestHypers: res.data
       })
      })
  }



 printbestHypers = () => {
  var array = []
  for (let k in this.state.bestHypers) {
    array.push(<div><li>{this.state.bestHypers[k]}</li></div>)
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
        </div>
      </div>
    );
  }
};
