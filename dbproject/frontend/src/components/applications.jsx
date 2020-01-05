import React, { Component } from 'react';
import NavBar from './navbar';
import ApplicationCard from './appcard';
import { Card, CardBody, CardTitle, Button, FormGroup, Input, Form} from 'reactstrap';
import axios from 'axios';
import ls from 'local-storage'
import { runInThisContext } from 'vm';
import $ from 'jquery'; 

class Applications extends Component {
	constructor(props) {
		super();
		this.handleData = this.handleData.bind(this);
		this.state = {
			data:[], 
			newvalues_degree: 0,
			newvalues_alevels: 0,
			newvalues_languages: 0,
			newvalues_employment: 0,
			newvalues_skills: 0,
			repsonse:null,
			fromChild:'',
			radioValue: 2
		}
	}
	handleData(data) {
		this.setState({
			fromChild:data
		})
	}

	update2degree = (value)=>{
		this.setState({newvalues_degree: value})
	}


	update2alevels = (value)=>{
		this.setState({newvalues_alevels: value})
	}

	update2languages = (value)=>{
		this.setState({newvalues_languages: value})
	}

	update2employment = (value)=>{
		this.setState({newvalues_employment: value})
	}

	update2skills = (value)=>{
		this.setState({newvalues_skills: value})
	}

	getRadio = (value)=>{
		if (value =="accept") {
			this.setState({radioValue: 2})
		} else if (value == "test") {
			this.setState({radioValue: 1})
		} else {
			this.setState({radioValue: 0})
		}

	}

	componentDidMount() {
		var self = this;
		let headers = {
			"AUTH-TOKEN": "randomtesttoken_admin_test_one@gmail.com"
		};
		$.ajax({
			url: "http://localhost:8000/api/applications/accepted_applications/",
			type: 'GET',
			success: res => {
				console.log(res.Applications);
				var test = res.Applications;
				self.setState({ "data": test });
			},
			headers: headers
		});

	}

	onSubmit(job_id, app_id, event) {
		console.log(this.state.newvalues_degree)
		var json = { feedback_given: {"Degree": this.state.newvalues_degree, "A-Levels": this.state.newvalues_alevels, "Languages": this.state.newvalues_languages, "Employment": this.state.newvalues_languages, "Skills": this.state.newvalues_skills, "Response": this.state.radioValue}, "job_id": job_id, "application_id": app_id, "auth_token": "randomtesttoken_admin_test_one@gmail.com"};
		//send to neural
		console.log(json)
		event.preventDefault()
		$.ajax({
			method: 'post',
			url: 'http://localhost:8000/api/applications/submit_feedback/',
			data: JSON.stringify(json),
			success: res => {
				ls.set('auth_token', res.auth_token) //saving token
			},
			error: res => {
				let errors = res.responseJSON.errors;
				console.log(errors);

				// alert("Unexpected error try again");
			}
		});
		event.preventDefault();
	
	
		const data = event.target;

		const newtest = [];
		this.setState({data:newtest})
	}

	handlerfordata=(data)=>{
		console.log("in handler")
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

		console.log(this.state.data)
		const application_length = this.state.data.length;
		return (
			<div>
				<NavBar />
				<div style={{height: '100vh'}}>
					<div style={filter}>
						<h5>Filter</h5>
					</div>
					<div style={jobs}>
						<h4>Applications</h4>
						<p>{application_length} result(s)</p>
						{this.state.data.map(t =>
							
						<Form onSubmit = {this.onSubmit.bind(this, t.job_id, t.ID)}>
						<ApplicationCard updatedegree={this.update2degree} updateskills={this.update2skills} updatealevels={this.update2alevels} updateemployment={this.update2employment} updatelanguages = {this.update2languages} getRadioValue = {this.getRadio} values = {[t.score_degree, t.score_alevels, t.score_lang, t.score_employment, t.score_skills]}>
						
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
							<div style={{textAlign: 'center'}}>
						<Button color="info">Submit</Button>
						</div>			
						</ApplicationCard>
						</Form>
						)}
					</div>
				</div>
			</div>
		);
	}
}

export default Applications;
