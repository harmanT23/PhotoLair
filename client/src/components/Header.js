import React, { Fragment, Component } from 'react';
import { connect } from 'react-redux';
import { compose } from 'redux';
import SizeMe from 'react-sizeme'
import * as actions from '../actions';
import AccountBoxIcon from '@material-ui/icons/AccountBox';
import AppBar from '@material-ui/core/AppBar'
import Button from '@material-ui/core/Button';
import CameraIcon from '@material-ui/icons/Camera';
import CssBaseline from '@material-ui/core/CssBaseline';
import Link from "@material-ui/core/Link";
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import MonetizationOnIcon from '@material-ui/icons/MonetizationOn';
import Toolbar from '@material-ui/core/Toolbar';
import Tooltip from '@material-ui/core/Tooltip';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';

const useStyles = (theme) => ({
  root: {
     flexGrow: 1,
  },
  mainButton: {
     textDecoration: 'none',
     color: '#FF6701',
  },
  title: {
     flexGrow: 1,
     color: '#FFFFFF',
  },
  rightSideButtons: {
     textDecoration: 'none',
     color: '#FFFFFF',
  },
  leftAligned: {
     marginLeft: 'auto',
  },
  dropdown: {
     '&:focus': {
        backgroundColor: theme.palette.primary.main,
        '& .MuiListItemIcon-root, & .MuiListItemText-primary': {
           color: theme.palette.common.white,
        },
     },
  },
});


class Header extends Component {
  state = {
    dropDownMenu: null,
  };

  handleClick = (e) => {
    this.setState({ dropDownMenuElement: e.currentTarget });
  };

  handleClose = () => {
    this.setState({ dropDownMenuElement: null });
  };

  handleLogout = () => {
    this.handleClose();
    this.props.logoutUser();
    this.props.history.push({
      pathname: '/',
    });
  };

  menuDropdown = () => {
    if (this.state.dropDownMenuElement) {
       return (
          <Menu
             id='account-dropdown'
             anchorEl={this.state.dropDownMenuElement}
             getContentAnchorEl={null}
             anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'right',
             }}
             transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
             }}
             elevation={0}
             keepMounted
             open={Boolean(this.state.dropDownMenuElement)}
             onClose={this.handleClose}
             border='1px solid #d3d4d5'
             visible={this.state.dropDownMenuElement}
          >
              <MenuItem className='dropdown' onClick={this.handleLogout}>
                Logout
             </MenuItem>
          </Menu>
       );
    } else {
       return;
    }
  };

  getMenuItems(userData, classes, width) {
    /*
      If user is authenticated, we display a menu bar with their account
      balance, icon button with sign-out bottom as drop down.
    */
    console.log(userData)
    if(userData) {
      return (
        <Fragment>
          <Tooltip 
            title='Spend credits to buy an image. Gain credits by selling images.'
            aria-label='add'
          >
            <Button 
              color='inherit'
              className={classes.rightSideButtons}
            >
              <Typography
                variant='h6'
                className={classes.title}
              >
                <MonetizationOnIcon />
                {`${userData.credits}`}
              </Typography>
            </Button>
          </Tooltip>
          <Button
            aria-controls='account-dropdown'
            aria-haspopup='true'
            onClick={this.handleClick}
            className={classes.rightSideButtons}
          >
            <AccountBoxIcon 
              style={{ marginRight: '6px' }}
              color='inherit'
            />
            <Typography
              variant='h6'
              className={classes.title}
            >
              {`${userData.username}`}
            </Typography>
          </Button>
          {this.menuDropdown()}
        </Fragment>
      );
    } else {
      return;
    }
  }

  getLoginButton(userData, classes) {
    if (userData === false) {
      return (
        <Link 
          to='/login' 
          className={classes.rightSideButtons}
        >
          <Button
            color='inherit'
          >
            <Typography 
              variant='h5'
              className={classes.title}
            >
              Login
            </Typography>
          </Button>
        </Link>
      );
    } else {
      return;
    }
  }

  getLabelOrBoth(width, classes) {
    return (
      <Fragment>
        <CameraIcon />
        {width >= 500 && (
          <Typography
            style={{ marginLeft: '6px' }}
            variant='h5'
            className={classes.title}
          >
            PhotoLair
          </Typography>
        )}
      </Fragment>
    );
  }

  render() {
    const {
      size: {width},
      classes
    } = this.props 

    return (
      <div
        className={classes.root}
      >
        <CssBaseline />
        <AppBar
          position='static'
          color='primary'
        >
          <Toolbar>
            <Link
              to='/'
              className={classes.mainButton}
            >
              <Button
                color='inherit'
              >
                {this.getLabelOrBoth(width, classes)}
              </Button>
            </Link>
            <div
              className={classes.leftAligned}
            >
              {this.getMenuItems(this.props.userData, classes, width)}
              {this.getLoginButton(this.props.userData, classes)}
            </div>
          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

function mapStateToProps({ userData }) {
  return { userData };
}

export default compose(
  SizeMe(), 
  withStyles(useStyles), 
  connect(mapStateToProps, actions)
)(Header);