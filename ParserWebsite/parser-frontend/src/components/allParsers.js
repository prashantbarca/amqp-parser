/* eslint-disable jsx-a11y/no-static-element-interactions */
/* eslint-disable react/no-danger */
/* eslint-disable no-useless-constructor */

import '../style.scss';
import React from 'react';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faEdit, faCheckCircle } from '@fortawesome/free-solid-svg-icons';

library.add(faEdit);
library.add(faCheckCircle);

class AllParsers extends React.Component {
  constructor(props) {
    super(props);
  }

  editSymbol = () => {
    return (this.props.isEdit
      ? (
        <div onClick={this.editNote}>
          <i>
            <FontAwesomeIcon key="editIcon" icon={faCheckCircle} />
          </i>
        </div>
      )
      : (
        <div onClick={this.editNote}>
          <i>
            <FontAwesomeIcon key="editIcon" icon={faEdit} />
          </i>
        </div>
      )
    );
  }

  renderParser = () => {
    console.log(typeof this.props.all);
    return this.props.all.map((parser) => {
      return (
        <div className="card m-2">
          {this.editSymbol()}
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
