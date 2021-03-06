import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar} from 'react-bootstrap';
import {Nav} from 'react-bootstrap';
import {NavDropdown} from 'react-bootstrap';
import {Button} from 'react-bootstrap';
import {Form} from 'react-bootstrap';

class Email extends React.Component{
	render(){
		return(
			<Form.Group controlId="formBasicEmail">
				<Form.Label>Email address</Form.Label>
				<Form.Control type="email" placeholder="Enter email" />
			</Form.Group>
			);	
	}
}

class User extends React.Component{
	constructor(props){
		super(props);
		this.state={
			usuario:'',
		};
	}

	handleUserChange=(event)=>{
		this.setState({usuario:event.target.value});
	}

	render(){
		return(
			<Form.Group controlId="formBasicUser">
				<Form.Label>User</Form.Label>
				<Form.Control type="text" placeholder="Enter User" name="username" onChange={this.handleUserChange}/>
			</Form.Group>
			);	
	}
}

class Pass extends React.Component{
	constructor(props){
		super(props);
		this.state={
			password:'',
		};
	}

	handlePassChange=(event)=>{
		this.setState({password:event.target.value});
	}
	render(){
		return(
			<Form.Group controlId="formBasicPassword">
				<Form.Label>Password</Form.Label>
				<Form.Control type="password" placeholder="Password" name="password" onChange={this.handlePassChange}/>
			</Form.Group>
			);	
	}
}

class Submit extends React.Component{
	render(){
		return(
			<Button variant="primary" type="submit">
			    Submit
			</Button>
		);
	}
}


export {
	Email,
	Pass,
	Submit,
	User
}