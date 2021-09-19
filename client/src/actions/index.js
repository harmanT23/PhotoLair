import axiosInstance from '../api/axiosInstance';
import statusCodes from 'http-status-codes';
import {
  REGISTER,
  LOGIN,
  LOGOUT,
  FETCH_USER,
  FETCH_IMAGE_LIST
} from './types';

// userData consists of username and password for registration
export const registerUser = (userData) => async (dispatch) => {
  const res = await axiosInstance.post('users/', userData)

  if (!res || res.status !== statusCodes.CREATED) {
    return false;
  } else {
    dispatch({type: REGISTER, payload: null});
    return true;
  }
};

export const loginUser = (userData) => async (dispatch) => {
  const res = await axiosInstance.post('token/', {
      username: userData.username,
      password: userData.password,
    });

    if (!res || res.status !== statusCodes.OK) {
      return false;
    } else {
      dispatch({type: LOGIN, payload: res.data});
      return res.data;
    }
}

export const logoutUser = () => async (dispatch) => {
  await axiosInstance.post('token/blacklist/',{
    refresh_token: localStorage.getItem('refresh_token'),
  });
  dispatch({type: LOGOUT, payload: null})
}

export const fetchUser = () => async (dispatch) => {
  const res = await axiosInstance.get('users/me').catch(() => {
    return false;
  });

  if (!res || res.status !== statusCodes.OK) {
    return false;
  } else {
    dispatch({type: FETCH_USER, payload: res.data})
    return true;
  }
}

export const fetchImageList = () => async (dispatch) => {
  const res = await axiosInstance.get('/images')

  if (!res || res.status !== statusCodes.OK) {
    return false;
  } else {
    dispatch({type: FETCH_IMAGE_LIST, payload: res.data})
    return true;
  }

}
