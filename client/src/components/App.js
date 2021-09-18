import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from '../actions';

import Header from './Header';
import RegisterPage from './RegisterPage'
import LoginPage from './LoginPage';
import ImageGrid from './ImageGrid';
import SellPage from './SellPage';

class App extends Component {  
  render() {
    return (
      <BrowserRouter>
        <Header />
        <div>
          <Switch>
            <Route path= '/' exact component={ImageGrid} />
            <Route path= '/register' exact component={RegisterPage} />
            <Route path='/login' exact component={LoginPage} />
            <Route path='/sell' exact component={SellPage} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default connect(null, actions)(App)
