import React from 'react';
import ReactDOM from 'react-dom';
import Homepage from './homepage.jsx';
import Bootstrap from 'bootstrap/dist/css/bootstrap.css';
import { Router, Route, IndexRoute, Link, IndexRedirect, hashHistory, History } from 'react-router'

const App = React.createClass({

  render() {
    return (
      <div>
        <nav className="navbar navbar-default">
          <div className="container-fluid">              
            <div className="navbar-header">
              <a className="navbar-brand" href="/">Christmas Lights</a>
            </div>                
          </div>
        </nav>
        <div>
          <div className="container">
            {this.props.children}
          </div>
        </div>
      </div>
    )
  }
})

ReactDOM.render(
    <Router history={hashHistory}>
        <Route path="/" component={App}>
            <IndexRedirect to="/home" />
            <Route path="home" component={Homepage} />        
        </Route>
    </Router>,
    document.getElementById('react-app')
);
