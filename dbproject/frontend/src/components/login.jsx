import React, { Component } from "react";
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';
import ls from 'local-storage';
import $ from 'jquery'; 

class SignInForm extends Component {
	state = {
		email: null,
		password: null
	}
	

	submitLogin(event) {
		event.preventDefault()
		var json_data = {"email": this.state.email, "password": this.state.password}
		$.ajax({
			method: 'post',
			url: 'http://localhost:8000/api/auth/login/',
			data: JSON.stringify(json_data),
			success: res => {
				ls.set('auth_token', res.auth_token) //saving token
			},
			error: res => {
				let errors = res.responseJSON.errors;
				console.log(errors);
				for(let i = 0; i < errors.length; i++){
					if (errors[i].error_status === 'LOGIN_DETAILS_INVALID') {
						alert("Login details invalid");
					}
				}

				// alert("Unexpected error try again");
			}
		});
		console.log(json_data)
	}

	handleEmailChange(e) {
		this.setState({email: e.target.value})
	}

	handlePasswordChange(e) {
		this.setState({password: e.target.value})
	}


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
				<Form onSubmit = {this.submitLogin.bind(this)}>
					<FormGroup>
						<Label for="userEmail" hidden>Email</Label>
						<Input type="email" name="email" id="exampleEmail" value = {this.state.email} onChange = {this.handleEmailChange.bind(this)}placeholder="Email" />
					</FormGroup>
					{' '}
					<FormGroup>
						<Label for="userPassword" hidden>Password</Label>
						<Input type="password" name="password" id="examplePassword" value = {this.state.password} onChange = {this.handlePasswordChange.bind(this)} placeholder="Password" />
					</FormGroup>
					{' '}
					<Button color="info"  style={{margin:'20px'}}>Sign in</Button><br/>
					<Button color="link" onClick={this.props.switch} style={{color: '#373737'}}>Register an account</Button><br/>
					<Button color="link" style={{color: '#373737'}}>Reset password</Button>
				</Form>
			</div>
		</div>
    );
  }
}

export default SignInForm;