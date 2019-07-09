/* eslint-disable react/prefer-stateless-function */
import { connect } from 'react-redux';
import '../style.scss';
import React from 'react';
import {
  Button,
  Col,
  Row,
} from 'react-bootstrap';

class ButtonPanel extends React.Component {
  onPress8 = () => {
    console.log('hello world');
  }

  onPress16 = () => {
    console.log('hello world');
  }

  onPress32 = () => {
    console.log('hello world');
  }

  onPressCh = () => {
    console.log('hello world');
  }

  render() {
    return (
      <div>
        <Row>
          <Col xs={12}>
            <Button onClick={this.onPress8}>
            add h.uint8
            </Button>
          </Col>
          <Col xs={12}>
            <Button onClick={this.onPress16}>
            add h.int16
            </Button>
          </Col>
          <Col xs={12}>
            <Button onClick={this.onPress32}>
            add uint32
            </Button>
          </Col>
          <Col xs={12}>
            <Button onClick={this.onPressCh}>
            add h.ch
            </Button>
            <Col xs={12}>
              <Button onClick={this.onPressCh}>
            add h.ch_range
              </Button>
            </Col>
            <Col xs={12}>
              <Button onClick={this.onPressCh}>
            add h.int_range
              </Button>
            </Col>
            <Col xs={12}>
              <Button onClick={this.onPressCh}>
            add h.token
              </Button>
            </Col>
          </Col>
        </Row>
      </div>
    );
  }
}

export default connect(null, null)(ButtonPanel);
