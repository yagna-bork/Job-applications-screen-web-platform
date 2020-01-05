import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Slider from '@material-ui/lab/Slider';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';


const theme = createMuiTheme({
	palette: {
		primary: { main: '#00bcd4' }, // Purple and green play nicely together.
	},
});

const styles = {
	root: {
		width: 300,
	},
	slider: {
		padding: '22px 0px',
	},
};

class ResultSlider extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			value: this.props.value,
			label: props.category,
		}
	}

	handleChange = (event, value) => {

		this.setState({ value });
		this.props.updatestuff(value);
	};

	render() {
		const { classes } = this.props;
		const { value } = this.state;

		return (
			<div className={classes.root}>
			<MuiThemeProvider theme={theme}>
				<div style={{width: '300px', height: '15px'}}>
					<div style={{float: 'left'}}>{this.state.label}</div>
					<div style={{float: 'right'}}>{value}</div>
				</div>
				<Slider
					classes={{ container: classes.slider }}
					value={value}
					min={0}
					max={100}
					step={1}
					onChange={this.handleChange}
				/>
			</MuiThemeProvider>
			</div>
		);
	}
}

ResultSlider.propTypes = {
	classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(ResultSlider);