import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';


class Personas extends React.Component{

	componentDidMount() {
	    window.addEventListener('load', this.getPersonas);
	}

	render(){
		return(
			<div>
				<h1>Personas</h1>
			</div>
			);
	}

	getPersonas=()=>{
		axios.get('http://127.0.0.1:8000/personas/',{
			headers:{
				'Authorization':' Token '+localStorage.getItem('token'),
			}
		}).then(
			(response)=>{
				console.log(response);
			}
		).catch();
	}
}

export default Personas;