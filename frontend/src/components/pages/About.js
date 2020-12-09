import React from 'react';
import '../../App.css';
import axios from 'axios';
 
export default class About extends React.Component {

  state = {
    teamName: '',
    season: '',
    dataList: [[]]
  };


  insertfunc = event => {
    event.preventDefault();
    const team = {
      teamName: this.state.teamName,
      season: this.state.season
    }
    console.log(team);

    axios.post(`http://localhost:5000/searchTeams`, { team })
      .then(res => {
        console.log(res);
        console.log(res.data);
        this.setState({
          dataList: res.data
       })
      })
      
}



  handleChange = (evt) => {
    evt.preventDefault();
    this.setState({[evt.target.name]: evt.target.value});
  }


  printTable() {
    let array = []
    if (this.state.dataList.length > 1) {
      for (let k in this.state.dataList) {
        //array.push(<div><tr>)
        array.push(<tr>
          
          <th><b>{this.state.dataList[k][0]}</b></th>
          <th>{this.state.dataList[k][1]}</th>
          <th>{this.state.dataList[k][2]}</th>
          <th>{this.state.dataList[k][3]}</th>
          <th>{this.state.dataList[k][4]}</th>
          <th>{this.state.dataList[k][5]}</th>
          <th>{this.state.dataList[k][6]}</th>
        </tr>
        
          
          
          )
        {/* array.push(<th>{this.state.dataList[k][1]}</th>)
        array.push(<th>{this.state.dataList[k][2]}</th>)
        array.push(<th>{this.state.dataList[k][3]}</th>)
        array.push(<th>{this.state.dataList[k][4]}</th>)
        array.push(<th>{this.state.dataList[k][5]}</th></tr>) */}
        //array.push(</tr></div>)
      }
    }
    return array;
  }



  render(){
    return(
      <div>
        <div className = 'search'>
          <h1>Search for Team Stats Per Game</h1>
        <form onSubmit = {this.insertfunc}>
          <div> <input type="text" placeholder = "Enter team name" name = "teamName" onChange = {this.handleChange}/> </div>
          <div> <input type="text" placeholder = "Enter season" name = "season" onChange = {this.handleChange}/> </div>
          <button type = "submit"> Submit </button>
        </form>
        <table>
          <tr>
            <th>Opposing Team</th>
            <th>PTS</th>
            <th>FG_PCT</th>
            <th>FT_PCT</th>
            <th>3PT</th>
            <th>AST</th>
            <th>REB</th>
          </tr>
          {this.printTable()}
        </table>

        </div>
      </div>
    )
  }
};