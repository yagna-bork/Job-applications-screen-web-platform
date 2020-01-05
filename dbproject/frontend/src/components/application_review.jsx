import React, { Component } from 'react';
import { Button, Form, FormGroup, Label } from 'reactstrap';

class ApplicationContent extends Component {
	render() {
		return (
			<FormGroup>
				<Label for="exampleCheckbox">Radios</Label>
				<div>
					<CustomInput type="radio" id="exampleCustomRadio" name="customRadio" label="Select this custom radio" />
					<CustomInput type="radio" id="exampleCustomRadio2" name="customRadio" label="Or this one" />
				</div>
			</FormGroup>		
		);
	}
}

export default ApplicationContent;
