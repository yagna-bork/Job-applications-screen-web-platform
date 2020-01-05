import React, {Component} from 'react';
import { Card, CardBody, CardTitle, Button, FormGroup, Input, Form} from 'reactstrap';
import ResultSlider from './slider';


class ApplicationCard extends Component {
	constructor(props) {
		super(props);
		this.state = {
			open: false,
			values: this.props.values, 
			value_checked: "accept"
			
		}
	
		this.togglePanel = this.togglePanel.bind(this);
	}
	togglePanel(e) {
		this.setState({open: !this.state.open})
	};

	handleChange = (slider, value) => {
	    const newState = {};
	    newState[slider] = value;
	    this.setState(newState);
	};

	onSubmit(event) {
		event.preventDefault();
		this.props.handlerfordata("hi")
	};

	changedxdegree = (value) => {
		console.log(value)
		this.props.updatedegree(value);
	}

	changedxalevels = (value) => {
		this.props.updatealevels(value);
	}

	changedxlanguages = (value) => {
		this.props.updatelanguages(value);
	}

	changedxemployment = (value) => {
		this.props.updateemployment(value);
	}

	changedxskills = (value) => {
		this.props.updateskills(value);
	}

	giveRadioButton = (value) => {
		this.props.getRadio()
	}

	acceptClicked(event) {
		this.setState({ value_checked: event.target.id })
		this.props.getRadioValue(event.target.id)
	}
	testClicked(event) {
		this.setState({ value_checked: event.target.id })
		this.props.getRadioValue(event.target.id)
	}
	notClicked(event) {
		this.setState({ value_checked: event.target.id })
		this.props.getRadioValue(event.target.id)
	}


	render() {
		let card = {
			marginBottom: '15px',
			marginRight: '30px',
			fontFamily: 'Quicksand',

		}
		console.log(this.state.values[0])
		return(
		<div style={card}>
			<Card >
				<CardBody>
					<CardTitle style={{height: '30px'}}>
						<div>
							<div style={{float: 'left'}}>
								
							</div>
							<FormGroup check inline style={{float: 'right'}}>
								<Input type="radio"  name="customRadio"  id="accept" label="Accept" onChange= {this.acceptClicked.bind(this)} checked={this.state.value_checked == "accept"} defaultChecked /> Accept
								<Input type="radio"  onChange= {this.testClicked.bind(this)} id = "test" name="customRadio" label="Decline" style={{marginLeft: '20px'}} checked={this.state.value_checked == "test"} /> Further Tests
								<Input type="radio" onChange= {this.notClicked.bind(this)} id = "not" name="customRadio" label="Decline" style={{marginLeft: '20px'}} checked={this.state.value_checked == "not"} /> Decline
							</FormGroup>
						</div>
					</CardTitle>
					<div style={{height: '225px'}}>
						<div style={{margin: '15px', float: 'left'}}>
							<ResultSlider updatestuff = {this.changedxdegree.bind(this)} value= {this.state.values[0]} category="Degree" />
							<ResultSlider updatestuff= {this.changedxlanguages.bind(this)} value= {this.state.values[2]}  category="Languages" />
							<ResultSlider updatestuff= {this.changedxskills.bind(this)} value= {this.state.values[4]} category="General Skills" />
						</div>
						<div style={{margin: '15px', float: 'right'}}>
							<ResultSlider updatestuff= {this.changedxalevels.bind(this)} value= {this.state.values[1]} category="A-Levels" />
								<ResultSlider updatestuff={this.changedxemployment.bind(this)} value= {this.state.values[3]} category="Work Experience" />
						</div>
					</div>
					{this.state.open ? (<div>{this.props.children}</div>) : null}
					<div style={{textAlign: 'center'}}>
						<Button color="link" style={{color: '#00bcd4'}} onClick={(e)=>this.togglePanel(e)}>
							{this.state.open ? 'Hide application' : 'Show application'}
							
						</Button>
					</div>
				
				</CardBody>

			</Card>
		</div>			
		);
	}
}

export default ApplicationCard;