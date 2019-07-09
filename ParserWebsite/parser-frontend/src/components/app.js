/* eslint-disable react/prefer-stateless-function */
import '../style.scss';
import {
  BrowserRouter as Router, Route, Switch,
} from 'react-router-dom';
import React from 'react';
import Main from './mainPanel';
import ParserPanel from './parserPanel';

class App extends React.Component {
  render() {
    return (
      <Router>
        <div>
          <Switch>
            <Route exact path="/" component={Main} />
            <Route path="/add" component={ParserPanel} />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
