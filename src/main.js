var button=document.querySelector("button");
var filled=false;
button.addEventListener("click",function(){
	//alert('connected');
	console.log("BUTTON HAS BEEN CLICKED");
	if(filled)
		document.body.style.background="green";
	else
		document.body.style.background="blue";
	filled=!filled;
});
