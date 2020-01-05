import React, { Component } from 'react';
import { Form, Field, ErrorMessage } from 'formik';
import { Button, Progress } from 'reactstrap';
import ApplicationForm from './application_form';
import NavBar from './navbar';
import ls from 'local-storage';

class Application extends Component {
	
	state = {
		a_levels: [],
		employment: [],
		grades: [],
		languages:[],
		skills:[],
		hobbies:[],
		counter:0,
		counter_e:0,
		counter_l:0,
		counter_s:0,
		counter_h:0
		

	}

	// componentDidMount() {
	// 	console.log(this.props.location.state};
	// }



	addLevel(event) {
		this.setState({counter: ++this.state.counter})
		var text = "a_level"+String(this.state.counter);
		var text2 = "grade"+String(this.state.counter);
		this.setState({ a_levels: [this.state.a_levels, <label>A-Level</label>, <Field name={text} component="input" style={{width: '350px'}} />, <label>Grade</label>, <Field name={text2} component="input" style={{width: '350px'}} />]})
	}

	addEmployment(event) {
		this.setState({counter_e: ++this.state.counter_e})
		var text = "company"+String(this.state.counter_e);
		var text2 = "position"+String(this.state.counter_e);
		this.setState({ employment: [this.state.employment, <label>Company</label>, <Field name={text} component="input" style={{width: '350px'}} />, <label>Position</label>, <Field name={text2} component="input" style={{width: '350px'}} />]})
	}

	addLanguage(event) {
		this.setState({counter_l: ++this.state.counter_l})
		var text = "language"+String(this.state.counter_l);
		var text2 = "expertise"+String(this.state.counter_l);
		this.setState({ languages: [this.state.languages, <label>Language</label>,<br></br>,<Field  name={text} component="input" style={{float:'left', width: '200px'}}/>,<Field  name={text2} component="select" style={{width: '100px', height: '30px'}}>
			
			<option value="none">Expertise</option>
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
		</Field>, <br></br>]})
	}

	addSkill(event) {
		this.setState({counter_s: ++this.state.counter_s})
		var text = "skill"+String(this.state.counter_s);
		var text2 = "expertises"+String(this.state.counter_s);
		this.setState({ skills: [this.state.skills, <label>Skill</label>,<br></br>,<Field  name={text} component="input" style={{float:'left', width: '200px'}}/>,<Field  name={text2} component="select" style={{width: '100px', height: '30px'}}>
			
			<option value="none">Expertise</option>
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
		</Field>, <br></br>]})
	}

	addHobby(event) {
		this.setState({counter_h: ++this.state.counter_h})
		var text = "hobby"+String(this.state.counter_h);
		var text2 = "interest"+String(this.state.counter_h);
		this.setState({ hobbies: [this.state.hobbies, <label>Hobby</label>,<br></br>,<Field  name={text} component="input" style={{float:'left', width: '200px'}}/>,<Field  name={text2} component="select" style={{width: '100px', height: '30px'}}>
			
			<option value="none">Interest</option>
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
		</Field>, <br></br>]})
	}


	render () {
		console.log(ls.get('hi'))
		const required = value => (value ? undefined : 'Required');
		let form = {
			margin: 'auto',
			marginTop: '50px',
			fontFamily: 'Quicksand',
			width: '350px'
		}
		console.log(this.props.location.state.id);
		let input = {
			marginBottom: '25px'
		}
		console.log(this.state.counter);
		return(
			<div>
				<NavBar />
				<ApplicationForm
					initialValues={{
						name: "",
						degree: "",
						degree_level: "",
						university: ""
					}}
					onSubmit={(values, actions) => {
						actions.setSubmitting(false);
					}}
					num_alevels = {this.state.counter} num_employment ={this.state.counter_e} num_lang = {this.state.counter_l} num_skills={this.state.counter_s} num_hobbies = {this.state.counter_h} id = {this.props.location.state.id}
				>
					<ApplicationForm.Page>
						<Progress value={25} color="info" />
						<Form style={form}>
							<div style={input}>
								<label>Full Name</label><br/>
								<Field name="name" component="input" validate={required} style={{width: '350px'}} />
								<ErrorMessage name="name" component="div" style={{color: 'red'}}className="field-error" />	 
							</div>
							<div style={input}>
								<label>Degree</label><br/>
								<Field name="degree" component="input" validate={required} style={{width: '350px'}} />
								<ErrorMessage name="name" component="div" style={{color: 'red'}}className="field-error" />		  
							</div>
							<div style={input}>
								<label>Degree Level</label><br/>
								<Field  name="degree_level"component="select" validate={required} style={{width: '350px', height: '30px'}}>
								<option value="none" >- Select -</option>
								<option value="BA">BA - Bachelor of Arts</option>
								<option value="BEng">BEng - Bachelor of Engineering</option>
								<option value="BSc">BSc - Bachelor of Science</option>
								<option value="Masters">Masters</option>
								<option value="PhD">PhD</option>
							</Field>	  
							<ErrorMessage name="name" component="div" style={{color: 'red'}}className="field-error" />	
							</div>
							<div style={input}>
								<label>University/Insitution</label><br/>
								<Field name="university" component="input" validate={required} style={{width: '350px'}} />
								<ErrorMessage name="name" component="div" style={{color: 'red'}}className="field-error" />	  
							</div>
					</Form>
					</ApplicationForm.Page>
					<ApplicationForm.Page>
						<Progress value={50} color="info" />
						<Form style={form}>
							<div style={input}>
								<label>A-Levels</label><br/>
								<label>A-Level</label><br/>
								<Field name="a_level0" component="input" validate={required}style={{width: '350px'}} />
								<label>Grade</label><br/>
								<Field name="grade0" component="input" style={{width: '350px'}} />
								{this.state.a_levels}
								{/* {this.state.grades} */}
								<ErrorMessage name="name" component="div" className="field-error" />
								<Button color="link" onClick = {this.addLevel.bind(this)} style={{color: '#373737'}}>+ Add A-Level</Button>	
							</div>
							<div style={input}>
								<label>Work Experience</label><br/>
								<label>Company</label><br/>
								<Field name="company0" component="input" style={{width: '350px'}} />
								<label>Position</label><br/>
								<Field name="position0" component="input" style={{width: '350px'}} />
								{this.state.employment}
								<ErrorMessage name="name" component="div" className="field-error" />	
								<Button color="link" onClick = {this.addEmployment.bind(this)} style={{color: '#373737'}}>+ Add Employment</Button>
								<br/> 
							</div>
					</Form>
					</ApplicationForm.Page>
					<ApplicationForm.Page>
						<Progress value={75} color="info" />
						<Form style={form}>
							<div style={input}>
								<label>Languages</label><br/>
								<label>Language</label><br/>
								<Field name="language0" component="input" validate={required} style={{float:'left', width: '200px'}} />
						
								<Field  name="expertise0"component="select" style={{width: '100px', height: '30px'}}>
									<option value="none">Expertise</option>
									<option value="1">1</option>
									<option value="2">2</option>
									<option value="3">3</option>
									<option value="4">4</option>
									<option value="5">5</option>
									<option value="6">6</option>
									<option value="7">7</option>
									<option value="8">8</option>
									<option value="9">9</option>
									<option value="10">10</option>
								</Field>
								{this.state.languages}
						
								<Button color="link" onClick = {this.addLanguage.bind(this)} style={{color: '#373737'}}>+ Add Language</Button>  
								<ErrorMessage name="name" component="div" className="field-error" />	  
							</div>
							<div style={input}>
								<label>Skills</label><br/>
								<label>Skill</label><br/>
								<Field name="skill0" component="input" validate={required} style={{width: '200px'}}/>

								<Field  name="expertises0"component="select" style={{width: '100px', height: '30px'}}>
								<option value="none">Expertise</option>
								<option value="1">1</option>
								<option value="2">2</option>
								<option value="3">3</option>
								<option value="4">4</option>
								<option value="5">5</option>
								<option value="6">6</option>
								<option value="7">7</option>
								<option value="8">8</option>
								<option value="9">9</option>
								<option value="10">10</option>
							</Field>
							<br></br>
							{this.state.skills}
			
							<Button color="link" onClick = {this.addSkill.bind(this)} style={{color: '#373737'}}>+ Add Skill</Button>  
							</div>
							<div style={input}>
								<label>Hobbies</label><br/>
								<label>Hobby</label><br/>
								<Field  name="hobby0"component="input" style={{float:'left', width: '200px'}}/>
							
								<Field  name="interest0"component="select" style={{width: '100px', height: '30px'}}>
								
								<option value="none">Expertise</option>
								<option value="1">1</option>
								<option value="2">2</option>
								<option value="3">3</option>
								<option value="4">4</option>
								<option value="5">5</option>
								<option value="6">6</option>
								<option value="7">7</option>
								<option value="8">8</option>
								<option value="9">9</option>
								<option value="10">10</option>
							</Field>
							<div>

							</div>
							{this.state.hobbies}

							<Button color="link" onClick = {this.addHobby.bind(this)} style={{color: '#373737'}}>+ Add Hobby</Button>  
				
						 
							</div>
					</Form>
					</ApplicationForm.Page>
					<ApplicationForm.Page>
						<Progress value={100} color="info" />
						<div style={form}>
							<h4>Please review you application throroughly before submitting.</h4>
							<br/><br/>
						</div>
					</ApplicationForm.Page>
				</ApplicationForm>
			</div>
		);
	}
}

export default Application;