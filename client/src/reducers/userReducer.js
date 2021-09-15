import {
  REGISTER,
  LOGIN,
  LOGOUT,
  FETCH_USER,
}  from '../actions/types';

const initialState = {};

export default function (state=initialState, action) {
  switch(action.type) {
    case REGISTER:
      return state;
    case LOGIN:
      return action.payload;
    case LOGOUT:
      return false;
    case FETCH_USER:
      return action.payload || false;
    default:
      return state;
  }
}