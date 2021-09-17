import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import { withRouter } from 'react-router-dom';
import axiosInstance from '../api/axiosInstance';

import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';
import { 
  ValidatorForm, 
  TextValidator 
} from 'react-material-ui-form-validator';

import * as actions from '../actions';
import { isNumber }  from '../utilities/isNumber';


const useStyles = (theme) => ({
  paper: {
     marginTop: theme.spacing(8),
     display: 'flex',
     flexDirection: 'column',
     alignItems: 'center',
  },
  form: {
     width: '100%', // Fix IE 11 issue.
     marginTop: theme.spacing(1),
  },
  rightSideButtons: {
    textDecoration: 'none',
    '&:hover': {
       backgroundColor: '#3C52B2',
       color: '#FFFFFF',
    },
  },
  submit: {
     margin: theme.spacing(3, 0, 2),
  },
});

class Sell extends Component {
  state = {
    title: '',
    price: '',
    inventory: '',
    image: '',
    error: '',
  }

  componentDidMount() {
    //Ensure value is greater than or equal to zero
    ValidatorForm.addValidationRule('greaterThanEqZero', (value) => {
      if (!isNumber(value) && parseInt(value, 10) < 0) {
        return false;
      }
      return true;
    });
  }

  componentWillUnmount() {
    // Remove validation checks when component unmounted
    ValidatorForm.removeValidationRule('greaterThanEqZero');
  }

  handleChange = (e) => {
    this.setState({
      ...this.state,
      error: '',
      [e.target.name]: e.target.value
    });
  };

  handleInput = async (e) => {
    const selectedFile = e.target.files[0];
    this.state.image = selectedFile;
  };

  handleSubmit = async () => {
    this.props.fetchUser();

    console.log(this.state.image)

    const formData = new FormData();
    formData.append('image_name', this.state.title);
    formData.append('price', this.state.price);
    formData.append('inventory', this.state.inventory);
    formData.append('image', this.state.image);
    formData.append('user', this.props.userData.id);

    await axiosInstance.post('/images/', formData).catch((err) => {
       alert(err.msg);
    });

    this.props.history.push({
      pathname: '/'
    });
  }

 render() {
   const { classes } = this.props;
   return (
    <Container 
      component="main" 
      maxWidth="xs"
    >
      <CssBaseline />
      <div 
        className={classes.paper}
      >
        <Typography 
          component="h1" 
          variant="h3" 
          align="center" 
          color="textPrimary" 
          gutterBottom
        >
          Sell Your Photo
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
                variant='outlined'
                margin='normal'
                fullWidth
                id='title'
                label='title'
                name='title'
                autoFocus
                value={this.state.title}
                onChange={this.handleChange}
                validators={['required']}
                errorMessages={['Please enter a title']}
                error={this.state.error ? true : false}
                helperText={this.state.error}
              />
            </Grid>
            <Grid 
              item 
              xs={12}
            >
              <TextValidator
                variant='outlined'
                margin='normal'
                fullWidth
                id='price'
                label='price'
                name='price'
                autoFocus
                value={this.state.price}
                onChange={this.handleChange}
                validators={['required', 'greaterThanEqZero']}
                errorMessages={['Please enter a price in credits']}
                error={this.state.error ? true : false}
                helperText={this.state.error}
              />
            </Grid>
            <Grid 
              item 
              xs={12}
            >
              <TextValidator
                variant='outlined'
                margin='normal'
                fullWidth
                id='inventory'
                label='inventory'
                name='inventory'
                autoFocus
                value={this.state.inventory}
                onChange={this.handleChange}
                validators={['required', 'greaterThanEqZero']}
                errorMessages={['Please enter a inventory']}
                error={this.state.error ? true : false}
                helperText={this.state.error}
              />
            </Grid>
          </Grid>
          <label>
            <input 
              accept="image/*" 
              type="file" 
              style={{ display: 'none' }} 
              onChange={this.handleInput} 
            />
            <Button
              color='primary' 
              className={classes.rightSideButtons} 
              component="span"
              variant='outlined'
            >
              Upload
            </Button>
          </label>
          <Button
            type='submit'
            fullWidth
            variant='contained'
            color='primary'
            className={classes.submit}
          >
            Submit
          </Button>
        </ValidatorForm>
      </div>
    </Container>
   ); 
 }
}

function mapStateToProps({ userData }) {
  return { userData };
}

export default compose(
  withStyles(useStyles), 
  withRouter, 
  connect(mapStateToProps, actions)
)(Sell);
