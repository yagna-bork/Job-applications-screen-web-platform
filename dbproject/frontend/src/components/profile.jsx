import React, { Component } from 'react';
import NavBar from './navbar';
import ApplicationCard from './appcard';
import { Card, CardBody, CardTitle, Button, FormGroup, Input, Form} from 'reactstrap';
import axios from 'axios';
import ls from 'local-storage';
import $ from 'jquery'; 
import { runInThisContext } from 'vm';
import ProfileCard from './profilecard';

class Profile extends Component {

	state = {
		// jobs: [],
		applications:[],

	}

	componentDidMount() {
		var self = this;
		var headers = { 'AUTH-TOKEN': ls.get('auth_token') }
		$.ajax({
			url: "http://localhost:8000/api/applications/feedback/",
			headers: headers,
			type: 'GET',
			success: res => {
				console.log(res.applications);
				// let stringed = JSON.stringify(res.applications).replace(/\\/g, "");
				// console.log(stringed);
				// console.log(JSON.parse(stringed));
				// // console.log("here");
				var test = res.applications;

				self.setState({ "applications": test });
			}
		})
	
	}

	render() {
		let filter = {
			margin: '15px',
			marginLeft: '40px',
			fontFamily: 'Quicksand',
			width: '25%',
			height: '100vh',
			float: 'left',
		}
		let jobs = {
			margin: '15px',
			fontFamily: 'Quicksand',
			width: '68%',
			height: '100vh',
			float: 'right',
		}
		let welcome = {
			marginLeft: '10%',
			marginRight: '10%',
			height: '200px',
			textAlign: 'center',
			backgroundColor: '#C0C0C0'
		}
		let content = {
			margin: '30px', 
			marginLeft: '10%',
			marginRight: '10%'
		}
		const application_length = this.state.applications.length;
		
		return (
			<div>
				<div style={{fontFamily: 'Quicksand'}}>
					<NavBar />
					<div style={welcome}>
						<h3 style={{lineHeight: '200px'}}>Dashboard</h3>			
					</div>
					<div style={content}>
						<div>
							<h4>Submitted applications</h4>
							<p>{application_length} result(s)</p>
							{this.state.applications.map(t =>
						
						<ProfileCard>
						
						<h6>Degree</h6>
							<ul>
								<li>Degree: {t.DegreeQualification}</li>
								<li>Degree Level: {t.DegreeLevel}</li>
								<li>University Attended: {t.UniversityAttended}</li>
							</ul>
							<h6>A-Levels</h6>
							<ul>
							{t.ALevelQualifications.map(x=>
								<li>Subject: {x.Subject}. Grade: {x.Grade}</li>
							)}
							</ul>
							<h6>Langauges</h6>
							<ul>
							{t.LanguagesKnown.map(x=>
								<li>Language: {x.Language}. Expertise: {x.Expertise}</li>
							)}
							</ul>
							<h6>Previous Employment</h6>
							<ul>
							{t.PreviousEmployment.map(x=>
								<li>Company: {x.Company}. Position: {x.Position}</li>
							)}
							</ul>
							<h6>Skills</h6>
							<ul>
							{t.Skills.map(x=>
								<li>Skill: {x.Skill}. Expertise: {x.Expertise}</li>
							)}
							</ul>
							<h6>Response</h6>
							{t.Response == 0 &&
							<h7>Rejected</h7>
							} 
							{t.Response == 1 &&
							<h7>Further Tests</h7>
							} 

							{t.Response == 2 &&
							<h7>Accepted</h7>
							} 
							<div style={{textAlign: 'center'}}>
						</div>			
						</ProfileCard>
						
						)}
						</div>			
					</div>

				</div>
			</div>
		);
	}
}

export default Profile;