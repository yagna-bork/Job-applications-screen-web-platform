import React, { Component } from 'react';
import { Form } from 'reactstrap';
import Question from './question';
import NavBar from './navbar';

class Test extends Component {
	render() {
		return (
			<div>
				<NavBar />
				<div style={{margin: '30px', marginLeft: '20%px', fontFamily: 'Quicksand'}}>
					<h4>Further Testing</h4>
					<div>
						<Form>
							<Question 
								q="Question 1"
								a1="Option 1"
								a2="Option 2"
								a3="Option 3"
								a4="Option 4"
							/>
						</Form>
					</div>
				</div>
			</div>
		);
	}
}

export default Test;