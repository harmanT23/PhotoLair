import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import { withRouter } from 'react-router-dom';
import { Link } from 'react-router-dom';

import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { withstyles } from '@mui/material/styles';
import { 
  ValidatorForm, 
  TextValidator 
} from 'react-material-ui-form-validator';

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
     width: '100%', // Fix IE 11 issue.
     marginTop: theme.spacing(1),
  },
  submit: {
     margin: theme.spacing(3, 0, 2),
  },
});


class Login extends Component {
  state = {
    username: '',
    password: '',
    error: '',
  }

  handleChange = (e) => {
    this.setState({
      ...this.state,
      error: '',
      [e.target.name]: e.target.value
    });
  };

  handleSubmit = () => {
    this.props.loginUser({
      username: this.state.username,
      password: this.state.pssword
    }).then((result) => {
      if(result) {
        this.props.history.push({
          pathname: '/',
        });
      }
      else {
        this.setState({
          error: result ? '' : 'Invalid username or password entered'
        })
      }
    }).catch((err) => {
      alert(err.response.data.msg)
    });
  };
  
  getCopyright() {
    return (
      <Typography 
        variant="body2" 
        color="text.secondary" 
        align="center"
      >
        {'Copyright © '}
        <Link 
          color="inherit" 
          href="/"
        >
          PhotoLair
        </Link>{' '}
        {new Date().getFullYear()}
        {'.'}
      </Typography>
    );
  };

  render() {
    const { classes } = this.props;

   
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography
          component='h1'
          variant='h5'
        >
          Login
        </Typography>
        <ValidatorForm
          onSubmit={this.handleSubmit}
          className={classes.form}
        >
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <TextValidator
                variant='outlined'
                margin='normal'
              >

              </TextValidator>
            </Grid>
          </Grid>

        </ValidatorForm>
      </div>
    </Container>

  };

}

export default compose(
  withStyles(useStyles), 
  withRouter, 
  connect(null, actions)
)(Login);


