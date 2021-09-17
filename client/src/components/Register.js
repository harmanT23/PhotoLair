import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import { withRouter } from 'react-router-dom';
import axiosInstance from '../api/axiosInstance';

import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import { Link } from 'react-router-dom';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { ValidatorForm, TextValidator } from 'react-material-ui-form-validator';
import { withStyles } from '@material-ui/core/styles';

import * as actions from '../actions';

const useStyles = (theme) => ({
   paper: {
      marginTop: theme.spacing(8),
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
   },
   avatar: {
      margin: theme.spacing(1),
      backgroundColor: theme.palette.secondary.main,
   },
   form: {
      width: '100%',
      marginTop: theme.spacing(3),
   },
   submit: {
      margin: theme.spacing(3, 0, 2),
   },
});

class Register extends Component {
  state = {
    username: '',
    password: '',
    error: ''
  };

  componentDidMount() {
    //Ensure the length does not exceed max set by backend
    ValidatorForm.addValidationRule('usernameLength', (value) => {
      if (value.length === 0 || value.length > 150) {
        return false;
      }
      return true;
    });

    //Ensure password length is at least 8 chars as required by backend
    ValidatorForm.addValidationRule('passwordLength', (value) => {
      if (value.length < 8) {
        return false;
      }
      return true;
    });
  }

  componentWillUnmount() {
    // Remove validation checks when component unmounted
    ValidatorForm.removeValidationRule('usernameLength');
    ValidatorForm.removeValidationRule('passwordLength');
  }

  handleChange = (e) => {
    this.setState({
      ...this.state,
      [e.target.name] : e.target.value,
      error: ''
    })
  };

  handleSubmit = () => {
    //Register then login the user.
    this.props.registerUser({
      username: this.state.username,
      password: this.state.password
    }).then((result) => {
      if (result) {
        this.props.loginUser({
          username: this.state.username,
          password: this.state.password
        }).then((loginResult) => {
          if (loginResult) {
            localStorage.setItem('access_token', loginResult.access);
            localStorage.setItem('refresh_token', loginResult.refresh);
            axiosInstance.defaults.headers['Authorization'] = 
            'JWT ' + localStorage.getItem('access_token');
            this.props.history.push({
              pathname: '/'
            });
          }
        });
      } else {
        this.setState({
          error: 'This username is already taken.'
        });
      }
    });
  };

  render() {
    const { classes } = this.props;
    return (
      <Container 
        component='main' 
        maxWidth='xs'
      >
        <CssBaseline />
        <div 
          className={classes.paper}
        >
          <Avatar 
            className={classes.avatar}
          >
            <LockOutlinedIcon />
          </Avatar>
          <Typography 
              component="h1" 
              variant="h5"
          >
              Register
          </Typography>
          <ValidatorForm 
            onSubmit={this.handleSubmit} 
            className={classes.form}
          >
            <Grid 
              container 
              spacing={2}
            >
              <Grid 
                item 
                xs={12}
              >
                <TextValidator
                  validators={['required', 'usernameLength']}
                  variant='outlined'
                  fullWidth
                  id='username'
                  label='username'
                  name='username'
                  value={this.state.username}
                  onChange={this.handleChange}
                  errorMessages={[
                    'Please enter a username',
                    'Username must be between 1 character and 150 characters in length'
                  ]}
                  error={this.state.error ? true : false}
                  helperText={this.state.error}
                />
              </Grid>
              <Grid 
                item 
                xs={12}
              >
                <TextValidator
                  validators={['required', 'passwordLength']}
                  variant='outlined'
                  fullWidth
                  id='password'
                  label='password'
                  name='password'
                  type={'password'}
                  value={this.state.password}
                  onChange={this.handleChange}
                  errorMessages={[
                    'Please enter a password',
                    'Password must be at least 8 characters in length'
                  ]}
                  error={this.state.error ? true : false}
                  helperText={this.state.error}
                />
              </Grid>
            </Grid>
            <Button
              type='submit'
              fullWidth
              variant='contained'
              color='primary'
              className={classes.submit}
            >
              Register
            </Button>
            <Link
              to='/login'
              variant='body2'
            >
              Already have an account? Login
            </Link>
          </ValidatorForm>
        </div>
      </Container>
    );
  }
}

export default compose(
  withStyles(useStyles), 
  withRouter, 
  connect(null, actions)
)(Register)