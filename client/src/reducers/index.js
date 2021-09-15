import { combineReducers } from 'redux';
import userReducer from './userReducer';
import imageReducer from './imageReducer';

export default combineReducers({
  userData:userReducer,
  imageList: imageReducer
})
