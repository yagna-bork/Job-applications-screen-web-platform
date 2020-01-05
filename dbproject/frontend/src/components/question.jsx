import React, { Component } from 'react';
import { FormGroup, Input } from 'reactstrap';

class Question extends Component {
	constructor(props) {
		super(props);
		this.state = {
			question: props.q,
			answer1: props.a1,
			answer2: props.a2,
			answer3: props.a3,
			answer4: props.a4,
		}
	}
	render() {
		return (
			<div>
				<div style={{fontSize: '20px'}}>{this.state.question}</div>
				<FormGroup style={{marginLeft: '20px'}}>
					<Input type="radio" name="customRadio" label="Option 1" /> {this.state.answer1} <br/>
					<Input type="radio" name="customRadio" label="Option 2" /> {this.state.answer2} <br/>
					<Input type="radio" name="customRadio" label="Option 3" /> {this.state.answer3} <br/>
					<Input type="radio" name="customRadio" label="Option 4" /> {this.state.answer4} <br/>
				</FormGroup>
			</div>
		);
	}
}

export default Question;