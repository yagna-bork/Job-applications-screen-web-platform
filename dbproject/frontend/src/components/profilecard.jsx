import React, {Component} from "react";
import { Card, CardText, CardBody, CardTitle, Button } from 'reactstrap';

class ProfileCard extends Component {
	constructor(props){
		super(props);
		this.state = {
			open: false
		}
		this.togglePanel = this.togglePanel.bind(this);
	}
	togglePanel(e){
		this.setState({open: !this.state.open})
	}	
	render() {
		let card = {
			fontFamily: 'Quicksand',
		}			
		return(
		<div style={card}>
			<Card >
				<CardBody>
					<CardTitle><h5>Engineer - Full Stack</h5></CardTitle>
					<CardText>With supporting text below as a natural lead-in to additional content.</CardText>
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

export default ProfileCard;
