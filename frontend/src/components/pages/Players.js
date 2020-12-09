import React from 'react';
import '../../App.css';
import axios from 'axios';

export default class Players extends React.Component {
  state = {
    playerName: '',
    season:'',
    fg_pct:'',
    fg3_pct:'',
    blk:'',
    pp:'',
  };

  handleChange = (evt) => {
    evt.preventDefault();
    this.setState({[evt.target.name]: evt.target.value});
  }
  insertfunc = event => {
    event.preventDefault();
    const player = {
      playerName: this.state.playerName,
      season: this.state.season,
      fg_pct: this.state.fg_pct,
      fg3_pct: this.state.fg3_pct,
      blk: this.state.blk,
      pp: this.state.pp
    }
    console.log(player);

    axios.post(`http://localhost:5000/UpdateBlocks`, { player })
      .then(res => {
        console.log(res);
        console.log(res.data);
        this.setState({
          bestBlockers: res.data
       })
      })
      axios.post(`http://localhost:5000/UpdatePlayerPerformance`, { player })
      .then(res => {
        console.log(res);
        console.log(res.data);
        this.setState({
          bestPlayers: res.data
       })
      })

      axios.post(`http://localhost:5000/Updatethreeptgoal`, { player })
      .then(res => {
        console.log(res);
        console.log(res.data);
        this.setState({
          bestShooters: res.data
       })
      })

      axios.post(`http://localhost:5000/Updatefg`, { player })
      .then(res => {
        console.log(res);
        console.log(res.data);
        this.setState({
          bestFieldGoalers: res.data
       })
      })


};

  render(){
    return(
      <div>
        <div className = 'hype'>
      <form onSubmit={this.insertfunc}>
            <label>
            <b>Insert player details: </b>
              <div> <input type="text" placeholder = "Enter player name" name = "playerName" onChange = {this.handleChange}/> </div>
              <div> <input type="text" placeholder = "Enter season played" name = "season" onChange = {this.handleChange}/> </div>
              <div> <input type="text" placeholder = "Enter FG%" name = "fg_pct" onChange = {this.handleChange}/> </div>
              <div> <input type="text" placeholder = "Enter 3PT%" name = "fg3_pct" onChange = {this.handleChange}/> </div>
              <div> <input type="text" placeholder = "Enter Blocks" name = "blk" onChange = {this.handleChange}/> </div>
              <div> <input type="text" placeholder = "Enter Player Performance" name = "pp" onChange = {this.handleChange}/> </div>
              <button type = "submit"> Submit </button>
            </label>
          </form>
          </div>
      </div>
    )
  }
};
