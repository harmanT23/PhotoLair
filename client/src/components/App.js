import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from '../actions';

import Header from './Header';
import Register from './Register'
import Login from './Login';
import ImageGrid from './ImageGrid';
import Sell from './Sell';

class App extends Component {  
  render() {
    return (
      <BrowserRouter>
        <Header />
        <div>
          <Switch>
            <Route path= '/' exact component={ImageGrid} />
            <Route path= '/register' exact component={Register} />
            <Route path='/login' exact component={Login} />
            <Route path='/sell' exact component={Sell} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default connect(null, actions)(App)
