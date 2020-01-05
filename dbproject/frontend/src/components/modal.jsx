import React, { Component } from "react";
import { Button, Modal, ModalHeader, ModalBody } from 'reactstrap';
import SignInForm from './login';
import RegisterForm from './register';
import arrow from './left_arrow.png';

import './modal.css';

class SignIn extends Component {
	constructor(props) {
		super(props);
		this.state = {
			modal: false,
			register: false
		};

		this.toggle = this.toggle.bind(this);
		this.switch = this.switch.bind(this);
	}

	toggle() {
		this.setState(prevState => ({
			modal: !prevState.modal
		}));
	}

	switch() {
		this.setState(prevState => ({
			register: !prevState.register
		}));
	}

	render() {
		return (
			<div>
				<Button color="info" onClick={this.toggle}>Sign in</Button>
				<Modal isOpen={this.state.modal} toggle={this.toggle} className={this.props.className}>
					<ModalHeader toggle={this.toggle}>
						{this.state.register ? (
						<div>
							<Button color="none" onClick={this.switch}>
								<img src={arrow} alt="Back arrow" style={{width: '20px', height: '20px'}} />
							</Button>
						</div>
						) : null}
					</ModalHeader>
					<ModalBody>
						{this.state.register ? (<div><RegisterForm /></div>) : (<div><SignInForm switch={this.switch} /></div>)}		
					</ModalBody>
				</Modal>
			</div>
		);
	}
}

export default SignIn;