import {
  REGISTER,
  LOGIN,
  LOGOUT,
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
    default:
      return state;
  }
}