import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from '../actions';

import Header from './Header';
import Register from './Authorization/register'

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Header />
        <div>
          <Switch>
            <Route path= '/' exact component={Register} />
            <Route path= '/register' exact component={Register} />
            <Route path='/login' exact component={Register} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default connect(null, actions)(App)