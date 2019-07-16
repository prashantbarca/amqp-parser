export const ActionTypes = {

  ADD_PARSER: 'ADD_PARSER',
  // Auth actions
  AUTH_ERROR: 'AUTH_ERROR',
};

export function authError(error) {
  return {
    type: ActionTypes.AUTH_ERROR,
    message: error,
  };
}

export function addParser(parserType) {
  return (dispatch) => {
    const parser = {
      name: '',
      type: '',
      bytes: parserType,
    };
    dispatch({ type: ActionTypes.ADD_PARSER, payload: parser });
  };
}
