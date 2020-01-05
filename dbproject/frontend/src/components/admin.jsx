import React, { Component } from 'react';
import { Button } from 'reactstrap';
import SignInForm from './login';
import RegisterForm from './register';

class Admin extends Component {
	constructor(props) {
		super(props);
		this.state = {
			register: false
		};

		this.switch = this.switch.bind(this);
	}
	switch() {
		this.setState(prevState => ({
			register: !prevState.register
		}));
	}
	render() {
		let box = {
			width: '475px',
			height: '500px',
			margin: 'auto',
			marginTop: '100px'
		}
		return (
			<div style={box}>
				{this.state.register ? (
					<div style={{textAlign: 'center'}}>
						<RegisterForm />
						<Button color="link" onClick={this.switch} style={{color: '#373737'}}>
							Back to sign in
						</Button><br/>
					</div>
				) : (<div><SignInForm switch={this.switch} /></div>)}   
			</div>
		);
	}
}

export default Admin;