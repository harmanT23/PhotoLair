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
       backgroundColor: '#00ADB5',
       color: '#FFFFFF',
    },
    primary: {
      main: '#393E46'
    }
  },
  submit: {
     margin: theme.spacing(3, 0, 2),
     '&:hover': {
      backgroundColor: '#00ADB5',
      color: '#FFFFFF',
     },
     primary: {
      main: '#393E46'
    }
  },
});

class SellPage extends Component {
  state = {
    title: '',
    price: '',
    inventory: '',
    image: '',
    error: '',
  }

  handleChange = (e) => {
    this.setState({
      ...this.state,
      [e.target.name]: e.target.value,
      error: '',
    });
  };

  handleInput = async (e) => {
    const selectedFile = e.target.files[0];
    this.state.image = selectedFile;
  };

  handleSubmit = async () => {
    const formData = new FormData();
    formData.append('image_name', this.state.title);
    formData.append('price', this.state.price);
    formData.append('inventory', this.state.inventory);
    formData.append('image', this.state.image);
    formData.append('user', this.props.location.state.userData.id);

    const res = await axiosInstance.post('/images/', formData).catch(() => {
       alert(
         'Unable to upload image. One or more of the fields ' +
         'Were filled out incorrectly. Please try again.'
       )
    });

    if (res) {
        this.props.history.push({
        pathname: '/'
      });
    }
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
                validators={['required']}
                variant='outlined'
                margin='normal'
                fullWidth
                id='title'
                label='Title'
                name='title'
                placeholder='Enter title for your image i.e. Scenic Views'
                value={this.state.title}
                onChange={this.handleChange}
                errorMessages={['Please enter a title']}
                helperText={this.state.error}
              />
            </Grid>
            <Grid 
              item 
              xs={12}
            >
              <TextValidator
                validators={[
                  'required', 
                  'matchRegexp:^[0-9]+$',
                  'minNumber:0',
                ]}
                variant='outlined'
                margin='normal'
                fullWidth
                id='price'
                label='Price'
                name='price'
                placeholder='Enter price in credits (a positive number) i.e. 2'
                autoFocus
                value={this.state.price}
                onChange={this.handleChange}
                errorMessages={[
                  'Please enter a price in credits',
                  'Please enter a Integer as the price',
                  'The minimum allowed price is 0',
                ]}
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
                label='Inventory'
                name='inventory'
                placeholder='Enter inventory as a positive integer (i.e. 5)'
                autoFocus
                value={this.state.inventory}
                onChange={this.handleChange}
                validators={[
                  'required',
                  'matchRegexp:^[0-9]+$', 
                  'minNumber:1',
                ]}
                errorMessages={[
                  'Please enter a inventory',
                  'Please enter a Integer',
                  'There must be at least 1 image in inventory',
                ]}
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

export default compose(
  withStyles(useStyles), 
  withRouter, 
  connect(null, actions)
)(SellPage);
