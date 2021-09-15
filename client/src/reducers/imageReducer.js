import { FETCH_IMAGE_LIST } from '../actions/types';

const initialState = {};

export default function (state=initialState, action) {
  switch(action.type) {
    case FETCH_IMAGE_LIST:
      return action.payload;
    default:
      return state
  }
}
