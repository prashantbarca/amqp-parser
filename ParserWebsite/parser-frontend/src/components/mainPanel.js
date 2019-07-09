/* eslint-disable react/prefer-stateless-function */
import '../style.scss';
import React from 'react';
import { connect } from 'react-redux';
import {
  Container,
  Col,
  Row,
} from 'react-bootstrap';
import ButtonPanel from './buttonPanel';
import AllParsers from './AllParsers';
// import ParserPanel from './parserPanel';

class Main extends React.Component {
  render() {
    return (
      <div>
        <Container>
          <Row>
            <Col xs={3}>
              <ButtonPanel />
            </Col>
            <Col xs={9}>
              <AllParsers />
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default connect(null, null)(Main);
