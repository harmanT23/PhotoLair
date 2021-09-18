import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import axiosInstance from '../api/axiosInstance';
import statusCodes from 'http-status-codes';
import Button from '@material-ui/core/Button';
import { withStyles } from '@material-ui/core/styles';

import * as actions from '../actions';
import { checkEmpty }  from '../utilities/checkEmptyObj';

const useStyles = (theme) => ({
  rightSideButtons: {
     marginLeft: 'auto',
     textDecoration: 'none',
     '&:hover': {
        backgroundColor: '#00ADB5',
        color: '#FFFFFF',
     },
  },
});

class BuyAndDownloadImage extends Component {
  state = {
    error: false,
  };

  handleClick = async () => {
    const res = await axiosInstance.get(
      '/images/' + this.props.imageID, {
        responseType: 'blob',
     }).catch((error) => {
      this.setState({ error: true });
      if (checkEmpty(this.props.userData)) {
        alert('You must be logged in to download an image');
      } if (error.response.status === statusCodes.INTERNAL_SERVER_ERROR) {
        alert('You don\'t have enough credits or image is out of stock. Sell images to gain more credits')
      }
    });

    if (!this.state.error) {
      // Download image 
      const url = window.URL.createObjectURL(
        new Blob([res.data], {
          type: res.headers['content-type'],
        })
      );
      
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute(
        'download', 
        this.props.image_name.replace(' ', '_') + '.jpeg'
      )
      document.body.appendChild(link);
      link.click();
      link.parentNode.removeChild(link);
      this.props.fetchUser();
    }
  };

  render() {
    const { classes } = this.props;
    return (
      <Button
        size='small'
        variant='outlined'
        color='#393E46' 
        className={classes.rightSideButtons} 
        onClick={this.handleClick}
      >
        Buy
      </Button>
    );
  }
}

function mapStateToProps({ userData }) {
  return { userData };
}

export default compose(
  withStyles(useStyles), 
  connect(mapStateToProps, actions)
)(BuyAndDownloadImage);
