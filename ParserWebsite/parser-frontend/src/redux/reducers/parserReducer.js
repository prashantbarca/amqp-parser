/* eslint no-param-reassign:0 new-cap:0 */
import { ActionTypes } from '../actions';

const initialState = {
  all: [],
};

const ParserReducer = (
  state = initialState, action,
) => {
  switch (action.type) {
    case ActionTypes.ADD_PARSER: {
      return { ...state, all: [...state.all, action.payload] };
    }
    default:
      return state;
  }
};

export default ParserReducer;
