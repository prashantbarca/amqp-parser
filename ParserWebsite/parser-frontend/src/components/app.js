/* eslint-disable react/prefer-stateless-function */
import '../style.scss';
import {
  BrowserRouter as Router, Route, Switch,
} from 'react-router-dom';
import React from 'react';
import Main from './mainPanel';

class App extends React.Component {
  render() {
    return (
      <Router>
        <div>
          <Switch>
            <Route exact path="/" component={Main} />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
