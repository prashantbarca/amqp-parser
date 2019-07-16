/* eslint-disable react/prefer-stateless-function */
import { connect } from 'react-redux';
import '../style.scss';
import React from 'react';
import {
  Button,
  Col,
  Row,
} from 'react-bootstrap';
import { addParser } from '../redux/actions';

class ButtonPanel extends React.Component {
  onPress8 = () => {
    this.props.addParser('uint8');
  }

  onPress16 = () => {
    this.props.addParser('uint16');
  }

  onPress32 = () => {
    this.props.addParser('uint32');
  }

  onPressCh = () => {
    this.props.addParser('h.ch');
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

export default connect(null, { addParser })(ButtonPanel);
