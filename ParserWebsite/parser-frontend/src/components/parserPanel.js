import '../style.scss';
import React from 'react';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
// import { } from '../redux/actions/index';

class ParserPanel extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      bytes: '',
    };
  }

  handleNameChange = (e) => {
    this.setState({
      name: e.target.value,
    });
  }

  handleBytesChange = (e) => {
    this.setState({
      bytes: e.target.value,
    });
  }

  addPost = () => {

  };

  render() {
    return (
      <div className="container">
        <div className="m-1">
          Enter Name: <input className="form-control" onChange={this.handleNameChange} value={this.state.name} />
        </div>
        <div className="m-1">
          Enter # of bytes: <input className="form-control" onChange={this.handleBytesChange} value={this.state.bytes} />
        </div>
      </div>
    );
  }
}


export default withRouter(connect(null, null)(ParserPanel));
