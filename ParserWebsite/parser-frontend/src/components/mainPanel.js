/* eslint-disable react/prefer-stateless-function */
import '../style.scss';
import React from 'react';
import { connect } from 'react-redux';
import ButtonPanel from './buttonPanel';
import AllParsers from './AllParsers';
import ParserPanel from './parserPanel';

class Main extends React.Component {
  render() {
    return (
      <div>
        <div>
          <ButtonPanel />
        </div>
        <div>
          <AllParsers />
        </div>
        <div>
          <ParserPanel />
        </div>
      </div>
    );
  }
}

export default connect(null, null)(Main);
