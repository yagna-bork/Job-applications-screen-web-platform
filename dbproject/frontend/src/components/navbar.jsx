import React, {Component} from 'react';
import SignIn from './modal';
import './navbar.css';
import { Link } from 'react-router-dom';
import { Button } from 'reactstrap';

class NavBar extends Component {
	state = {
		logged_in: true,
	}
	render() {
		let list = {
			listStyleType: 'none',
			margin: '0',
			padding: '0',
		}
		let items = {
			float: 'left',
			margin: '15px',
			textDecoration: 'none',
		}
		let links = {
			color: '#373737'
		}
		return(
			<nav className="navbar navbar-expand navbar-light" style={{margin: '10px', marginLeft: '20px'}}>
				<div>COMPANY NAME</div>
				<button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExample02" aria-controls="navbarsExample02" aria-expanded="false" aria-label="Toggle navigation">
					<span className="navbar-toggler-icon"></span>
				</button>
				<div className="collapse navbar-collapse justify-content-between">
					<div className="navbar-nav">
						<ul style={list}>
							<li style={items}><Link to="/about" style={links}>About Us</Link></li>
							<li style={items}><Link to="/locations" style={links}>Locations</Link></li>
							<li style={items}><Link to="/jobs" style={links}>Job Search</Link></li>
							<li style={items}><Link to="/help" style={links}>How to Apply</Link></li>
						</ul>
					</div>
					<div className="navbar-nav">
						{this.state.logged_in ? 
							<div>
								<Button color="none"><Link to="/profile" style={{color: '#00bcd4'}}>Dashboard</Link></Button>
								<Button color="info"><div style={{color: 'white'}}>Sign out</div></Button>
							</div> 
							: 
							<SignIn />
							}
					</div>
				</div>
			</nav>
		);
	}
}

export default NavBar;