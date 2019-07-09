/* eslint no-param-reassign:0 new-cap:0 */
import { ActionTypes } from '../actions';

const initialState = {
  all: [],
  current: {},
};

const ParserReducer = (
  state = initialState, action,
) => {
  switch (action.type) {
    case ActionTypes.ALL_PARSERS: {
      return { ...state, all: action.payload };
    }
    default:
      return state;
  }
};

export default ParserReducer;
