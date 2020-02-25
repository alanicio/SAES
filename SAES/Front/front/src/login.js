import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar} from 'react-bootstrap';
import {Nav} from 'react-bootstrap';
import {NavDropdown} from 'react-bootstrap';
import {Button} from 'react-bootstrap';
import {Email,Pass,Submit} from './forms.js'


class Login extends React.Component{
	render(){
		const style={
			marginRight:"40%",
			marginLeft:"40%",
			marginTop:"10%",
		}
		return(
			<form style={style}>
				<Email/>
				<Pass/>
				<Submit/>
			</form>
			);
	}
}

export default Login;