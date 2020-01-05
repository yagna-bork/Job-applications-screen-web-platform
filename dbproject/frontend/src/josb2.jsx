import React, { Component } from 'react';
import NavBar from './navbar';
import JobCard from './jobcard';
import { Link } from 'react-router-dom';
import { Button } from 'reactstrap';

class JobSearch extends Component {
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
			marginTop: '50px',
			fontFamily: 'Quicksand',
			width: '75%',
			height: '100vh',
		}

		return (
			<div>
				<NavBar />
				<div className="justify-content-between">
					<div style={filter}>
						<h5>Filter</h5>
					</div>
					<div style={jobs}>
						<h4>Available Opportunities</h4>
						<h7>30 results found</h7>
						<JobCard >
							<p>
								Lorem ipsum dolor sit amet, illud deserunt deterruisset no usu, nec ea quis aeterno
								definiebas, eu pri nullam cetero aperiam. Est probo essent id, ei eos inani utamur facilis,
								quo quaestio scriptorem omittantur ei. Et usu quas mazim vivendum. Ad vel persius
								dissentiunt, ut est posse blandit. Denique sensibus vix ex.
							</p>
							<p>
								Eu vis meis offendit mediocrem. Vis at sale minimum. Summo singulis qualisque vix id,
								et eam prima nostrum lobortis. Vel dico aperiri id, evertitur theophrastus cum in, duo 
								ornatus docendi cu.
							</p>
							<Button color="info"><Link to="/apply" style={{color: 'white'}}>Apply</Link></Button>
						</JobCard>
						<JobCard >
							<p>
								Lorem ipsum dolor sit amet, illud deserunt deterruisset no usu, nec ea quis aeterno
								definiebas, eu pri nullam cetero aperiam. Est probo essent id, ei eos inani utamur facilis,
								quo quaestio scriptorem omittantur ei. Et usu quas mazim vivendum. Ad vel persius
								dissentiunt, ut est posse blandit. Denique sensibus vix ex.
							</p>
						</JobCard>
						<JobCard >
							<p>
								Lorem ipsum dolor sit amet, illud deserunt deterruisset no usu, nec ea quis aeterno
								definiebas, eu pri nullam cetero aperiam. Est probo essent id, ei eos inani utamur facilis,
								quo quaestio scriptorem omittantur ei. Et usu quas mazim vivendum. Ad vel persius
								dissentiunt, ut est posse blandit. Denique sensibus vix ex.
							</p>
							<p>
								Eu vis meis offendit mediocrem. Vis at sale minimum. Summo singulis qualisque vix id,
								et eam prima nostrum lobortis. Vel dico aperiri id, evertitur theophrastus cum in, duo 
								ornatus docendi cu.
							</p>
						</JobCard>
					</div>
				</div>
			</div>
		);
	}
}

export default JobSearch;