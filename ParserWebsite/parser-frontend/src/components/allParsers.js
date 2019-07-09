/* eslint-disable react/no-danger */
/* eslint-disable no-useless-constructor */

import '../style.scss';
import React from 'react';
import { NavLink, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { addParser } from '../redux/actions/index';

class AllParsers extends React.Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    addParser();
  }

  renderPosts() {
    return this.props.all.map((post) => {
      return (
        <NavLink to={`/posts/${post.id}`} key={post.id}>
          <div className="card m-2">
            <div className="card-body">
              <p className="card-text"> {post.Name}</p>
              <p className="card-text"> {post.btyes}</p>
              <p className="card-text">{post.type}</p>
            </div>
          </div>
        </NavLink>
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
        <div className="m-4">
          <div className="row">
            {this.renderPosts()}
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


export default withRouter(connect(mapStateToProps, {})(AllParsers));
