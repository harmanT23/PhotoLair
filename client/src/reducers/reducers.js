import { combineReducers } from 'redux';
import userReducer from './userReducer';
import imageReducer from './imageReducer';

export default combineReducers({
  user_data:userReducer,
  image_list: imageReducer
})
