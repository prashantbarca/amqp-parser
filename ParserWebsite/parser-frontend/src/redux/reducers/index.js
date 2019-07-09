
// the starting point for your redux store
// this defines what your store state will look like
import { combineReducers } from 'redux';
import ParserReducer from './parserReducer';

const rootReducer = combineReducers({
  parsers: ParserReducer,
});

export default rootReducer;
