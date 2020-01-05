import React, {Component} from "react";
import { Card, CardText, CardBody, CardTitle, Button } from 'reactstrap';

class JobCard extends Component {
	constructor(props, title, text){
		super(props);
		this.state = {
			open: false,
		}
		this.togglePanel = this.togglePanel.bind(this);
	}
	togglePanel(e){
		this.setState({open: !this.state.open})
	}	
	render() {
		let card = {
			marginTop: '15px',
			marginRight: '20px',
			fontFamily: 'Quicksand',
		}
		const title = this.props.title;
		const text = this.props.text;
		const date_posted = this.props.date_posted;
		const date_expiry = this.props.date_expired;
		var expired = this.props.expired;
		var text_expired;
		console.log(expired);
		if (expired == true) {
			text_expired = "This job has expired"
		}

		return(
		<div style={card}>
			<Card >
				<CardBody>
					<CardTitle><h5>{title}</h5></CardTitle>
					<CardText>
						<div style={{marginBottom: '10px'}}>
							<div style={{float: 'left', marginRight: '20px'}}>Date Posted: {date_posted}</div>
							<div>Closing Date: {date_expiry}</div>
						</div>
						<p>{text_expired}</p>
						
						<h6>Description</h6>
							<ul>
							{text.split('\n').map(item => 
								<li>{item}</li>
							)}
							</ul>
							</CardText>
					{this.state.open ? (<div>{this.props.children}</div>) : null}
					<div style={{textAlign: 'center'}}>
						<Button color="link" style={{color: '#00bcd4'}} onClick={(e)=>this.togglePanel(e)}>
							{this.state.open ? 'View less' : 'View more'}
						</Button>
					</div>

				</CardBody>
			</Card>
		</div>			
		);
	}
}

export default JobCard;