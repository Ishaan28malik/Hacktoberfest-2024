import React, {Component} from 'react';
import {osName, browserName} from 'react-device-detect';

const onClickHandler = (name) => {

	alert(name);
	
}
const stylebutton = {

 
  padding: "15px 32px",
  textAlign: "center",
  textDecoration: "none",
  display: "inline-block",
  fontSize: "16px",
  margin: "4px 2px",
  cursor: "pointer",
  backgroundColor: "white", 
  color: "black", 
  border: "2px solid #008CBA",
}
const DetectOs = () => {

	return(
		<div> 
			<button className={stylebutton} onClick={() => onClickHandler(osName)}>Click to reveal OS</button>
		
			<button className={stylebutton} onClick={() => onClickHandler(browserName)}>Click to reveal Browser Name</button>
		</div>


	);


}
export default DetectOs;