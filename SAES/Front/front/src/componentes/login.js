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
		ev.preventDefault();
		// console.log(this.refs.usuario.state.usuario);
		// this.refs.usuario.state.usuario me permite accceder a las propiedades del ref, el nombre ref
		// esta definido cuando uso el componente
		axios.post('http://127.0.0.1:8000/api/auth/token/login', { username: this.refs.usuario.state.usuario,
																	 password: this.refs.pass.state.password })
			.then(function(response){
				console.log(response.data.auth_token);
				localStorage.setItem('token',response.data.auth_token)
			//Perform action based on response
			}).catch(function(e){
				console.log(e);
			})
	}

	constructor(){
		super();
		// this.state={
		// 	usuario:'',
		// 	pass:'',
		// }
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

			// ref me permite acceder a las propiedades del componente
			<form style={style} method="post" onSubmit={(ev)=>this.send(ev)}>
				<User ref="usuario"/>
				<Pass ref="pass"/>
				<Submit/>
			</form>
			);
	}
}

export default Login;