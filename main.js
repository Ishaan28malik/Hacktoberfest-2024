var button=document.querySelector("button");
var filled=false;
button.addEventListener("click",function(){
	//alert('connected');
	if(filled)
		document.body.style.background="blue";
	else
		document.body.style.background="green";
	filled=!filled;
});

