import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';
import JobSearch from './components/jobs';
import NavBar from './components/navbar';
import Admin from './components/admin';
import Application from './components/application';
import Applications from './components/applications';
import Test from './components/test';
import Profile from './components/profile';

class Router extends Component {
	render() {
		return (
			<Switch>
				<Route exact path="/" component={NavBar} />
				<Route exact path="/about" component={NavBar} />
				<Route path="/jobs" component={JobSearch} />
				<Route path="/locations" component={NavBar} />
				<Route path="/help" component={NavBar} />
				<Route path="/apply" component={Application} />
				<Route path="/admin" component={Admin} />
				<Route path="/review" component={Applications} />
				<Route path="/test" component={Test} />
				<Route path="/profile" component={Profile} />
			</Switch>			
		);
	}
}

export default Router;
