import React, { Component } from 'react';
import NavBar from './navbar';
import JobCard from './jobcard';
import { Link } from 'react-router-dom';
import { Button } from 'reactstrap';
import { Form, FormGroup, Label, Input } from 'reactstrap'
import './jobs.css';
import $ from 'jquery'; 
import ls from 'local-storage';


class JobSearch extends Component {

	constructor(props) {
		super(props);
		this.state = {
			// jobs: [],
			test: [],
			locations: [],
			value_checked: null
		}
	}

	componentDidMount() {
		var self = this;
		var headers = {'AUTH-TOKEN': ls.get('auth_token')}
		$.ajax({
			url: "http://localhost:8000/api/jobs/all_jobs/",
			headers: headers,
			type: 'GET',
			success: res => {
				var test = JSON.parse(res.jobs);
				console.log(test);
				console.log("Self is");
				
				console.log(self);
				self.setState({ "test": test });
			}
		})
			
	
			// console.log(jobs);
		
			const locations = {"Location 0": "London", "Location 1": "New York"}

			// console.log(jobs);
			// console.log(locations);
	
			
			console.log(this.state.test)
			this.setState({ locations })
			// console.log(locations);
	
	}

	uncheck(event) {
		var self = this;
		var headers = { 'AUTH-TOKEN': ls.get('auth_token') }
		$.ajax({
			url: "http://localhost:8000/api/jobs/all_jobs/",
			headers: headers,
			type: 'GET',
			success: res => {
				var test = JSON.parse(res.jobs);
				console.log(test);
				console.log("Self is");

				console.log(self);
				self.setState({ "test": test });
			}
		})
		this.setState({
			value_checked: null
		})
	}

	handleClickAvailable(event) {
		var self = this;
		var headers = { 'AUTH-TOKEN': ls.get('auth_token') }
		$.ajax({
			url: "http://localhost:8000/api/jobs/all_available_jobs/",
			headers: headers,
			type: 'GET',
			success: res => {
				var test = JSON.parse(res.jobs);
				console.log(test);
				console.log("Self is");

				console.log(self);
				self.setState({ "test": test });
			}
		})
	
		this.setState({
			value_checked: event.target.id
		})
	}

	handleClickNotAvailable(event) {
		var self = this;
		var headers = { 'AUTH-TOKEN': ls.get('auth_token') }
		$.ajax({
			url: "http://localhost:8000/api/jobs/all_not_available_jobs/",
			headers: headers,
			type: 'GET',
			success: res => {
				var test = JSON.parse(res.jobs);
				console.log(test);
				console.log("Self is");

				console.log(self);
				self.setState({ "test": test });
			}
		})
		this.setState({
			value_checked: event.target.id
		})
	}

	handleClickLocation(location, event) {
		// console.log(location)
		const test = [{"ID": 1, "Title": "Java", "Description": "You will will work as part of a multi-skilled agile team, dedicated to improved automation and tooling to support continuous delivery.\n Your team will work hard to foster increased collaboration and create a Devops culture.\n You will help us to release our software more frequently, efficiently and with less risk.\n You will have the opportunity to work on challenging problems, building high-performance systems to process large volumes of data, using the latest technologies.", "Responsibilities": "Work with with other engineers to support our adoption of continuous delivery\nautomating the building, packaging, testing and deployment of applications\nCreate the tools required to deploy and manage applications effectively in production, with minimal manual effort\n Help teams to adopt modern delivery practices, such as extensive use of automated testing, continuous integration, more frequent releases, blue/greendeployment, canary releases, etc.\n Modify existing applications to make use of containers, infrastructure as aservice and platform as a service; ensure that new applications make use of these technologies and teach others how to use them.\n Configure and manage code repositories, continuous builds, artifact repositories, cloud platforms and other tools\n Contribute towards a culture of learning and continuous improvement within your team and beyond\n Share skills and knowledge in a wide range of topics relating to Devops and software delivery", "PeopleManagement": "As a Assistant Vice President, you will be expected to lead others. For example insharing knowledge, facilitating meetings and workshops, defining new designs andisovering new techniques. In some cases, it may also include elements of team leadership or line management., \nAs a Vice President, your role will include management and leadership responsibilities, such as: Leading teams, Line management, Mentoring and teaching, Discovering new techniques and helping others to adopt them, Leading by example", "SkillsNeeded": "Experience creating and maintaining automated builds, using tools such Team City, Jenkins, Bamboo, etc., Knowledge of scripting languages, such as bash, ruby or python.\n Some experience with general-purpose programming languages preferably Java\n Good understanding of version control systems, branching, merging, etc.\nPractical experience using Git, Using repositories such as Nexus and Artifactory to manage and distributebinary artifacts\n An understanding of automated testing, using tools such as Junit, Cucumber,selenium, Protractor, etc.\nAn understanding of operating systems, platforms and infrastructure. Including Unix and Windows, Docker, virtualization, PaaS and IaaS technologies such as Open Shift\nExperience working in an agile team, practicing Scrum, Kanban or XP \nKnowledge gained in Financial Services environments, for example products instruments, trade lifecycles, regulation, risk, financial reporting or accounting", "IdealCandidate": "The ideal candidate has a strong programming knowledge and experience of working in this field", "Education": "We are happy to consider candidates with a wide variety of educational backgrounds and qualifications. \nQualifications in computer science, STEM subjects, other numerate disciplines, business and economics are beneficial for the role.\nWe also look favourably upon candidates with equivalent practical experience. This could have be gained in the workplace or in other contexts, such as contributing to open source software or working on personal projects.", "Location": "London", "DatePosted": "2019-03-05", "DateExpiry": "2019-03-05", "Expired": true}]
		this.setState({
			test,
			value_checked: event.target.id
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

		console.log("Something else");
		console.log(ls.get('auth_token'));

			const job_length = this.state.test.length;
			const location_length = Object.keys(this.state.locations).length;
			console.log(location_length);
			var location_check = [];

			for (var j = 0; j < location_length; j++) {
	
				location_check.push(<Label check><Input type="radio" name="customRadio" id = {this.state.locations["Location "+j]}onChange={this.handleClickLocation.bind(this, this.state.locations["Location "+j])} checked={this.state.value_checked == this.state.locations["Location "+j]}/><a>{this.state.locations["Location "+j]}</a></Label>)
				location_check.push(<div></div>)
			}
			console.log(location_check)
			return (
				<div>
				<NavBar/>
				<div className="justify-content-between">
					<div style={filter}>
						<h5>Filter</h5>
						<FormGroup check>
							<Label check>
								{/* adapted from https://stackoverflow.com/questions/51514204/uncheck-radio-button-in-reactjs */}
								<Input type="radio" name ="customRadio" id = "available" onChange={this.handleClickAvailable.bind(this)} checked={this.state.value_checked == "available"}/> {' '}
								<a>Available Jobs</a>
								</Label>
								<div>
								</div>
								<Label check>
								<Input type="radio" name ="customRadio" id = "not" onChange={this.handleClickNotAvailable.bind(this)} checked = {this.state.value_checked == "not"}/> {' '}
								<a>Not Available</a>
								</Label>
								<div>
								</div>
								{location_check}
								<br>
								

								</br>
						</FormGroup>
						
						<div>
						<Button color="info" onClick={this.uncheck.bind(this)}>Clear All</Button>
						</div>
					</div>
					<div style={jobs}>
						<h4>Available Opportunities</h4>
						<h7> {job_length} result(s) found</h7>
						
						{this.state.test.map(t => 			
						<JobCard title = {t.Title} text = {t.Description} date_expired = {t.DateExpiry} date_posted = {t.DatePosted} expired = {t.Expired}>
						{/* adpated from https://www.freecodecamp.org/forum/t/newline-in-react-string-solved/68484 */}
							
							<h6>Responsibilities</h6>
							<ul>
							{t.Responsibilities.split('\n').map(item => 
								<li>{item}</li>
							)}
							</ul>
							<h6>People Management</h6>
							<ul>
							{t.PeopleManagement.split('\n').map(item => 
								<li>{item}</li>
							)}
							</ul>
							<h6>Skills Needed</h6>
							<p>You will have experience with a range of tools and techniques that can be used to make software delivery faster and more reliable: </p>
							<ul>
							{t.SkillsNeeded.split('\n').map(item => 
								<li>{item}</li>
							)}
							</ul>
							<h6>Ideal Candidate</h6>
							<ul>
							{t.IdealCandidate.split('\n').map(item => 
								<li>{item}</li>
							)}
							</ul>
							<h6>Education</h6>
							<ul>
							{t.Education.split('\n').map(item => 
								<li>{item}</li>
							)}
							</ul>
							<Button color="info"><Link to={{pathname:"/apply", state:{id : t.ID}}}style={{color: 'white'}}>Apply</Link></Button>
						</JobCard>
					
						)}
	
				</div>
				</div>
				</div>
			)
		//For one json
		// const title = this.state.jobs.title
		// return (
		// 	<ul>
			
		// 	<li>
		// 	{title}
		// 	</li>
		//   </ul>
		// )
	}
}

export default JobSearch

