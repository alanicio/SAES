import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar} from 'react-bootstrap';
import {Nav} from 'react-bootstrap';
import {NavDropdown} from 'react-bootstrap';
import {Button} from 'react-bootstrap';
import {Email,Pass,Submit,User} from './forms.js'
// Libreria para ajax creo, xD es para el POST
import axios from 'axios';


class Login extends React.Component{
	// Para probar funciones flechas y eventos
	// prueba=(ev)=>{
	// 	alert(ev.type);
	// 	ev.preventDefault();
	// }

	send=(ev)=>{
		alert("prueba1");
		ev.preventDefault();
		axios.post('/api/register', 'a')
			.then(function(response){
				console.log(response);
		//Perform action based on response
			})
	}

	constructor(){
		super();
		this.state={
			formFields:{data:''}
		}
	}
	render(){
		const style={
			marginRight:"40%",
			marginLeft:"40%",
			marginTop:"10%",
		}
		return(
			// probando los triggers como argumentos
			// <form style={style} onSubmit={(ev)=>this.prueba(ev)} method="post">
			// 	<User/>
			// 	<Pass/>
			// 	<Submit/>
			// </form>
			<form style={style} method="post" onSubmit={(ev)=>this.send(ev)}>
				<User/>
				<Pass/>
				<Submit/>
			</form>
			);
	}
}

export default Login;