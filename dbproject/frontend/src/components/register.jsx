import React, { Component } from "react";
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';

class RegisterForm extends Component {
  render() {
	let logo = {
		textAlign: 'center',
		margin: '15px',
		fontFamily: 'Quicksand',
	}
	let formStyle = {
		marginLeft: '85px',
		marginRight: '85px',
		marginTop: '50px',
		marginBottom: '20px',
		textAlign: 'center',
		fontFamily: 'Quicksand',
	}
    return (
		<div>
			<div style={logo}>
				COMPANY NAME
			</div>
			<div style={formStyle}>
				<Form>
					<FormGroup>
						<Label for="firstName" hidden>First Name</Label>
						<Input type="text" name="firstName" placeholder="First Name(s)" />
					</FormGroup>
					{' '}
					<FormGroup>
						<Label for="lastName" hidden>Last Name</Label>
						<Input type="text" name="lastName" placeholder="Last Name" />
					</FormGroup>
					{' '}
					<FormGroup>
						<Label for="email" hidden>Email</Label>
						<Input type="email" name="email" placeholder="Email" />
					</FormGroup>
					{' '}
					<FormGroup>
						<Label for="password" hidden>Password</Label>
						<Input type="password" name="password" placeholder="Password" />
					</FormGroup>
					{' '}
					<FormGroup>
						<Label for="passwordConf" hidden>Confirm Password</Label>
						<Input type="password" name="passwordConf" placeholder="Confirm Password" />
					</FormGroup>
					{' '}
					<FormGroup>
						<Label for="key" hidden>Registration Key</Label>
						<Input type="password" name="key" placeholder="Registration Key" />
					</FormGroup>
					{' '}
					<Button color="info" style={{margin:'20px'}}>Register</Button><br/>
				</Form>
			</div>
		</div>
    );
  }
}

export default RegisterForm;