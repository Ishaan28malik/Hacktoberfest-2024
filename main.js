var button=document.querySelector("button");
var filled=false;
button.addEventListener("click",function(){
	//alert('connected');
	
	if(filled)
		document.body.style.background="blue";
	else if 
		document.body.style.background="green";
	else 
		docuemnt.body.style.background="red";	
	filled=!filled;
});
