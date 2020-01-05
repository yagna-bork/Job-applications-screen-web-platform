import React, { Component } from 'react';
import { Formik } from 'formik';
import { Button } from 'reactstrap';
import { Link } from 'react-router-dom';
import ls from 'local-storage';
import $ from 'jquery';

class ApplicationForm extends Component {
	static Page = ({ children }) => children;

	constructor(props) {
		super(props);
		this.state = {
			page: 0,
			values: props.initialValues,
			num: props.num_alevels
		};
	}



	next = values =>
		this.setState(state => ({
			page: Math.min(state.page + 1, this.props.children.length - 1),
			values,
		}));

	previous = () =>
		this.setState(state => ({
			page: Math.max(state.page - 1, 0),
		}));

	validate = values => {
		console.log("hi")
		const activePage = React.Children.toArray(this.props.children)[
			this.state.page
		];
		return activePage.props.validate ? activePage.props.validate(values) : {};
	};

	handleSubmit = (values, bag) => {
		const { children, onSubmit } = this.props;
		const { page } = this.state;
		const isLastPage = page === React.Children.count(children) - 1;
		if (isLastPage) {
			return onSubmit(values, bag);
		} else {
			bag.setTouched({});
			bag.setSubmitting(false);
			this.next(values);
		}
		console.log(values)


	};

	submit = (values) => {
		var data = values;
		var num_alevels = this.props.num_alevels;
		var num_lang = Number(this.props.num_lang);
		var num_employment = Number(this.props.num_employment);
		var num_skills = Number(this.props.num_skills);
		var num_hobbies = Number(this.props.num_hobbies);
		var a_levels = [];
		var languages = [];
		var employment = [];
		var skills = [];
		var hobbies = [];
		for (var i = 0; i < num_alevels+1; i++) {
			console.log("hi")
			a_levels.push({'Subject': values["a_level"+i], 'Grade': values["grade"+i]})
		}

		for (var i = 0; i < num_lang+1; i++) {
			console.log("hi")
			languages.push({'Language': values["language"+i], 'Expertise': values["expertise"+i]})
		}

		for (var i = 0; i < num_skills+1; i++) {
			console.log("hi")
			skills.push({'Skill': values["skill"+i], 'Expertise': values["expertises"+i]})
		}

		for (var i = 0; i < num_employment+1; i++) {
			console.log("hi")
			employment.push({'Company': values["company"+i], 'Position': values["position"+i]})
		}

		for (var i = 0; i < num_hobbies+1; i++) {
			console.log("hi")
			hobbies.push({'Hobby': values["hobby"+i], 'Interest': values["interest"+i]})
		}


		var json_data = {"Name": values.name, "DegreeQualification": values.degree, "DegreeLevel": values.degree_level, "UniversityAttended": values.university, "ALevelQualifications": a_levels, "LanguagesKnown": languages, "PreviousEmployment": employment, "Skills": skills, "Hobbies": hobbies, "job_id": this.props.id, "auth_token": ls.get("auth_token")}

		console.log(json_data)

		$.ajax({
			url: 'http://localhost:8000/api/applications/submit/',
			method: 'post',
			data: JSON.stringify(json_data),
			success: res => {
				console.log(res);
			},
			error: err => {
				console.log(err);
			}
		});
	}

	render() {
		const { children } = this.props;
		const { page, values } = this.state;
		const activePage = React.Children.toArray(children)[page];
		const isLastPage = page === React.Children.count(children) - 1;
		return (
			<Formik
				initialValues={values}
				enableReinitialize={false}
				validate={this.validate}
				onSubmit={this.handleSubmit}
				render={({ values, handleSubmit, isSubmitting, handleReset }) => (
					<form onSubmit={handleSubmit}>
						{activePage}
						<div style={{width: '350px', margin: 'auto'}}>
							{page > 0 && (
								<div style={{float: 'left'}}>
									<Button color="info" onClick={this.previous}>
										« Previous
									</Button>
								</div>
							)}

							{!isLastPage &&
								<div style={{float: 'right'}}>
									<Button color="info" type="submit">Next »</Button>
								</div>
							}
							{isLastPage && (
								<div style={{float: 'right'}}>
									<Button color="info" onClick={this.submit.bind(this, this.state.values)} type="submit">

										<Link to="/jobs" style={{color:"white"}}>Submit</Link>
									</Button>
								</div>
							)}
						</div>
					</form>
				)}
			/>
		);
	}
}

export default ApplicationForm;