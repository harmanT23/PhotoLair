import axiosInstance from '../api/axiosInstance';
import statusCodes from 'http-status-codes';
import {
  REGISTER,
  LOGIN,
  LOGOUT,
  FETCH_IMAGE_LIST
} from './types';

// userData consists of username and password for registration
export const registerUser = (userData) => async (dispatch) => {
  const res = await axiosInstance.post('users/', userData)
  if (res.status !== statusCodes.CREATED) {
    return false;
  } else {
    dispatch({type: REGISTER, payload: null});
    return true;
  }
};

export const loginUser = (userData) => async (dispatch) => {
  const res = await axiosInstance
    .post('token/', {
      username: userData.username,
      password: userData.password,
    }).then((res) => {
      localStorage.setItem('access_token', res.data.access);
      localStorage.setItem('refresh_token', res.data.refresh);
      axiosInstance.defaults.headers['Authorization'] =
          'JWT ' + localStorage.getItem('access_token');
    })

  if (res.status !== statusCodes.OK) {
    return false;
  } else {
    dispatch({type: LOGIN, payload: res.data});
    return true;
  }
}

export const logoutUser = () => async (dispatch) => {
  const res = await axiosInstance.post('token/blacklist', {
    refresh_token: localStorage.getItem('refresh_token'),
  });
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  axiosInstance.defaults.headers['Authorization'] = null;
  dispatch({type: LOGOUT, payload: res.data})
}

export const fetchImageList = () => async (dispatch) => {
  const res = await axiosInstance.get('/images')
  dispatch({type: FETCH_IMAGE_LIST, payload: res.data})
}