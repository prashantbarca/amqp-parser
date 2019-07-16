/* eslint-disable react/no-danger */
/* eslint-disable no-useless-constructor */

import '../style.scss';
import React from 'react';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';

class AllParsers extends React.Component {
  constructor(props) {
    super(props);
  }

  renderParser = () => {
    console.log(typeof this.props.all);
    return this.props.all.map((parser) => {
      return (
        <div className="card m-2">
          <div className="card-body">
            <p className="card-text"> {parser.name}</p>
            <p className="card-text">{parser.type}</p>
            <p className="card-text"> {parser.bytes}</p>
          </div>
        </div>
      );
    });
  }


  render() {
    if (this.props.all == null) {
      return (
        <div>
        Loading
        </div>
      );
    } else {
      return (
        <div>
          <div className="m-4">
            <div className="row">
              {this.renderParser()}
            </div>
          </div>
          <div>
            <button type="button">
            Create code
            </button>
          </div>
        </div>
      );
    }
  }
}

const mapStateToProps = (state) => {
  return (
    {
      all: state.parsers.all,
    }
  );
};


export default withRouter(connect(mapStateToProps, null)(AllParsers));
